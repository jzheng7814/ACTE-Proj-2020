from tkinter import Label, Button, OptionMenu, Tk, StringVar, Entry
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from tempfile import TemporaryFile
from dataclasses import dataclass
from collections import deque
from bs4 import BeautifulSoup
from pickle import load, dump
from threading import Thread
from itertools import chain
from os.path import exists
from random import choice
from re import sub, match
from requests import get
from os import makedirs

credentials = None
if exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        credentials = load(token)
if not credentials or not credentials.valid:
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', 'https://www.googleapis.com/auth/documents')
    credentials = flow.run_local_server(port = 0)
    with open('token.pickle', 'wb') as token:
        dump(credentials, token)

service = build('docs', 'v1', credentials=credentials)

def read_paragraph_element(element):
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')

def read_strucutural_elements(elements):
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_strucutural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text


def get_doc_text(DOCUMENT_ID):
    global service
    doc = service.documents().get(documentId = DOCUMENT_ID).execute()
    return read_strucutural_elements(doc.get('body').get('content'))

@dataclass
class vocab_word:
    word : str
    definition : str

term_lookup_table = {}
write = TemporaryFile()

def process_word(word):
    while term_lookup_table[word.word] == 'Pending': pass
    text = term_lookup_table[word.word].prettify()
    text = text[text.find('window.INITIAL_STATE = {') + 24:]
    text = text[:text.find('</script>')]

    synonyms = text[text.find('"synonyms":') + 11:text.find('"antonyms":')]
    synonyms = [j[8:-1] for j in filter(lambda i: match('"term":".+"', i),
                                        chain(*[i.split(',') for i in sub('[{\[\]]', '', synonyms).split('},')]))]

    antonyms = text[text.find('"antonyms":') + 11:text.find('"exampleSentences":')]
    antonyms = [j[8:-1] for j in filter(lambda i: match('"term":".+"', i),
                                        chain(*[i.split(',') for i in sub('[{\[\]]', '', antonyms).split('},')]))]

    example_sentences = text[text.find('"exampleSentences":') + 19:text.find('"relatedWordsAPIData":')]
    example_sentences = [j[12:-1] for j in filter(lambda i: match('"sentence":".+"', i),
                                                  chain(*[i.split(',') for i in sub('[{\[\]]', '', example_sentences).split('},')]))]

    return word.word, word.definition, synonyms, antonyms, example_sentences

def add_word(word):
    def add_info_to_table(wd):
        term_lookup_table[wd] = BeautifulSoup(get('https://www.thesaurus.com/browse/' + wd + '?s=t').content, 'html5lib')

    term_lookup_table[word] = 'Pending'
    Thread(target = add_info_to_table, args = tuple([word])).start()

def parse(DOCUMENT_ID):
    vocab_words = []
    x = ''.join([j + '\n' for j in filter(lambda i: i != '\n', get_doc_text(DOCUMENT_ID).split('\n')[1:])])
    text = deque(filter(lambda i: i != '-', x.split()))
    text.popleft()
    length = len(text)

    while length > 0:
        vocab_words.append(vocab_word(text.popleft(), ''))
        add_word(vocab_words[-1].word)
        txt = text.popleft()
        length -= 2
        while not match('[0-9]+\.', txt) and length >= 0:
            vocab_words[-1].definition += txt + ' '
            if length > 0:
                txt = text.popleft()
            length -= 1

    return vocab_words


def get_details(DOCUMENT_ID):
    for i in parse(DOCUMENT_ID):
        yield process_word(i)
    return None

def get_two_from_list(l):
    r = []
    if len(l) > 5:
        sentences = choice(l[:5])
        l.remove(sentences)
        r.append(sentences)
        sentences = choice(l[:4])
        r.append(sentences)
    elif len(l) >= 2:
        r.append(l[0])
        r.append(l[1])
    else:
        r = l
    return r

root = Tk()
warning_label = Label(root, text = '', font = ('Times New Roman', 20))
warning_label.grid(row = 2, column = 0, columnspan = 2)
v = StringVar()
v.set('(Choose)')

def create(DOCUMENT_LINK):
    if DOCUMENT_LINK.find('docs.google.com/document/d/') == -1: warning_label['text'] = 'INVALID LINK FORMAT'
    else: warning_label['text'] = 'Creating file at C:\\quickstart\\data.txt...'
    root.update()
    DOCUMENT_ID = DOCUMENT_LINK[DOCUMENT_LINK.find('docs.google.com/document/d/') + 27:]
    DOCUMENT_ID = DOCUMENT_ID[:DOCUMENT_ID.find('/')]
    path = r'C:\quickstart'
    if not exists(path):
        makedirs(path)
    with open('C:\\quickstart\\data.txt', 'w') as outfile:
        if v.get() == 'Sentences/Synonyms/Antonyms':
            data = []
            newdoc = service.documents().create().execute()
            for i in get_details(DOCUMENT_ID):
                data.append(i)
            for i in range(5):
                service.documents().batchUpdate(documentId = newdoc.get('documentId'), body = {'requests': []})
        elif v.get() == 'Flashcards':
            x = ''.join([j + '\n' for j in filter(lambda i: i != '\n', get_doc_text(DOCUMENT_ID).split('\n')[1:])])
            text = deque(filter(lambda i: i != '-', x.split()))
            text.popleft()
            length = len(text)

            while length > 0:
                outfile.write(text.popleft() + '\t')
                txt = text.popleft()
                length -= 2
                while not match('[0-9]+\.', txt) and length >= 0:
                    outfile.write(txt + ' ')
                    if length > 0:
                        txt = text.popleft()
                    length -= 1
                outfile.write('\n')
        else:
            raise ValueError


    warning_label['text'] = 'File at C:\\quickstart\\data.txt created, check for data'
    root.update()

Label(root, text = "Link:", font = ('Times New Roman', 20)).grid(row = 0, column = 0)
e = Entry(root, width = 50, font = ('Times New Roman', 20))
e.grid(row = 0, column = 1)
Button(root, text = 'Run', font = ('Times New Roman', 20), command = lambda i=e: create(e.get()), bg = 'green').grid(row = 0, column = 2)
c = OptionMenu(root, v, '(Choose)', 'Sentences/Synonyms/Antonyms', 'Flashcards')
c.grid(row = 1, column = 0)
root.mainloop()