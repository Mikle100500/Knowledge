from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from python_page_object_pattern.core.locators import PageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_title_matches(self):
        return "Google" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(By.ID, 'gb_70')
        element.click()


class LogInEmailAccount(BasePage):
    def set_email(self):
        email = self.driver.find_element(By.ID, 'next').click()
        email.send_keys('forTestingJohnTester@gmail.com', Keys.ENTER)

    def set_password(self):
        element = self.driver.find_element(PageLocators.SET_PASSWORD_BUTTON)
        element.send_keys('gmailtest', Keys.ENTER)


class EmailPage(BasePage):
    def load_mail_page(self):
        element = self.driver.find_element(PageLocators.EMAIL_BUTTON)
        element.click()

    def count_letters_at_a_page(self):
        element = self.driver.find_element(PageLocators.COUNT_ALL_LETTERS)
        return len(element)

    def send_a_letter_to_smb(self, adress, theme_of_the_letter):
        element = self.driver.find_element(PageLocators.COMPOSE)
        element.click()
        element = self.driver.find_element(PageLocators.SEND_TO)
        element.send_keys(adress, Keys.ENTER)
        element = self.driver.find_element(PageLocators.THEME_OF_THE_LETTER)
        element.send_keys(theme_of_the_letter, Keys.ENTER)
        element = self.driver.find_element(PageLocators.SEND_LETTER)
        element.click()