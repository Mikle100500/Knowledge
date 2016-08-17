import unittest

from selenium import webdriver

from python_page_object_pattern.core import pages


class GoogleSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
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
        login_page.load_mail_page()

    def test_count_letters(self):
        email_page = pages.EmailPage(self.driver)
        assert email_page.count_letters_at_the_page() == 3

    def test_send_mail(self):
        mail = pages.EmailPage(self.driver)
        mail.send_a_letter_to_yourself()


if __name__ == "__main__":
    unittest.main()
