from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from linkedin_registration import registration

from collector import links_collector

from page_scraper import scraper

from filewriter import write_to_file


chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)

def main() -> None:
    """Start function"""

    registration(driver)
    links = links_collector(amount_of_users=10, driver=driver)
    jobdata = scraper(links, driver)
    write_to_file(jobdata)
    

    

if __name__ == '__main__':
    main()

