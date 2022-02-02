from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:

    def __init__(self, base_url):
        self.browser = webdriver.Chrome(executable_path='POM\chromedriver.exe')
        self.base_url = base_url

    def go_to_site(self):
        return self.browser.get(self.base_url)