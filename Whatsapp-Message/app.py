import pywhatkit
import keyboard
import time
from datetime import datetime

contats = ["seus contatos aqui!"]

while len(contats) >= 1:
    pywhatkit.sendwhatmsg(contats[0], 
                          'Olá! Essa mensagem foi enviada por um script Python.', 
                          datetime.now().hour, datetime.now().minute + 1)
    del contats[0]
    time.sleep(15)
    keyboard.press_and_release("ctrl+w")

    