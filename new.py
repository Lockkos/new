from colorama import Fore
import time
import sys
import random
import os
import string
import subprocess, requests
from getpass import getpass
import secrets
from random import randint
 
from getpass import getpass
username = input('Enter Username: ')
password = getpass('Enter Password: ')



os.system("cls")
wallet = input(Fore.RED + "Wallet: ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
print("Wallet found")

time.sleep(0.2)

print(Fore.CYAN + '88     88  dP""b8 88  88 888888' )   
print(Fore.CYAN + '88     88 dP   `" 88  88   88' )       
print(Fore.CYAN + '88  .o 88 Yb  "88 888888   88' )       
print(Fore.CYAN + '88ood8 88  YboodP 88  88   88' ) 

print(Fore.WHITE +' ====================================================') 
print(Fore.WHITE +'             Welcome to LightMiner Premium          =') 
print(Fore.WHITE +'                @2022   LIGHTMINER v1               =') 
print(Fore.WHITE +'                                                    =') 
print(Fore.WHITE +' ====================================================')

time.sleep(3)

print(Fore.WHITE +"Connecting...")
time.sleep(2)

print(Fore.GREEN + 'Successfully connected')
time.sleep(1)
print(Fore.WHITE +'Enter your product key (:EXAMPLE=KEY')

LicenseKey = input(Fore.RED + 'Input License Key: ')
if LicenseKey == "123":
    print(Fore.GREEN + "Key is Valid!")
    time.sleep(0.5)
else:
    print(Fore.RED + "Invalid Key!")
    print(Fore.RED + "Press Enter to quit!")
    input("")
    exit(123)

print(Fore.WHITE +" installing...")
time.sleep(3)
print(Fore.GREEN +"Success")
time.sleep(3)

continuing = True
 
btcval = 31643.79
 
while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0,2500)
    if ranInt <= 1:
      randomBTC = randint(1,100)/100
      print(Fore.BLUE + "[-] ╚═══► 0x" + secrets.token_hex(20) + Fore.GREEN + " ╚═══► " + str(randomBTC) + " BTC ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      answer = input("> Would you like to continue? (Y/N) ")
      if answer.lower() == "y":
        continuing = True
      else:
        continuing = False
    else:
      print(f''' {Fore.WHITE}[LightMiner] {Fore.CYAN}|BTC| bx''' + secrets.token_hex(20) + ''' 0.00 |BAL| ($0.000)''')
