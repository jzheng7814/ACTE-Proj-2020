from backend import get_credentials, remove_whitespace, unique, remove_punctuation
from tkinter import Tk, OptionMenu, StringVar, Entry, Label, Button
from oauth2client.service_account import ServiceAccountCredentials
from re import sub, split
import gspread

root = Tk()

class Date:
    def __init__(self, month = StringVar(root), day = StringVar(root), year = StringVar(root), hour = StringVar(root), minute = StringVar(root), second = StringVar(root)):
        self.month, self.day, self.year, self.hour, self.minute, self.second = month, day, year, hour, minute, second

    def __str__(self):
        return self.year.get().rjust(4, ' ') + self.month.get().rjust(2, ' ') + self.day.get().rjust(2, ' ') + self.hour.get().rjust(2, '0') + self.minute.get().rjust(2, '0') + self.second.get().rjust(2, '0')

def rearrange(spec):
    f = split('[:/ ]', spec)
    return f[2].rjust(4, ' ') + f[0].rjust(2, ' ') + f[1].rjust(2, ' ') + f[3].rjust(2, '0') + f[4].rjust(2, '0') + f[5].rjust(2, '0')

def arrange_table():
    global link, date

    client = gspread.authorize(get_credentials(['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']))
    sheet = client.open_by_url(link.get()).sheet1
    data = sheet.get_all_records()

    if len(data) == 0:
        return

    for i in data:
        new_keys = []
        to_pop_keys = []
        for j in i:
            new_key = remove_whitespace(j)
            new_key = remove_punctuation(new_key)
            new_key = new_key.lower()

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

    data = sorted(data, key = lambda i: i['score'], reverse = True)

    data = unique(data, key = lambda i: i['emailaddress'])
    data.sort(key = lambda i: i['lastname'])
    data.sort(key = lambda i: i['block'])

    column_map = ['timestamp', 'emailaddress', 'lastname', 'firstname', 'score', 'block']
    cur_row = 2
    sheet.clear()

    cells = sheet.range('A1:F1')
    for i, j in zip(cells, ['Timestamp:', 'Email Address:', 'LAST Name:', 'FIRST Name:', 'Score:', 'Block:']):
        i.value = j
    sheet.update_cells(cells)

    for i in data:
        if rearrange(i['timestamp']) > str(date):
            continue
        cells = sheet.range('A' + str(cur_row) + ':F' + str(cur_row))
        for j, k in zip(cells, column_map):
            j.value = i[k]
        sheet.update_cells(cells)
        cur_row += 1

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