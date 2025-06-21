from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from financeiro.models.fornecedor import Fornecedor
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


@shared_task
def enviar_email(destinatario, mensagem):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("thomazxaavier@gmail0.com")
    to_email = To("thomazx4v13r@gmail.com")
    subject = "Hello World"
    content =  Content("text/plain", "Testando a porra do sendgrid")
    mail = Mail(from_email, to_email, subject, content)

    mail_json = mail.get()

    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
