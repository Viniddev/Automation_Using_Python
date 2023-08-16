from imbox import Imbox
from datetime import datetime
import pandas as pd

username = "diasvinicius95@gmail.com"
password = open("pass", "r").read()
host = "imap.gmail.com"

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages(unread = True)

for (uid, message) in messages:
    #copiaremos os arquivos em anexo para uma pasta
    if len(message.attachments) > 0:
        for attach in message.attachments:
            file = open("attachments/report.pdf", "wb")
            file.write(attach["content"].read())
            file.close()