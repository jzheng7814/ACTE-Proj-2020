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
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', 'https://www.googleapis.com/auth/drive')
    credentials = flow.run_local_server(port = 0)
    with open('token.pickle', 'wb') as token:
        dump(credentials, token)

service = build('docs', 'v1', credentials=credentials)


requests = \
[
    {
        'insertTable' : {'rows' : 4, 'columns' : 4, 'endOfSegmentLocation' : {'segmentId' : ''}},
    }
]

result = service.documents().batchUpdate(documentId='1aPknNebJ0lIez5iwHt0a3UhL8luVGPuJTPCJgID5dGU', body={'requests': requests}).execute()
document = service.documents().get(documentId='1aPknNebJ0lIez5iwHt0a3UhL8luVGPuJTPCJgID5dGU').execute()
table = document['body']['content'][2]

requests = \
[
    {
        'insertText' : \
            {
                'location': \
                    {
                        'index': table['table']['tableRows'][0]['tableCells'][0]['content'][0]['startIndex']
                    },
                'text' : 'Hello :P'
            }
    }
]

result = service.documents().batchUpdate(documentId='1aPknNebJ0lIez5iwHt0a3UhL8luVGPuJTPCJgID5dGU', body={'requests': requests}).execute()
print('done')

