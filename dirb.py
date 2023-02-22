#!/user/bin/python3
#scans for web directories from a word list
#replace common.txt with your wordlist
#for python 3

import requests

def requests(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = input("Enter Target URL: ")

file = open("common.txt","r")
for line in file:
    word = line.strip()
    full_url = target_url + "/" + word
    response = request(full_url)
    if response:
        print("Discovered directory at this link: " + full_url)
