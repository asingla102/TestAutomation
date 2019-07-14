from selenium import webdriver
import pytest,pytest_html,time
# chromeDriver = None


class Drivers:

    @staticmethod
    def initializeChromeDriver():
        global chromeDriver
        chromeDriver = webdriver.Chrome(executable_path='C:/Users/asing/PycharmProjects/TestAutomation/Drivers/chromedriver_win32/chromedriver.exe')
        chromeDriver.maximize_window()
        return chromeDriver
