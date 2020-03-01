from google_auth_oauthlib.flow import InstalledAppFlow
from pickle import load, dump
from os.path import exists

def auth():
    if exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = load(token)
    else:
        credentials = InstalledAppFlow.from_client_secrets_file('client_secrets.json', 'https://www.googleapis.com/auth/spreadsheets').run_local_server(port = 0)

    return credentials
