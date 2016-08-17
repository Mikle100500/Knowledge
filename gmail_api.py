import base64
from email.mime.text import MIMEText


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string())}


create_message('forTestingJohnTester@gmail.com', 'forTestingJohnTester@gmail.com', 'text', 'text test')