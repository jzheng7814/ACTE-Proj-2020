from backend import get_credentials, remove_whitespace, unique, remove_punctuation
from tkinter import Tk, OptionMenu, StringVar, Entry, Label, Button
from oauth2client.service_account import ServiceAccountCredentials
from gspread.models import Worksheet
from typing import List, Dict
from re import sub, split
import gspread
import pprint

root = Tk()

class Date:
    def __init__(self, month = StringVar(root), day = StringVar(root), year = StringVar(root), hour = StringVar(root), minute = StringVar(root), second = StringVar(root)):
        self.month, self.day, self.year, self.hour, self.minute, self.second = month, day, year, hour, minute, second

    def __str__(self):
        return self.year.get().rjust(4, ' ') + self.month.get().rjust(2, ' ') + self.day.get().rjust(2, ' ') + self.hour.get().rjust(2, '0') + self.minute.get().rjust(2, '0') + self.second.get().rjust(2, '0')

def rearrange(spec : str) -> str:
    f = split('[:/ ]', spec)
    return f[2].rjust(4, ' ') + f[0].rjust(2, ' ') + f[1].rjust(2, ' ') + f[3].rjust(2, '0') + f[4].rjust(2, '0') + f[5].rjust(2, '0')

def write_row(sheet : Worksheet, data : List[str], row : int) -> None:
    cells = sheet.range('A' + str(row) + ':F' + str(row))
    for i, j in zip(cells, data):
        i.value = j
    sheet.update_cells(cells)

def write_to_sheet(sheet : Worksheet, data : List[Dict[str, str]], column_headers : List[str]) -> None:
    row = 2
    for i in data:
        write_row(sheet, i.values(), row)
        row += 1

def remove_meaningless_keys(data : List[Dict[str, str]]) -> None:
    for i in data:
        new_keys = []
        to_pop_keys = []
        for j in i:
            new_key = remove_punctuation(remove_whitespace(j)).lower()

            if new_key in {'score', 'emailaddress', 'lastname', 'firstname', 'timestamp', 'block'}:
                new_keys.append((new_key, j))
            else:
                to_pop_keys.append(j)

        for j, k in new_keys:
            if j in {'lastname', 'firstname'}:
                i[k] = ''.join(i[k].split()).lower().capitalize()
            i[j] = i[k]
            i.pop(k)
        for j in to_pop_keys:
            i.pop(j)

def arrange_table() -> None:
    global link, date

    client = gspread.authorize(get_credentials(['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']))
    sheet = client.open_by_url(link.get()).sheet1
    data = sheet.get_all_records()
    sheet.clear()

    column_map = ['timestamp', 'emailaddress', 'lastname', 'firstname', 'score', 'block']

    if len(data) == 0: return

    remove_meaningless_keys(data)
    data = sorted(data, key = lambda i: i['score'], reverse = True)
    data = unique(data, key = lambda i: i['emailaddress'])
    data.sort(key = lambda i: i['lastname'])
    data.sort(key = lambda i: i['block'])
    
    write_row(sheet, ['Timestamp:', 'Email Address:', 'LAST Name:', 'FIRST Name:', 'Score:', 'Block:'], 1)
    data = filter(lambda i, cutoff = str(date): rearrange(i['timestamp']) < cutoff, data)
    write_to_sheet(sheet, data, column_map)
        

date = Date()
date.month.set('MM')
date.day.set('DD')
date.year.set('YYYY')
date.second.set('SS')
date.minute.set('MM')
date.hour.set('HH')
OptionMenu(root, date.month, *range(1, 13),).grid(row = 1, column = 1)
Label(root, text = '/').grid(row = 1, column = 2)
OptionMenu(root, date.day, *range(1, 32)).grid(row = 1, column = 3)
Label(root, text = '/').grid(row = 1, column = 4)
OptionMenu(root, date.year, *range(2019, 2040)).grid(row = 1, column = 5)
Label(root, text = ' ').grid(row = 1, column = 6)
OptionMenu(root, date.hour, *range(00, 24)).grid(row = 1, column = 7)
Label(root, text = ':').grid(row = 1, column = 8)
OptionMenu(root, date.minute, *range(00, 60)).grid(row = 1, column = 9)
Label(root, text = ':').grid(row = 1, column = 10)
OptionMenu(root, date.second, *range(00, 60)).grid(row = 1, column = 11)

Label(root, text = 'Link to spreadsheet: ', font = ('Times New Roman', 24)).grid(row = 0, column = 0)
link = Entry(root, width = 50, font = ('Times New Roman', 24))
link.grid(row = 0, column = 1, columnspan = 11)
Label(root, text = 'Timestamp cutoff: ', font = ('Times New Roman', 24)).grid(row = 1, column = 0)

Button(root, text = 'Arrange data', font = ('Times New Roman', 24), command = arrange_table, bg = 'green').grid(row = 2, column = 0, columnspan = 12, sticky = 'NESW')
root.mainloop()