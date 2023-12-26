# ---------------------------------------------
# ! FOR EDUCATION PURPOSES ONLY !
# MORE Information HERE --> https://github.com/Fattcat/Ulti-Fi
# Created for automate penetration testing
# ---------------------------------------------
# Moduly
import os
import time
import subprocess
import platform

# Farbicky
reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
orange = '\033[33m   #\033[31m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'

# Clear terminal
os.system("clear")

CheckOS = platform.platform()
print(CheckOS)
if "linux" in CheckOS:
    print("Detected Linux OS\nStarting ...")
else:
    print("! Other OS!\nAborting script!")
os.system("iwconfig")
AdapterChoice = input("Select WiFi Adapter for USE : ")
print("Starting monitor mode on", AdapterChoice)
time.sleep(1)
subprocess.run(['sudo', 'airmon-ng', 'start', AdapterChoice], check=True, shell=False)
time.sleep(1)
subprocess.run([""])
