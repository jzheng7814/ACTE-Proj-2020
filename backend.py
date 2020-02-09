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
from json import dumps


credentials = None
if exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        credentials = load(token)
if not credentials or not credentials.valid:
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', 'https://www.googleapis.com/auth/drive')
    credentials = flow.run_local_server(port = 0)
    with open('token.pickle', 'wb') as token:
        dump(credentials, token)

service = build('docs', 'v1', credentials = credentials)

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

def get_two_from_list(l):
    if len(l) >= 2:
        return l[:2]
    else:
        return l

def process_word(word):
    text = BeautifulSoup(get('https://www.thesaurus.com/browse/' + word.term + '?s=t').content, 'html5lib').prettify()
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

    if len(example_sentences) == 0:
        example_sentences = ['']
    word.synonyms = ', '.join(get_two_from_list(synonyms))
    word.antonyms = ', '.join(get_two_from_list(antonyms))
    word.sentence = choice(example_sentences)
    return word

@dataclass
class word:
    term : str
    parts_of_speech : str
    definition : str
    antonyms : str
    synonyms : str
    sentence : str

words = []
unused = None
filename = get_doc_text('195NrVPNtTsKQJLsPtRt3qcVfxctTahP0rB4EUmrffqU').split('\n')[0]
x = ''.join([j + '\n' for j in filter(lambda i: i != '\n', get_doc_text('195NrVPNtTsKQJLsPtRt3qcVfxctTahP0rB4EUmrffqU').split('\n')[1:])])
text = deque(filter(lambda i: i != '-', x.split()))
text.popleft()
length = len(text)

while length > 0:
    words.append(word('', '', '', '', '', ''))
    words[-1].term = text.popleft()
    txt = text.popleft()
    length -= 2
    while not match('[0-9]+\.', txt) and length >= 0:
        if match('\([a-zA-Z]+\)', txt):
            if words[-1].parts_of_speech != '':
                words[-1].parts_of_speech += '; '
            if words[-1].definition != '':
                words[-1].definition = words[-1].definition[:-1]
                words[-1].definition += '; '
            words[-1].parts_of_speech += txt + ''
            txt = text.popleft()
        elif length > 0:
            words[-1].definition += txt + ' '
            txt = text.popleft()
        length -= 1

words = map(process_word, words)

requests = [{
      'insertTable': {
          'rows': 20,
          'columns': 4,
          'endOfSegmentLocation': {
            'segmentId': ''
          }
      },
  }
  ]

docid = service.documents().create(
    body = {
        'title' : filename
    }
).execute().get('documentId')

service.documents().batchUpdate(
    documentId = docid,
    body = {'requests' : requests}
).execute()

doc = service.documents().get(documentId = docid).execute()
table = doc['body']['content'][2]

requests = [
            {
                'updateTableRowStyle' : {
                    'tableStartLocation': {'index': 2},
                    'rowIndices': [],
                    'tableRowStyle': {
                        'minRowHeight': {
                            'magnitude': 175,
                            'unit': 'PT'
                        }
                    },
                    'fields': '*'
                }
            },
            {
                'updateDocumentStyle' : {
                    'documentStyle': {
                        'marginTop' : {
                            'magnitude' : 23,
                            'unit' : 'PT'
                        },

                        'marginBottom' : {
                            'magnitude' : 30,
                            'unit' : 'PT'
                        },

                        'marginLeft' : {
                            'magnitude' : 30,
                            'unit' : 'PT'
                        },

                        'marginRight' : {
                            'magnitude' : 30,
                            'unit' : 'PT'
                        }
                    },
                    'fields' : 'marginTop,marginBottom,marginRight,marginLeft'
                }
            }
        ]

service.documents().batchUpdate(
    documentId = docid,
    body = {'requests' : requests}
).execute()

doc = service.documents().get(documentId = docid).execute()
table = doc['body']['content'][2]

def ignore():
    global table
    for i, j in zip([((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)) for i in range(0, 20, 2) for j in range(0, 4, 2)], words):
        requests = [{
            'insertText' : {
                'location' : {
                    'index' : table['table']['tableRows'][i[0][0]]['tableCells'][i[0][1]]['content'][0]['startIndex']
                },
                'text' : f'Word: {j.term}\n\n\nParts of speech: {j.parts_of_speech}\n\n\nDefinition: {j.definition}'
            }
        }]

        service.documents().batchUpdate(
            documentId = docid,
            body = {'requests' : requests}
        ).execute()

        doc = service.documents().get(documentId = docid).execute()
        table = doc['body']['content'][2]

        requests = [{
            'insertText' : {
                'location' : {
                    'index' : table['table']['tableRows'][i[1][0]]['tableCells'][i[1][1]]['content'][0]['startIndex']
                },
                'text' : 'Draw a picture to help you remember/understand the word.'
            }
        }]

        service.documents().batchUpdate(
            documentId = docid,
            body = {'requests' : requests}
        ).execute()

        doc = service.documents().get(documentId = docid).execute()
        table = doc['body']['content'][2]

        requests = [{'insertText' : {
                'location' : {
                    'index' : table['table']['tableRows'][i[2][0]]['tableCells'][i[2][1]]['content'][0]['startIndex']
                },
                'text' : f'Use the word in your own sentence.\n\n{j.sentence}'
            }
        }]

        service.documents().batchUpdate(
            documentId = docid,
            body = {'requests' : requests}
        ).execute()

        doc = service.documents().get(documentId = docid).execute()
        table = doc['body']['content'][2]

        requests = [{'insertText' : {
                'location' : {
                    'index' : table['table']['tableRows'][i[3][0]]['tableCells'][i[3][1]]['content'][0]['startIndex']
                },
                'text' : f'Synonyms: {j.synonyms}\n\n\nAntonyms: {j.antonyms}'
            }
        }]

        service.documents().batchUpdate(
            documentId = docid,
            body = {'requests' : requests}
        ).execute()

        doc = service.documents().get(documentId = docid).execute()
        table = doc['body']['content'][2]

ignore()
