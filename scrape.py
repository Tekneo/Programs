from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector 
import csv
def validate_field(field):
    field = 'No results'
    return field

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('https://www.linkedin.com')

email = driver.find_element_by_xpath('//*[@id="session_key"]')
email.send_keys('***@gmail.com')

password = driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys('***')

log_in_button = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button')
log_in_button.click()

driver.get('https://www.google.com')
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "Bengaluru"')
search_query.send_keys(Keys.RETURN)

linkedin = driver.find_elements_by_class_name('yuRUbf')

linkedin = [url.text for url in linkedin]

print(linkedin)

for linkedin_url in linkedin:
    driver.get(linkedin_url)
    sel = Selector(text=driver.page_source) 

    name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()
    if job_title:
        job_title = job_title.strip()

    job_title = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first()
    if job_title:
        job_title = job_title.strip()

    company = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()
    if company:
        company = company.strip()

    college = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()
    if college:
        college = college.strip()

    location = sel.xpath('//*[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first()
    if location:
        location = location.strip()


    linkedin_url = driver.current_url

    print('\n')
    print('Name: ' + name)
    print('Job Title: ' + job_title)
    print('Company: ' + company)
    print('College: ' + college)
    print('Location: ' + location)
    print('URL: ' + linkedin_url)
    print('\n')

    writer = csv.writer(open('LinkedInURL.csv', 'wb'))
    writer.writerow(['Name','Job Title','Company','College', 'Location','URL'])

    writer.writerow([name.encode('utf-8'), job_title.encode('utf-8'), company.encode('utf-8'), college.encode('utf-8'), location.encode('utf-8'), linkedin_url.encode('utf-8')])