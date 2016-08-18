from gmail_page_object_pattern.core import pages
from gmail_page_object_pattern.test.BaseTest import BaseTest


class GoogleSearchTest(BaseTest):
    def test_01_get_gmail_page(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.click_login_button()

    def test_02_login_page(self):
        login_page = pages.LogInEmailAccount(self.driver)
        login_page.set_email()
        login_page.set_password()
        login_page.load_mail_page()
        assert self.driver.title == "Входящие - fortestingjohntester@gmail.com - Gmail"

    def test_03_count_letters(self):
        email_page = pages.EmailPage(self.driver)
        assert email_page.count_letters_at_the_page() == 5

    def test_04_send_mail(self):
        mail = pages.EmailPage(self.driver)
        mail.send_a_letter_to_yourself(email_adress="fortestingjohntester@gmail.com", subject='test')
