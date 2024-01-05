# ----------------- [ Colors ] ------------------ #
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
orange = '\033[31m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'
# ------------- [ End of Colors ] --------------- #


# -------------- [ Start of Logo ] -------------- #

ll = ("""
                   ------------------------
                   [  --> WELCOME TO <--  ]
                   ------------------------
           __    __________________    __________________
  |\     /|( \   \__   __/\__   __/    (  ____ |\__   __/
  | )   ( || (      ) (      ) (       | (    \/   ) (   
  | |   | || |      | |      | | _____ | (__       | |   
  | |   | || |      | |      | |(_____)|  __)      | |   
  | |   | || |      | |      | |       | (         | |   
  | (___) || (____/\| |   ___) (___    | )      ___) (___
  (_______)(_______/)_(   \_______/    |/       \_______/""")
# --------------- [ End of Logo ] --------------- #

MainMenu = f"""
    ---------------------------------------------------------------------------------
    ---- {green}[ Main Menu ]{reset} ---------------------------- {green}[ Small Help ]{reset} ------------------
    ---------------------------------------------------------------------------------

    [1] Start monitor mode                    - {green}Enable Monitor Mode{reset} on '{magenta}wlan1{reset}'
    [2] Start Deauth Attack                   - {green}For{reset} {red}DISCONNECT USERS{reset} on target WiFi
    [3] Capture WiFi HandShake                - {green}Catch HandShake to File{reset}
    [4] Crack HandShake File                  - {green}Crack with some wordlist{reset}
    [5] -h or help                            - {green}display usage with command{reset}
    [{red}6{reset}] {red}EXIT{reset}                                  - {red}Stop and EXIT{reset}
"""

Help = f"""
     ---------------------------
     ----{green}[ Commands & help ]{reset}----
     ---------------------------

1. Start monitor mode
             ---[ INFO ] ---
- Command for start Monior Mode on specific WiFi Adapter
   - Example --> wlan0 or wlan1 (or if you have wlan1mon)

2. Start Deauth Attack
             ---[ INFO ] ---
- Command for start deauth attack on correct WiFi SSID
- will be added
"""


Vyhadzovak = (f"""
--------------------------------------------------------------
{yellow}`########::'##:::'##:'########:'########::'##:::'##:'########:
 ##.... ##:. ##:'##:: ##.....:: ##.... ##:. ##:'##:: ##.....::
 ##:::: ##::. ####::: ##::::::: ##:::: ##::. ####::: ##:::::::
 ########::::. ##:::: ######::: ########::::. ##:::: ######:::
 ##.... ##:::: ##:::: ##...:::: ##.... ##:::: ##:::: ##...::::
 ##:::: ##:::: ##:::: ##::::::: ##:::: ##:::: ##:::: ##:::::::
 ########::::: ##:::: ########: ########::::: ##:::: ########:
........::::::..:::::........::........::::::..:::::........::{reset}
--------------------------------------------------------------
         -> KALI LINUX - Best Linux OS for Haking <-         """)


