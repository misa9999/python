from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib, ssl

my_email = "my_email@gmail.com"
my_passwd = "password"

with open("template.html", "r") as html:
    template = Template(html.read())
    date = datetime.now().strftime("%d/%m/%Y")
    message_body = template.safe_substitute(name="Misa", date=date)


msg = MIMEMultipart()
msg["from"] = "Yuuki"
msg["to"] = my_email
msg["subject"] = "Attention this is a test email"


body = MIMEText(message_body, "html")
msg.attach(body)

with open("a1.jpg", "rb") as img:
    img = MIMEImage(img.read())
    msg.attach(img)

port = 587
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    try:
        server.ehlo()
        server.starttls(context=context)
        server.login(my_email, my_passwd)
        server.send_message(msg)
        print("Success")
    except Exception as e:
        print("Error:", e)
