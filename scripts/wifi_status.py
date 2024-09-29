from subprocess import run
from logger import logger
from os import getenv

# Check if interface is connceted
def check_current_wifi_linux():
    try: 
        result = run(['nmcli', '-t', '-f', 'ACTIVE,SSID', 'device', 'wifi'], capture_output=True, text=True)
        wifi_list = result.stdout.strip().splitlines()
        for wifi in wifi_list:
            active,ssid = wifi.split(":")
            if active  == "yes":
                logger.info(f"Connceted to wifi: {ssid}")
                return ssid
            logger.warning("No active conncetion found.")
            return None
    except Exception as e:
        logger.error(f"Error checking WiFi connection: {e}")
        return None

def check_current_wifi_windows():
    try:
        result = run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        for line in result.stdout.strip().lower().splitlines():
            if "ssid" in line:
                ssid = line.split(':').strip()
                logger.info(f"Connceted to wifi: {ssid}")
                return ssid
            logger.warning("No active conncetion found.")
            return None
    except Exception as e:
        logger.error(f"Error checking WiFi connection: {e}")
        return None


def check_current_wifi(platform:str) -> str | None:
    logger.info("Checking wifi connection status...")
    platform = getenv("PLATFORM")
    if platform == 'linux':
        return check_current_wifi_linux()
    elif platform == 'windows':
        return check_current_wifi_windows()
    else:
        logger.error("Did you set PLATFORM Correctly?")
        return None


def connect_to_wifi_linux(wifi_ssid: str,wifi_password:str) -> bool:
    try:
        command = ['nmcli', 'device', 'wifi', 'connect', wifi_ssid, 'password', wifi_password]
        result = run(command, capture_output=True, text=True)

        if result.returncode == 0:
            logger.info(f"Successfully connected to {wifi_ssid}")
        else:
            logger.error(f"Failed to connect to {wifi_ssid}: {result.stderr}")
    except Exception as e:
        logger.error(f"Error while trying to connect to WiFi: {e}")

def connect_to_wifi_windows(wifi_ssid : str,wifi_password:str) -> bool:
    try:
            # This assumes the WiFi profile is already configured.
            # You can automate setting up profiles if needed.
        command = ['netsh', 'wlan', 'connect', 'name=' + wifi_ssid]
        
        result = run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            logger.info(f"Successfully connected to {wifi_ssid}")
        else:
            logger.error(f"Failed to connect to {wifi_ssid}: {result.stderr}")
    except Exception as e:
        logger.error(f"Error while trying to connect to WiFi: {e}")


def conncet_to_wifi(platform, wifi_ssid,wifi_password):
    logger.info("Attempting to conncet to SSID")

    if platform == 'linux':
        return connect_to_wifi_linux(wifi_ssid,wifi_password)
    elif platform == 'windows':
        return connect_to_wifi_windows(wifi_ssid,wifi_password)
    else:
        logger.error("Did you set PLATFORM Correctly?")
        return None


