from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from settings import config

def registration(driver) -> None:
    """Registration in linkedin
    
    It's impossible to scrape information from linkedin profile without registration"""

    while True:
        try:
            driver.get('https://www.linkedin.com')

            username = driver.find_element(By.ID, 'session_key')

            username.send_keys(config.linkedin_gmail.get_secret_value())

            sleep(0.5)

            password = driver.find_element(By.ID, 'session_password')

            password.send_keys(config.linkedin_password.get_secret_value())

            sleep(0.5)

            sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

            sign_in_button.click()
            sleep(3)
        except:
            continue
        if username:
            break