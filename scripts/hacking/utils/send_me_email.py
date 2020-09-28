import smtplib

# server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("ftime2882@gmail.com", "ftime000ftime")
server.sendmail("ftime2882@gmail.com", "ftime2882@gmail.com", "outputs haha")
server.quit()


"""
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")
message = """
"""
Subject: Hi there

This message is sent from Python.

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
"""