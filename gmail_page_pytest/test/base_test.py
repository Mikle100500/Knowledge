import pytest
from selenium import webdriver


class BaseTestPytest(object):
    @pytest.fixture(scope="class")
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.get("http://www.google.com/ncr")


        # def tearDownClass(self):
        #     self.driver.close()


if __name__ == "__main__":
    pytest.main()
