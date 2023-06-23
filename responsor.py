#!usr/bin/python3

# [desc]: displays response codes of websites in given list
# [dev] : A Divinemonk creation!

import requests as r
import sys

print("\n \33[7;90;97m [ R3SP0NS0R ] (ctrl-z to exit) \033[0m\n")

try:
	with open (sys.argv[1], 'r') as urls:
		# url should we without `http://` or `https://`
		url = urls.read().split('\n')

		# requesting each url and displays their response code
		for u in url:
			try:
				status_code = r.get('https://'+u, timeout=10).status_code
			except:
				continue
			if status_code == 200:
				print ('\33[1;49;92m   [',status_code, ']:',u)
			elif status_code == 403:
				print ('\33[1;49;93m   [',status_code, ']:',u)
			else:
				print ('\33[1;49;91m   [',status_code, ']:',u)

	# scan complete message
	print ('\n \033[0m\33[7;90;97m [ Aye aye, happy hacking captain :) ] \033[0m\n')

# handling errors
except IndexError:
	print (' [!] File name missing\n [i] usage: \'python responsor.py URL_LIST.txt\'\n')
except FileNotFoundError:
	print (f' [!] File \'{sys.argv[1]}\' not found\n')
