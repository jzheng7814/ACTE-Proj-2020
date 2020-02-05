from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pickle import load, dump
from os.path import exists
from json import dumps

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
id = '1IxikvJjNvFTW2AassEuoa0Ukg0KGM5OzcagB9jhFj0M'

service.documents().batchUpdate(
    documentId = id,
    body = \
    [{
        
    }]
)
