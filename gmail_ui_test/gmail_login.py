from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

login = "forTestingJohnTester@gmail.com"
password = "gmailtest"


# class GmailLoginLogut(object):
#     def gmail_login(self, login, password):

# class TestGmailMails(unittest.TestCase):
#     def get_mail_page(self):
#         pass
#
#     def login(self):
#         pass

driver = webdriver.Firefox()

driver.get('https://www.google.com/ncr')
driver.find_element_by_id('gb_70').click()

driver.find_element_by_id('Email').send_keys(login, Keys.ENTER)
driver.find_element_by_id('next').click()

driver.find_element_by_id('Passwd').send_keys(password)
driver.find_element_by_id('PersistentCookie').click()
driver.find_element_by_id('signIn').click()
driver.find_element_by_xpath('.//*[@id="gbw"]/div/div/div[1]/div[2]/a').click()

print(len(driver.find_elements_by_xpath('//table[contains(@id, ":3")]//tr')))

driver.quit()
# def count_mails():
