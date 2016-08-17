import unittest
from time import sleep

from selenium import webdriver

from python_page_object_pattern.core import pages


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com/ncr")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_get_gmail_page(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.click_login_button()

    def test_login_page(self):
        login_page = pages.LogInEmailAccount(self.driver)
        login_page.set_email()
        login_page.set_password()

    def test_email_page(self):
        email_page = pages.EmailPage(self.driver)
        email_page.load_mail_page()
        assert email_page.count_letters_at_the_page() == 0

    # def test_send_mail(self):
    #     mail = pages.EmailPage(self.driver)
    #     mail.send_a_letter_to_smb(self, 'forTestingJohnTester@gmail.com', 'TestTestTest')

if __name__ == "__main__":
    unittest.main()