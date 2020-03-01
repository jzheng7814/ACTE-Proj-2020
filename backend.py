from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pickle import load, dump
from typing import Callable
from os.path import exists
from re import sub

_client_secret = 'client_secrets.json'

class credentials_wrapper(Credentials):
    def __init__(self, creds : Credentials):
        super().__init__(creds.token, creds.refresh_token, creds.id_token, creds.token_uri, creds.client_id, creds.client_secret, creds.scopes, creds.quota_project_id)
        self.access_token = creds.token

def set_client_secret_path(new_path : str) -> None:
    _client_secret = new_path

def get_credentials(scopes : list or tuple) -> credentials_wrapper: #note type safety
    credentials = None
    if exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', scopes)
            credentials = flow.run_local_server(port = 0)
            with open('token.pickle', 'wb') as token:
                dump(credentials, token)

    return credentials_wrapper(credentials)

def unique(container : list, key : Callable = lambda i: i) -> list:
    new_container = []
    used_values = set()
    for i in container:
        if key(i) not in used_values:
            new_container.append(i)
            used_values.add(key(i))
    return new_container

def remove_whitespace(string : str) -> str:
    return ''.join(string.split())

def remove_punctuation(string : str) -> str:
    return sub(r'[^\w\s]', '', string)