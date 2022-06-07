def B1T1X(Amount_Of_Addresses, filenumber):
    import shutil
    import os
    import secrets
    from random import randint
    from static.logogen import ui
    w = os.get_terminal_size().columns
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    ui("BITIX")
    GenStat = 0
    filenumber = str(filenumber)
    while (GenStat != Amount_Of_Addresses):
        GenStat = GenStat + 1
        genstat2 = str(GenStat)
        bits = secrets.randbits(256)
        bits_hex = hex(bits)
        private_key = bits_hex[2:]
        filename = f"GeneratedAddresses-{filenumber}.txt"
        file = open(filename, "a")
        file.write(f"{private_key}\n")
        file.close()
        print(f"[{genstat2}]Wrote {private_key} to {filename}".center(w))
    clear()
    ui("BITIX")
    print(f"All private keys saved to {filename}")
    l = input("Please Press Enter To Close")
