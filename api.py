import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define el ámbito (scope) necesario para acceder a Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None
    # El archivo token.pickle almacena los tokens de acceso y actualización del usuario.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no existen credenciales válidas, solicita al usuario que inicie sesión.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima ejecución.
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def mark_unread_emails_as_read(service):
    try:
        # Busca todos los correos no leídos
        results = service.users().messages().list(userId='me', q="is:unread").execute()
        messages = results.get('messages', [])

        if not messages:
            print("No hay correos no leídos.")
            return

        for message in messages:
            # Marcar cada mensaje como leído
            service.users().messages().modify(
                userId='me', id=message['id'],
                body={'removeLabelIds': ['UNREAD']}
            ).execute()

        print(f"{len(messages)} correos no leídos se han marcado como leídos.")
    except Exception as e:
        print(f"Error al marcar los correos como leídos: {e}")

def main():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    mark_unread_emails_as_read(service)

if __name__ == '__main__':
    main()
