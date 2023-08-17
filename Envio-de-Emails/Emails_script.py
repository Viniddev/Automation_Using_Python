from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open("pass", "r").read()

email_origem = "diasvinicius95@gmail.com"
email_destino = ("diasvinicius95@outlook.com")

assunto = "Testando envio automático"
body = open("email.txt", "r").read()

mensagem = EmailMessage()

mensagem["From"] = email_origem
mensagem["To"] = email_destino
mensagem["Subject"] = assunto

mensagem.set_content(body, subtype="html")
safe = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())