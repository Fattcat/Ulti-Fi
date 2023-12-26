# --------------------------------------------------------------#
#               ! FOR EDUCATION PURPOSES ONLY !
# MORE Information HERE --> https://github.com/Fattcat/Ulti-Fi
#           Created for automate penetration testing
# ------------------------------------------------------------- #

# Moduly
import os
import time
import subprocess
import platform
from SRC import DoNK-Menu

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
time.sleep(1)

# ------------------------
#TU SPRAVIT LEPSI CHECK OS
# ------------------------

def check_monitor_mode():
    # Spustí príkaz iwconfig a zachytí výstup ze neho musim nastavit text=False az to nepise vsetko
    result = subprocess.run(["iwconfig"], capture_output=True, text=True)

    # Získa výstupné riadky z teho
    output_lines = result.stdout.split('\n')

    # Prejde cez riadky a vyhľada informácie o tom monitor móde
    for line in output_lines:
        if "Mode:Monitor" in line:
            # Extrahujte názov wifi adaptéra
            adapter_name = line.split()[0]
            
            # Vypíše informáciu o zapnutom monitor móde
            print(f"Monitor mód je už zapnutý na: {adapter_name}")
        else:
          print("Monitor mod este neni zapnuty")
# Spust funkciu pre kontrolu monitor módu
print("Checking if Monitor Mode is Turned ON ...\n")
check_monitor_mode()

#spušta iba testovaci prikaz len tak :D
os.system("iwconfig")
AdapterChoice = input("Select WiFi Adapter for USE : ")
print("Starting monitor mode on", AdapterChoice)
time.sleep(1)
CommandForMonModeON = "sudo airmon-ng start"
subprocess.run([CommandForMonModeON, AdapterChoice], check=True, text=False, shell=False)
time.sleep(1)
subprocess.run([""])
