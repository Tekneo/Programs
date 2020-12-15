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
email.send_keys('***')

password = driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys('***')

log_in_button = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button')
log_in_button.click()

driver.get('https://www.duckduckgo.com')
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "Bengaluru"')
search_query.send_keys(Keys.RETURN)

linkedin = driver.find_elements_by_class_name('result__url')

linkedin = [url.text for url in linkedin]

writer = csv.writer(open('LinkedInURL.txt', 'w+'))
writer.writerow(["Name","Job Title","Company","College", "Location","URL"])

for linkedin_url in linkedin:
    driver.get(linkedin_url)
    sel = Selector(text=driver.page_source) 

    #name = sel.xpath('//*[starts-with(@class, "pv-top-card--list")]/text()').extract_first()
    name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
    if name:
        name = name.strip()

    job_title = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal break-words")]/text()').extract_first()
    if job_title:
        job_title = job_title.strip()

    company = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
    if company:
        company = company.strip()
'''
    college = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
    if college:
        college = college.strip()
'''
    location = sel.xpath('//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()
    if location:
        location = location.strip()


    linkedin_url = driver.current_url

    print('Name: ' + name)
    print('Job Title: ' + job_title)
    print('Company: ' + company)
    #print('College: ' + college)
    print('Location: ' + location)
    print('URL: ' + linkedin_url)

    writer.writerow([name, job_title, company, location, linkedin_url])