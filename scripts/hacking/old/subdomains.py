#!/usr/bin/env python3

import requests


def request(url):
    try:
        print(f"https://{url}")
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input("[*] Enter Target URL: ")

file_name = input("[*] Enter File To Use: ")

file = open(file_name, "r")
for line in file:
    word = line.strip()
    full_url = word + "." + target_url
    response = request(full_url)
    if response:
        print(f"[+] Discovered Subdomain At This Link: {full_url}")
    
