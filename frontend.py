from oauth2client.service_account import ServiceAccountCredentials
from re import sub, split
from tkinter import *
import gspread
import pprint

root = Tk()

class Date:
    """
       Date class used to represent dates (honestly, more of a @dataclass so I don't have to fool around with 6 more
       global variables. Smh, so much stuff to deal with in this language).
    """
    def __init__(self, month = StringVar(root), day = StringVar(root), year = StringVar(root), hour = StringVar(root), minute = StringVar(root), second = StringVar(root)):
        self.month, self.day, self.year, self.hour, self.minute, self.second = month, day, year, hour, minute, second

    def __str__(self):
        return self.year.get().rjust(4, ' ') + self.month.get().rjust(2, ' ') + self.day.get().rjust(2, ' ') + self.hour.get().rjust(2, '0') + self.minute.get().rjust(2, '0') + self.second.get().rjust(2, '0')

def rearrange(spec):
    """Arranges data into the YYYYMMDDHHMMSS format as Date.__str__() returns."""
    f = split('[:/ ]', spec)
    return f[2].rjust(4, ' ') + f[0].rjust(2, ' ') + f[1].rjust(2, ' ') + f[3].rjust(2, '0') + f[4].rjust(2, '0') + f[5].rjust(2, '0')

def arrange_table():
    """Does the heavy lifting on the data arrangement of the spreadsheet."""

    global link, date

    #bunch of extra authentication hurdles I have to jump through to get to the sheet. -_-.
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #specifies access scope
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)      #retrieves credentials
    client = gspread.authorize(creds)                                                          #authorizes to get access
    sheet = client.open_by_url(link.get()).sheet1                                              #opens the spreadsheet

    used = []
    unique = []
    data = sheet.get_all_records() #gets all data as list of dicts

    if len(data) == 0: #efficiency optimization, checking if empty destroys a lot of request inefficiency
        return

    #resets keys to known values for reference: all punctuation and whitespace are eliminated. Correct spelling was assumed
    for i in data:
        new_keys = [] #contains new keys that need to be made into standard form
        to_pop_keys = []
        for j in i:
            new_key = ''.join(j.lower().split()) #strips all whitespace
            new_key = sub('[:,.]', '', new_key)  #strips all punctuation assumed
            if new_key in {'score', 'emailaddress', 'lastname', 'firstname', 'timestamp', 'block'}: #eliminates all useless keys
                new_keys.append((new_key, j)) #Cannot change length of dict() in iteration
            else:
                to_pop_keys.append(j)         #ditto

        for j, k in new_keys:
            if j in {'lastname', 'firstname'}:
                i[k] = ''.join(i[k].split()).lower().capitalize() #arranges names in case someone tries to do something funny
            i[j] = i[k]                                           #(sighs) someone did cODY. Please.
            i.pop(k)                                              #or how about that /'/.'/' name?
        for j in to_pop_keys:
            i.pop(j)

    data = sorted(data, key = lambda i: i['score'], reverse = True) #Sorts items by score in reverse order
                                                                    #(aids in taking highest score with unique() call)

    #calls ad hoc unique() on elements (email address is used because there are no repeats, last names will repeat)
    for i in data:
        if i['emailaddress'] not in used:
            used.append(i['emailaddress'])
            unique.append(i)

    unique.sort(key = lambda i: i['lastname']) #stable_sort()s by last name
    unique.sort(key = lambda i: i['block'])    #stable_sort()s by block

    column_map = ['timestamp', 'emailaddress', 'lastname', 'firstname', 'score', 'block']
    cur_row = 2
    sheet.clear() #eliminates all data

    #initializes header row
    cells = sheet.range('A1:F1')
    for i, j in zip(cells, ['Timestamp:', 'Email Address:', 'LAST Name:', 'FIRST Name:', 'Score:', 'Block:']):
        i.value = j
    sheet.update_cells(cells)

    #pastes rest of data to table in arranged order
    for i in unique:
        if rearrange(i['timestamp']) > date.__str__(): #eliminates all submissions after due time
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