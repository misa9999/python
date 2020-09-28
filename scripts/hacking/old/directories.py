#!/usr/bin/env python3

import requests


def request(url):
    try:
        print(f"https://{url}")
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input("[*] Enter Target URL: ")

file = open("wordlist/wordlist_top_500PswMangled.txt", "r")
for line in file:
    word = line.strip()
    full_url = target_url + "/" + word
    response = request(full_url)
    if response:
        print(f"[+] Discovered Directory At This Link: {full_url}")
    
