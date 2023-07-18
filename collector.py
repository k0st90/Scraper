from time import sleep

import random

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from typing import List

def links_collector(amount_of_users: int, driver, links=[]) -> List:
    """Collects all links to user accounts in linkedin"""

    for x in range(0, amount_of_users, 10):
            driver.get(f'https://www.google.com/search?q=site:linkedin.com/in/+AND+"lead"&ei=sg61ZL6kFr2mwPAPgZuakAE&start={x}&sa=N&ved=2ahUKEwi-xYS8u5WAAxU9ExAIHYGNBhI4MhDy0wN6BAgKEAQ&biw=1920&bih=970&dpr=1')
            sleep(random.uniform(2.5, 4.9))
            linkedin_urls = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
            links.append(linkedin_urls)
    return links
        
            
        