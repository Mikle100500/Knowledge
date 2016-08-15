from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class GmailPage:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def navigate_to_gmail(self, driver):
        driver.get('https://www.google.com/ncr')
        driver.find_element_by_id('gb_70').click()

    def login(self, driver, account, password):
        driver.find_element_by_id('Email').send_keys(account, Keys.ENTER)
        driver.find_element_by_id('next').click()

        driver.find_element_by_id('Passwd').send_keys(password)
        driver.find_element_by_id('PersistentCookie').click()
        driver.find_element_by_id('signIn').click()

    def logout(self, driver):
        driver.find_element_by_id('.//*[@id="gb"]//span').click()
        driver.find_element_by_id('.//*[@id="gb_71"]').click()

    def number_of_mails(self, driver):
        return len(driver.find_elements_by_xpath('//table[contains(@id, ":3")]//tr'))
