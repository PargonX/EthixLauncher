def login():
    from hashlib import sha256
    from multiprocessing import AuthenticationError
    import time
    import os
    import shutil
    from hashlib import sha256
    import winreg
    from wmi import WMI
    from sys import platform
    import requests
    import json
    from collections import namedtuple
    from json import JSONEncoder
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
    def calculateHash(secret, key):
        u_timestamp = round(time.time() / 200) * 200
        program_secret = secret
        auth_key = key
        hwid = calculateHWID()
    
        str = f"{program_secret}{auth_key}{hwid}{u_timestamp}"
        return sha256(str.encode('utf-8')).hexdigest().upper()


    Auth_Key = input("Enter Nulled Auth Key: ")
    HWID = calculateHWID()
    URL = "https://www.nulled.to/authkeys.php"
    Headers = {
        "register":"1",
        "key":Auth_Key,
        "hwid":HWID,
        "program_id":"36"
        }
    def ConvertJSON(studentDict):
        return namedtuple('X', studentDict.keys())(*studentDict.values())
    response = requests.post(URL, data=Headers).text
    Response_Table = json.loads(response, object_hook=ConvertJSON)
    if Response_Table.data.message == "Succesfully registered":
        pass
    elif Response_Table.data.message == "Duplicate registry":
        pass
    elif Response_Table.data.message == "Invalid Auth Key":
        print("Error: 1")
        print(Response_Table.data.message)
        input("Press Enter To Exit")
        exit()
    Headers = {
        "validate":"1",
        "key":Auth_Key,
        "hwid":HWID,
        "program_id":"36"
        }
    response2 = requests.post(URL, data=Headers).text
    Response_Table2 = json.loads(response2, object_hook=ConvertJSON)
    if Response_Table2.status != False:
        if Response_Table2.data.groups[0] >= "7":
            Username = Response_Table2.data.name
            print(f"Welcome {Username}")
        else:
            print("We are sorry you are not VIP+ Rank")
            input("Press Enter To Exit")
            exit()
    else:
        print("Error: 2")
        print(Response_Table2.data.message)
        if Response_Table2.data.message == "Unknown error #722":
            print("invalid hwid")
        input("Press enter to exit")
        exit()
                