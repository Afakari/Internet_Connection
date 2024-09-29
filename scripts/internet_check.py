from os import getenv, system
from logger import logger


# Simple method to check conncetion
def Check_internet_connection() -> bool:
    logger.info("Checking internet connection...")
    t = "-c" if getenv("PLATFORM") == 'linux' else '-n'
    if system(f"ping {t} 1 8.8.8.8")     == 0 :   # To Limit pings to a single time
        logger.info("Connection not found.")
        return False
    logger.info("Conncetion active!")
    return True
        