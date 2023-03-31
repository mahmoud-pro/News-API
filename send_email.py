import os
import smtplib
import ssl

from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values('.env')
email = os.getenv("EMAIL")
password = os.getenv("PASS")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    email_sender = email
    pass_sender = password

    receiver = email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email_sender, pass_sender)
        server.sendmail(email_sender, receiver, message)
