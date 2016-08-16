import unittest

from selenium import webdriver
from gmail_ui_test.wrappers.gmail_wrapper import GmailPage


class TestNumberOfMails(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def gmail(driver):
        gmail = GmailPage(driver)
        return gmail

    def test_get_gmail(self):
        gmail = self.gmail(self.driver)
        gmail.navigate_to_gmail()

    def test_login(self):
        gmail = self.gmail(self.driver)
        gmail.login()

    def test_mail_numbers(self):
        gmail = self.gmail(self.driver)
        self.assertEquals(gmail.number_of_mails(), 3)


if __name__ == '__main__':
    unittest.main()