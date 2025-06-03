import os
from dotenv import load_dotenv  # type:ignore
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

load_dotenv()
PATH_HTML = pathlib.Path(__file__).parent / 'aula303.html'

# dados do remetente
remetente = os.getenv('EMAIL_USER', '')
destinatario = remetente
password = os.getenv('EMAIL_PASSWORS', '')

# configurações SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = remetente
smtp_password = password

with open(PATH_HTML, 'r', encoding='utf8') as file:
    reader_ = file.read()
    template = Template(reader_)
    email_text = template.substitute(nome='Thiago')

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do Email'

corpo_email = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Enviado com sucesso')
