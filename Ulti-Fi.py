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
import sys
# ------ [ My  Modules ] ------ #
from SRC import DoNKModule
from SRC import CaptureHandShake
from SRC import Deauth
# ------ [ My  Modules ] ------ #

# ------ [ Farbicky ] ------ #
red = '\033[91m'
orange = '\033[38;5;208m'
purple = '\033[95m'
green = '\033[92m'
blue = '\033[94m'
magenta = '\033[35m'
yellow = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'

# ------ [RanomPickColor ] ------ #
ColorList = [red, green, blue, orange, magenta, yellow, cyan]

os.system("clear")
time.sleep(0.1)

# ----- Print LOGO ----- #
Logo = DoNKModule.ll
print(orange, Logo, reset)
time.sleep(0.1)
print("------"* 10)
print(f"{blue}Author : {green}Fattcat - Dominik Hulin{reset}")
print(f"{blue}GitHub : {green}https://github.com/Fattcat{reset}")
# ----- Print LOGO ----- #


# ------ CHECK IF SCRIPT WAS STARTED WITH SUDO ------ #
if os.geteuid() != 0:
   print(f"      {red}!{reset} ------ {red}[ CANT CONTINUE ]{reset} ------ {red}!{reset}")
   print(f"{red}! Script was NOT STARTED WITH SUDO PERMISSIONS !{reset}")
   print(f"Please Start Script with following: {green}sudo python3 Ulti-Fi.py{reset}\n")
   sys.exit(1)

# Check OS
os_info = platform.system()
print(" "*8 + "-"*23)
print(" "*8 + f"- {magenta}Detected : {os_info} OS{reset} -")
print(" "*8 + "-"*23)

if os_info =="Linux":
    # Clear terminal
    # os.system("clear")
    time.sleep(0.2)
else:
    print(f"{yellow}Detected : {red} {os_info} OS{reset}")
    print(f"{red}Aborting ...{reset} CUZ OS IS NOT LINUX\nNO SUPPORT FOR SCRIPTS :/")

    # -------------------------------------------------------- #
    # Spravit triedu alebo func v "DoNKModul" pre SWAG vyhodenie
    vyhodenie = DoNKModule.Vyhadzovak
    print(vyhodenie)
    exit()
    # -------------------------------------------------------- #


# --------------------------------------------------------------
# SEM Check Mon mode ci je zapnuty na nejakom wlan WIFI adaptery
# --------------------------------------------------------------

#while True:
# ------- Vypisanie Menu --------- #
Menu = DoNKModule.MainMenu
RanColor = random.choice(ColorList)
print(Menu)
# -------------------------------- #

    
UserInput = input(f"{yellow}Pick number --> {reset}")

if UserInput =="1":
    print(" "*13 + "_"*8)
    print("-"*12 + " [ INFO ] " + "-"*12)
    print(f"{green}Enabling{reset} {orange}Monitor Mode{reset} on '{cyan}wlan1{reset}' ...")
    print("-"*30)
    time.sleep(1)

    subprocess.run(["sudo", "airmon-ng", "check", "kill"], capture_output=True)
    time.sleep(2)
    subprocess.run(["sudo", "airmon-ng", "start", "wlan1"], capture_output=True)
    time.sleep(2)

    process = subprocess.run(["iwconfig"], capture_output=True)
    output = process.stdout.decode("utf-8")

    if "wlan1" in output and "Mode:Monitor" in output:
        print(f"{orange}STATUS{reset} : Monitor mode {green}ENABLED{reset}")
# ------ TOTO else tu hadzalo stale chybu aj ked bol Mon Mode ENABLED na wlan1 ------ #
# ------ Tak som to nechal ZAKOMENTOVANE az to nehadze CHYBU stale ------ #
    else:
        print("Something went WRONG with Turning Monitor Mode ON :/")


elif UserInput =="2":
    DeauthIt = Deauth.main()

elif UserInput =="3":
    CATCHShake = CaptureHandShake.ShakeIt()

elif UserInput == "4":
    try:
        subprocess.Popen(["gnome-terminal", "--", "--geometry", "800x600+0+0", "--", "cd ET && python3 main.py"])
    except KeyboardInterrupt:
        print("CTRL-C bol stlačený v hlavnom skripte.")

elif UserInput =="5":
    PomocnePrikazy = DoNKModule.Help
    print(PomocnePrikazy)

elif UserInput =="6":
    vyhodenie = DoNKModule.Vyhadzovak
    print(vyhodenie)
    exit()

elif UserInput =="ET":
   print(f"{green}Čendžing dajrektorii{reset}...")
   # Spustenie nového terminálu aj s rozmermi terminálu a prepnutie pracovného adresára na "ET"
   subprocess.Popen(["gnome-terminal", "--geometry", "800x600+0+0", "--", "cd ET && python3 main.py"])


