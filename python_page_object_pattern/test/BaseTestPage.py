import unittest
from selenium import webdriver


class BaseTestPage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.get("http://www.google.com/ncr")

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
