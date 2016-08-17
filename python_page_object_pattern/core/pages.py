from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        email = self.driver.find_element(By.ID, 'Email')
        email.send_keys('forTestingJohnTester@gmail.com', Keys.ENTER)

    def set_password(self):
        element = self.driver.find_element(By.ID, 'Passwd')
        element.send_keys('gmailtest', Keys.ENTER)

    def load_mail_page(self):
        element = self.driver.find_element(By.XPATH, './/*[@id="gbw"]/div/div/div[1]/div[2]/a')
        element.click()


class EmailPage(BasePage):
    def count_letters_at_the_page(self):
        element = self.driver.find_elements(By.XPATH, '//table[contains(@id, ":3")]//tr')
        return len(element)

    def send_a_letter_to_yourself(self):
        element = self.driver.find_element(By.ID, ':4s')
        element.click()
        element = self.driver.find_element(By.ID, ':a2')
        element.send_keys('forTestingJohnTester@gmail.com', Keys.ENTER)
        element = self.driver.find_element(By.ID, ':a2')
        element.send_keys('TEST', Keys.ENTER)
        element = self.driver.find_element(By.ID, ':9c')
        element.click()