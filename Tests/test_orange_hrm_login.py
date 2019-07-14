from selenium import webdriver
import pytest,pytest_html,time, HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Drivers.drivers import Drivers
from Pages.loginPage import LoginPage
from Pages.homepage import HomePage


class TestOrangeHRM:

    @pytest.fixture()
    def setup(self):
          self.driver = Drivers.initializeChromeDriver()
          self.driver.get('https://opensource-demo.orangehrmlive.com/')
          yield
          self.driver.close()

    def test_homepagetitle(self,setup):
      assert self.driver.title == "OrangeHRM"
      print("Passed")

    def test_login_valid(self,setup):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        time.sleep(5)
        homepage.click_logout()
        time.sleep(10)