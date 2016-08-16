import unittest
from selenium import webdriver


class BaseTestPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com/ncr")

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()