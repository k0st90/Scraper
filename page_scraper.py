from time import sleep

import random

from bs4 import BeautifulSoup

from typing import List

from typing import Dict

def scraper(links: List[str], driver, Jobdata=[]) -> List[Dict[str, str]]:
    """Scrapes needed information from linkedin user page"""

    for link_list in links:
        for link in link_list:
    
            driver.get(link)

            sleep(random.uniform(2.5, 4.9))
                    
            src = driver.page_source

            soup = BeautifulSoup(src, 'lxml')
            
            main_info = soup.find_all('div', {'class':'pv-text-details__left-panel'}) # Name and job title of person
            if main_info:
                name = soup.find_all('div', {'class':'pv-text-details__left-panel'})[0].find('h1').get_text().strip()
                job_title = soup.find_all('div', {'class':'pv-text-details__left-panel'})[0].find('div', {'class':'text-body-medium break-words'}).get_text().strip()
            else:
                name = ''
                job_title=''

            company_info = soup.find_all('ul', {'class':'pv-text-details__right-panel'}) # Name of the current company the person works at
            if company_info:
                current_company = soup.find_all('ul', {'class':'pv-text-details__right-panel'})[0].find('li').get_text().strip()
            else:
                current_company = ''
                    
            experience = soup.find_all('section', {'class':'artdeco-card ember-view relative break-words pb3 mt2'}) # Names of all the previous companies the person worked at
            experience_clean_line = []
            for section in experience:
                if section.find_all('div', {'id':'experience'}):
                    experience_info = section.find_all("span", {'aria-hidden':'true'})
                    for line in experience_info:
                        experience_clean_line.append(line.get_text().strip().replace(u'\xa0', u' '))
                        
            education = soup.find_all('section', {'class':'artdeco-card ember-view relative break-words pb3 mt2'}) # All information about person's educational experience 
            education_clean_line = []
            for section in education:
                if section.find_all('div', {'id':'education'}):
                    education_info = section.find_all("span", {'aria-hidden':'true'})
                    for line in education_info:
                        education_clean_line.append(line.get_text().strip().replace(u'\xa0', u' '))

            #P.S. Linkedin doesn't provide users with telephone numbers unless the person has added you to friend list, so I decided to scrape education and experience

            data = {
                'name':name,
                'job_title':job_title,
                'current_company':current_company,
                'experience': '\n'.join(experience_clean_line),
                'education': '\n'.join(education_clean_line),
                'link':link
                }
                    
            Jobdata.append(data)
    return(Jobdata)



