import os
import platform
from dotenv import load_dotenv
from logger import logger

##########################################################################################################
# ENVs :                                                                                                 #
#    PLATFORM -> for subprocess commands / binary paths                                                  #
#    CHROME_BINARY_PATH   -> is set by the default paths in [unix | windows } /  can be changed in .env  #
# -> also the default is set for 64-bit systems                                                          #
#   in .env file :                                                                                       #
#   WIFI_SSID="WIFI-Name"                                                                                #
#   WIFI_PASSWORD="WIFI-Password"  -> if wifi needs authentication at some point                         #
#                                                                                                        #
#    LOGIN_IP=""   -> Login page                                                                         #
#    LOGIN_USERNAME=""                                                                                   #
#    LOGIN_PASSWORD=""                                                                                   #
#    LOGIN_USERNAME_XPATH=""   # I'm using XPATHS to find the elements in selenium.                      #
#    LOGIN_PASSWORD_XPATH=""                                                                             #
#    LOGIN_SUBMIT_XPATH=""                                                                               #
##########################################################################################################

# Setup platform dependant ENVS
def set_platform_env() -> None:
    current_platform = platform.system().lower()
    if "windows" in current_platform:
        os.environ["PLATFORM"] = "windows"
        os.environ["CHROME_BINARY_PATH"] = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    elif "linux" in current_platform:
        os.environ["PLATFORM"] = "linux"
        os.environ["CHROME_BINARY_PATH"] = "/usr/bin/google-chrome"
    else:
        os.environ["PLATFORM"] = "unknown"
    
    logger.info(f"Platform detected: {os.getenv['PLATFORM']}")

# Setting up ENV Method.
def setup_env():
    logger.info("Setting up ENV...")
    set_platform_env()
    load_dotenv()   # .ENV file 
    logger.info("Done.")
