from selenium import webdriver


def before_all(context):
    path = 'C:/Users/asing/PycharmProjects/TestAutomation/Drivers/chromedriver_win32/chromedriver.exe'
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get('google.com')

def after_all(context):
    context.driver.close()