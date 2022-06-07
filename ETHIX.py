from static.vari import clear, CreateSessionID
from static.login import login
from colorama import init, Fore
from nulled_auth import auth
from static.logogen import ui
import os
import time
width = os.get_terminal_size().columns
ui("ETHIX")
print("Welcome to ETH1X AIO".center(width))
print("Based on Pargonix Launcher".center(width))
print("Dedicated To Nulled".center(width))
print("Please Join The Discord If You Do Not Have Premium: https://discord.gg/S9Fq6bTYka".center(width))
input(f"{Fore.BLUE}Press Enter To Continue".center(width))
clear()
ui("ETHIX")
login()
SessionID = CreateSessionID(5)
print(f"Session ID created {SessionID}, this will be used on the files from outputs")
input("Press Enter To Continue")
clear()
ui("ETHIX")
print("Created By PargonX".center(width))
print(f"{Fore.YELLOW}[1]B1T1X [2]DR4GG [3]W1NG2".center(width))
print(f"{Fore.YELLOW}[4]CR345".center(width))
#print(f"{Fore.YELLOW}[4]PURG3 [5]CR4FT [4]SP0TX".center(width))
#print(f"{Fore.YELLOW}[7]OXYV2)
Selected_Module = input("#/INFO:")
if Selected_Module == "INFO":
    print("B1T1X = Bitcoin Private Key Generator")
    print("DR4GG = Bitcoin Private Key Generator + Balance Checker")
    print("W1NG2 = Buffalo Wild Wings Checker")
    #print("PURG3 = Ethereum Private Key Generator + Balance Checker")\
    #print("CR4FT = MinecratPY | Minecraft Checker)
    print("CR345 = Spotify[SELENIUM] Account Checker")
    #print("OXYV2 = OxygenX | Upgraded | Authorized by ShadowOxygen)
    input("Press Enter To Close")
else:
    Selected_Module = int(Selected_Module)
if Selected_Module == 1:
    from configs.B1T1X import B1T1X
    print("Setup:")
    WalletCount = int(input("How many private keys: "))
    print(f"{Fore.GREEN}Press Enter To Start B1T1X")
    input()
    B1T1X(WalletCount, SessionID)
elif Selected_Module == 2:
    from configs.DR4GG import DR4GG
    threads = int(input("Threads: "))
    DR4GG(SessionID, threads)
elif Selected_Module == 3:
    from configs.W1NG2 import W1NG2
    combolist = input("Please drag your combos into this window: ")
    combolist = open(combolist, "r").readlines()
    threadsset == False
    while threadsset == False:
        threadcount = int(input("Threads[Limit 50]: "))
        if threadcount <= 50:
            threadsset = True
    W1NG2(combolist, SessionID, threadcount)
elif Selected_Module == 4:
    from configs.CR345 import CR345
    input("Please make sure your combos are in combos.txt, then press ENTER")
    CR345(threads)