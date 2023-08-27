import requests
from send_email import send_user_email
import os
from dotenv import load_dotenv

load_dotenv()


topic = "tesla"
api_key = os.getenv("PASSWORD")

url = ("https://newsapi.org/v2/everything?"\
       f"q={topic}&from=2023-07-26&"\
       "sortBy=publishedAt&"\
       f"apiKey={api_key}&language=en")

response = requests.get(url)
response = response.json()

articles = response["articles"]

message = ""

for article in articles[:20]:
    message = message + '\n' + article["title"] + '\n' + article["description"]  + '\n' + article["url"] + 2*'\n'

message = f"""\
Subject : Daily news digest from Polo's python script
    
Hey, here is today's news from {topic}
{message}
"""
message = message.encode('utf-8')
send_user_email(message)
print("Email sent successfully")

