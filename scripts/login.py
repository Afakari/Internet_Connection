from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager as CDM
from logger import logger
from os import getenv


 # Login method , opens the page , fills in credentials
def login() -> None:
    ip_address = getenv("LOGIN_IP")
    username = getenv("LOGIN_USERNAME")
    password = getenv("LOGIN_PASSWORD")
    username_xpath=getenv("LOGIN_USERNAME_XPATH")
    password_xpath = getenv("LOGIN_PASSWORD_XPATH")
    submit_xpath = getenv("LOGIN_SUBMIT_XPATH")
    chrome_binary = getenv("CHROME_BINARY_PATH")

    if not all([ip_address, username, password, username_xpath, password_xpath, submit_xpath]):
        logger.error("Did you set all the ENV variabls?")
    
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.binary_location = chrome_binary
        service = Service(service)
        driver = webdriver.Chrome(service=service,options = options)
        logger.info("Started Chrome Dirver.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
        )
        username_field = driver.find_element(By.XPATH, username_xpath)
        username_field.clear()
        username_field.send_keys(username)
        logger.info("Filled username.")
                
        password_field = driver.find_element(By.XPATH, password_xpath)
        password_field.clear()
        password_field.send_keys(password)
        logger.info("Filled password.")

        submit_button = driver.find_element(By.XPATH, submit_xpath)
        submit_button.click()
        logger.info("Submit...")

        WebDriverWait(driver, 10).until(EC.url_changes(f"http://{ip_address}"))
        logger.info("Login successful.")

    except TimeoutException:
        logger.error("Timeout: One or more elements were not found within the specified time.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        logger.info("Closed the browser.")
        