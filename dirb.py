print("-------------------------------------")
print("||||||||||| edited dxnboy |||||||||||")
print("-------------------------------------")

import requests 
import sys 

#"wordlist.txt" must be in the same dir that pyDirb.py
sub_list = open("wordlist.txt").read() 
directories = sub_list.splitlines()
target_url = input("Target <https://google.com/>: ")

for dir in directories:
    #Change the URL.
    dir_enum = target_url + dir
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Directory:" ,dir_enum)
