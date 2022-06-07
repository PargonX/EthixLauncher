from static.vari import clear
from colorama import init, Fore
import requests
from bs4 import BeautifulSoup
import hashlib
import base58
import codecs
import ecdsa
import os
import shutil
import secrets
from random import randint
from threading import Thread
import ctypes
from static.logogen import ui
def DR4GG(file_number, threadcount):
    clear()
    ui("DRAGG")
    checked = 0
    def checker():
        while 1:
            try:
                bits = secrets.randbits(256)
                bits_hex = hex(bits)
                private_key = bits_hex[2:]
                private_key_bytes = codecs.decode(private_key, 'hex')
                public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
                public_key_bytes = public_key_raw.to_string()
                public_key_hex = codecs.encode(public_key_bytes, 'hex')
                public_key = (b'04' + public_key_hex).decode("utf-8")
                if (ord(bytearray.fromhex(public_key[-2:])) % 2 == 0):
                    public_key_compressed = '02'
                else:
                    public_key_compressed = '03'
                public_key_compressed += public_key[2:66]
                hex_str = bytearray.fromhex(public_key_compressed)
                sha = hashlib.sha256()
                sha.update(hex_str)
                sha.hexdigest()
                rip = hashlib.new('ripemd160')
                rip.update(sha.digest())
                key_hash = rip.hexdigest()
                modified_key_hash = "00" + key_hash
                sha = hashlib.sha256()
                hex_str = bytearray.fromhex(modified_key_hash)
                sha.update(hex_str)
                sha_2 = hashlib.sha256()
                sha_2.update(sha.digest())
                checksum = sha_2.hexdigest()[:8]
                byte_25_address = modified_key_hash + checksum
                address = base58.b58encode(bytes(bytearray.fromhex(byte_25_address))).decode('utf-8')
                URL = (f'https://bitcoin.atomicwallet.io/address/{address}')
                markup = "<h1></h1>"
                headers = {
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537'}
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                small = soup.find("small", {"class": 'text-muted'}).get_text()
                balance = str(small)[:2]
                balance = int(balance)
                balance_display = str(balance)
                display_string = f"{private_key}:{address} => {balance_display} BTC"
                if balance == 0:
                    print(f"{Fore.RED}[-] {display_string}")
                elif balance != 0:
                    print(f"{Fore.GREEN}[+] {display_string}")
                    file = open(f"DR4GG-{file_number}.txt", "a")
                    file.write(f"{display_string}\n")
                    file.close()
            except:
                pass
    activethreads = 0
    while activethreads < threadcount:
        t = Thread(target=checker)
        t.start()