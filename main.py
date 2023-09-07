import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Set up the Gmail API service
creds = Credentials.from_authorized_user_file('sec.json')  # Replace with your token file path
service = build('gmail', 'v1', credentials=creds)

# Create an email message
message = {
    'raw': base64.urlsafe_b64encode(b'From: agrawalbabli17@gmail.com\nTo: chetanyaagrawal@gmail.com\nSubject: Subject Text\n\nBody Text').decode('utf-8')
}
print(message)
# Send the email
try:
    message = service.users().messages().send(userId='me', body=message).execute()
    print('Message sent: %s' % message['id'])
except Exception as e:
    print('An error occurred: %s' % e)
