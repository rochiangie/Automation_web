import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Autenticación
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Marcar todos los correos no leídos como leídos
def mark_all_unread_as_read():
    query = "is:unread"
    unread_messages = []
    page_token = None

    # Obtener todos los mensajes no leídos
    while True:
        response = service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
        messages = response.get('messages', [])
        
        if not messages:
            print("No hay más correos no leídos.")
            break

        unread_messages.extend(messages)
        page_token = response.get('nextPageToken')

        if not page_token:
            break

    print(f"Total de mensajes no leídos: {len(unread_messages)}")

    # Marcar cada mensaje como leído
    for msg in unread_messages:
        msg_id = msg['id']
        service.users().messages().modify(userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
        print(f"Mensaje {msg_id} marcado como leído.")

mark_all_unread_as_read()

  
