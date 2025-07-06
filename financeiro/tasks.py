from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from financeiro.models.fornecedor import Fornecedor
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


load_dotenv()

@shared_task
def enviar_email(destinatario, assunto, mensagem):
    message = Mail(
        from_email='thomazxaavier@gmail.com',
        to_emails=destinatario,
        subject=assunto,
        html_content=mensagem)
    try:
        api_key = os.environ.get('SENDGRID_API_KEY')
        if not api_key:
            raise ValueError("SENDGRID_API_KEY não está definido no ambiente")
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)