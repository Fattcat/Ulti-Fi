# CrackHandShake File going to be here :D

import os

# Path to captured handshake file
captured_handshake = "capturedShake.cap"

# Path to rockyou.txt
rockyou_path = "/home/kali/Desktop/rockyou.txt"

# Aircrack-ng command to crack the handshake
aircrack_command = f"aircrack-ng -w {rockyou_path} {captured_handshake}"

# Execute the aircrack-ng command
os.system(aircrack_command)

# Check if the process is still in progress
if os.system(aircrack_command) == 0:
    print("Still in process...")
else:
    print("Successfully completed")
    # Extract and print the cracked password
    with open("key.txt", "r") as key_file:
        password = key_file.read().strip()
        print(f"Password is: {password}")
