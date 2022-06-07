import os
from colorama import init, Fore
import time
from random import randint
import requests
import shutil
from hashlib import sha256
import winreg
from wmi import WMI
from sys import platform
 
def get_guid():
    Registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    RawKey = winreg.OpenKey(Registry, "SOFTWARE\Microsoft\Cryptography")
    return winreg.QueryValueEx(RawKey, "MachineGuid")[0].upper()
 
def get_device_uuid():
    if platform == "linux" or platform == "linux2":
        return ""
        # linux
    elif platform == "darwin":
        return ""
        # OS X
    elif platform == "win32":
        return WMI().Win32_ComputerSystemProduct()[0].UUID
 
def calculateHWID():    
    c_name = os.environ.get("COMPUTERNAME")
    u_name = os.getlogin()
    p_rev = os.environ.get("PROCESSOR_REVISION")
    disk = shutil.disk_usage("/").total
    uuid = get_device_uuid()
    guid = get_guid()
 
    str = f"{c_name}{u_name}{p_rev}{disk}{uuid}{guid}"
    return sha256(str.encode('utf-8')).hexdigest().upper()
width = os.get_terminal_size().columns
def clear():#defines the console clear function
    os.system('cls' if os.name == 'nt' else 'clear')
def CreateSessionID(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)
