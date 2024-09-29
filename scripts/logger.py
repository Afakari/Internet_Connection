import logging

# Basic login setup
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("network_monitor.log"), 
        logging.StreamHandler()                    
    ]
)

# Logger method
logger = logging.getLogger()
