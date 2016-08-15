import unittest

from selenium import webdriver
from gmail_ui_test.wrappers.gmail_wrapper import GmailPage


class TestNumberOfMails(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Firefox()

    # @staticmethod
    # def page_init():
    #     return GmailPage

    def test_number_of_mails(self):
        gmail = GmailPage()
        gmail.navigate_to_gmail()
        gmail.login()
        self.assertEquals(gmail.number_of_mails(), 3)

if __name__ == '__main__':
    unittest.main()