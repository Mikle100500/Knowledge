from selenium.webdriver.common.by import By


class PageLocators(object):
    SIGN_IN_BUTTON = (By.ID, 'gb_70')
    SET_EMAIL_BUTTON = (By.ID, 'next')
    SET_PASSWORD_BUTTON = (By.ID, 'signIn')
    EMAIL_BUTTON = (By.XPATH, './/*[@id="gbw"]/div/div/div[1]/div[2]/a')
    COUNT_ALL_LETTERS = (By.XPATH, '//table[contains(@id, ":3")]//tr')
    COMPOSE = (By.ID, ':4s')
    SEND_TO = (By.ID, ':a2')
    THEME_OF_THE_LETTER = (By.ID, ':a2')
    SEND_LETTER = (By.ID, ':9c')