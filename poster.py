from selenium import webdriver
from settings import USERNAME, PASSWORD
import json
import random
import time

def login(browser):
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(USERNAME)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
    browser.find_element_by_xpath('//*[@id="_submit"]').click()
    return browser

def add_interview(browser, interview):
    email = interview['email']
    USA_STATES = [6,11,15,34,40] # california, florida, penn, new york, illinois (basically large states)
    browser.find_element_by_xpath('//*[@id="canvas-tools"]/div/div/div[3]/span/div/a/i').click()
    browser.find_element_by_xpath('//*[@id="canvas-tools"]/div/div/div[3]/span/div/ul/li[2]/a').click()
    browser.find_element_by_xpath('//*[@id="stream_customers_0_name"]').send_keys(email.split('@')[0].title())
    browser.find_element_by_xpath('//*[@id="stream_customers_0_title"]').send_keys(interview['role'].title())
    browser.find_element_by_xpath('//*[@id="stream_customers_0_company"]').send_keys(email.split('@')[1].split('.')[0].title())
    browser.find_element_by_xpath('//*[@id="customer-wrapper"]/div[3]/div/p/a').click()
    browser.find_element_by_xpath('//*[@id="stream_customers_0_email"]').send_keys(email)
    browser.find_element_by_xpath('//*[@id="stream_customers_0_industry"]/option[43]').click()
    browser.find_element_by_xpath('//*[@id="stream_customers_0_country"]/option[240]').click()
    state = random.choice(USA_STATES)
    browser.find_element_by_xpath('//*[@id="stream_customers_0_state"]/option[{}]'.format(state)).click()
    browser.find_element_by_xpath('//*[@id="btn-engagementType-3"]').click()
    datefield = browser.find_element_by_xpath('//*[@id="stream_occurredAt"]')
    datefield.clear()
    datefield.send_keys(interview['date'])
    browser.find_element_by_xpath('//*[@id="stream_notes"]').send_keys(interview['insights'])
    browser.find_element_by_xpath('//*[@id="form-body"]/div/div').send_keys(interview['description'])
    for hypothesis, action in interview['hypotheses']:
        browser.find_element_by_xpath('//*[@id="stream_relatedStreams_{}"]'.format(hypothesis)).click()
        browser.find_element_by_xpath('//*[@id="btn-stream_relatedStreams_{}-feedback"]/button[{}]'.format(hypothesis, action)).click()
    browser.find_element_by_xpath('//*[@id="btn-submit"]').click()

if __name__ == "__main__":
    browser = webdriver.Chrome('../chromedriver')
    browser.get('https://launchpadcentral.com/login')
    browser = login(browser)
    interviews = json.loads(open('sample.json').read())
    for interview in interviews:
        add_interview(browser, interview)
        time.sleep(2)

