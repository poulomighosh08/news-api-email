import smtplib, ssl
import os
from dotenv import load_dotenv

def send_user_email(message):
    load_dotenv()
    host = "smtp.gmail.com"
    receiver = "ghosh.poulomisweet@gmail.com"
    sender="ghosh.poulomisweet@gmail.com"
    password = os.getenv("PASSWORD")
    port=465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


