from selenium.webdriver.common.keys import Keys


class GmailPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_gmail(self):
        self.driver.get('https://www.google.com/ncr')
        self.driver.find_element_by_id('gb_70').click()

    def login(self):
        self.driver.find_element_by_id('Email').send_keys('forTestingJohnTester@gmail.com', Keys.ENTER)
        self.driver.find_element_by_id('next').click()

        self.driver.find_element_by_id('Passwd').send_keys('gmailtest')
        self.driver.find_element_by_id('PersistentCookie').click()
        self.driver.find_element_by_id('signIn').click()
        self.driver.find_element_by_xpath('.//*[@id="gbw"]/div/div/div[1]/div[2]/a').click()

    def logout(self):
        self.driver.find_element_by_id('gb').click()
        self.driver.find_element_by_id('gb_71').click()

    def number_of_mails(self):
        return len(self.driver.find_elements_by_xpath('//table[contains(@id, ":3")]//tr'))
