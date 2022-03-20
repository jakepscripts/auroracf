import time, ctypes, threading, random, traceback, sys, datetime, json, os, subprocess, requests
from os import system, name
import colorama
from colorama import Fore, init, Back, Style

init(convert=True)
colorama.init()
print('''
   ___   _   _   ___    ___    ___    ___             ___   ___    ___  __  __   ___   _____  _____   ___    ___   
  /   \ | | | | | _ \  / _ \  | _ \  /   \    o O O  | __| / _ \  | _ \|  \/  | /   \ |_   _||_   _| | __|  | _ \  
  | - | | |_| | |   / | (_) | |   /  | - |   o       | _| | (_) | |   /| |\/| | | - |   | |    | |   | _|   |   /  
  |_|_|  \___/  |_|_\  \___/  |_|_\  |_|_|  TS__[O] _|_|_  \___/  |_|_\|_|__|_| |_|_|  _|_|_  _|_|_  |___|  |_|_\  
_|"""""_|"""""_|"""""_|"""""_|"""""_|"""""|{======_| """ _|"""""_|"""""_|"""""_|"""""_|"""""_|"""""_|"""""_|"""""| 
"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-' 
''')

print("\n                 [AuroraCF] by jakep#0001 | purchase aurora at https://www.auroratools.shop/")
ctypes.windll.kernel32.SetConsoleTitleW(f"AURORACF | PURCHASE AURORA AT https://www.auroratools.shop/")

print(Style.RESET_ALL)



s = '''
                      #############################################################
                      #                                                           #
                      #                 [1] -> Cookie Formatter                   #
                      #                                                           #
                      #############################################################

'''
s.center(40)

print(s)



try:
    option = int(input('\n[AuroraCF] -> Select Option: ')) 
except:
    print(Fore.RED + "[AuroraCF] -> Invalid Option")
    time.sleep(30)
    sys.exit()
 





def cls():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')





if option == 1:
   
  

  
    cls()

    input = 'cookies.txt'
    output = 'bin/output.txt'


    cls()
    print('[AuroraCF] -> formatting.')

    cookiesfile = open('cookies.txt','r').read().splitlines()
    cookies = [cookie.split('|_',1)[1] for cookie in cookiesfile]

    cls()
    print('[AuroraCF] -> formatting..')

    with open("bin/output.txt", "w") as outfile:
        outfile.write("\n".join(cookies))

    cls()
    print('[AuroraCF] -> formatting...') 
    cls()

    print(Fore.LIGHTGREEN_EX + '[AuroraCF] -> Successfully Formated (saved to bin/output.txt)')
    time.sleep(3)
    cls()
