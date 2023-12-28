# --------------------------------------------------------------#
#               ! FOR EDUCATION PURPOSES ONLY !
# MORE Information HERE --> https://github.com/Fattcat/Ulti-Fi
#           Created for automate penetration testing
# ------------------------------------------------------------- #

# ------ [ Moduly ] ------ #
import os
import time
import random
import subprocess
import platform
# ------ [ My  Modules ] ------ #
from SRC import DoNKModule
from SRC import CaptureHandShake
from SRC import Deauth
# ------ [ My  Modules ] ------ #


# Farbicky
reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
orange = '\033[31m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'

ColorList = [red, green, blue, orange, magenta, yellow, cyan]

os.system("clear")
time.sleep(0.1)

# ----- Print LOGO ----- #
Logo = DoNKModule.ll
print(red, Logo, reset)
time.sleep(0.1)
# ----- Print LOGO ----- #


# Check OS
os_info = platform.system()
print("-"*23)
print(f"- {magenta}Detected : {os_info} OS{reset} -")
print("-"*23)

if os_info =="Linux": 
    # Clear terminal
    # os.system("clear")
    time.sleep(0.2)
else:
    print(f"{yellow}Detected : {red} {os_info} OS{reset}")
    print(f"{red}Aborting ...{reset} CUZ OS IS NOT LINUX\nNO SUPPORT FOR SCRIPTS :/")

    # -------------------------------------------------------- #
    # Spravit triedu alebo func v "DoNKModul" pre SWAG vyhodenie
    vyhodenie = DoNKModul.Vyhadzovak
    print(vyhodenie)
    # -------------------------------------------------------- #


# --------------------------------------------------------------
# SEM Check Mon mode ci je zapnuty na nejakom wlan WIFI adaptery
# --------------------------------------------------------------


# --------------------------------
# ------- Vypisanie Menu ---------
Menu = DoNKModule.MainMenu
RanColor = random.choice(ColorList)
print(RanColor, Menu, reset)
# --------------------------------

UserInput = input(f"{yellow}Pick number --> {reset}")

if UserInput =="1":
    pass
#spušta iba testovaci prikaz len tak :D
# lol = subprocess.run(["iwconfig"], capture_output=True, text=False)
# print(lol)

# AdapterChoice = input("Select WiFi Adapter for USE : ")
# print("Starting monitor mode on", AdapterChoice)
# time.sleep(1)


# -------- PRIKAZ PRE SPUSTENIE MON MODU ------- #
# CommandForMonModeON = "sudo airmon-ng start"
# MonModeON = subprocess.run([CommandForMonModeON, AdapterChoice], capture_output=True, text=True)
# print(MonModeON)
# -------------------- SEM --------------------- #

time.sleep(1)
print("Spustanie prikazu ")
#subprocess.run([""])

