from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Data import email, password
import time

class GoogleHelper(BasePage):
     #Поле поиска
    def search_obj(self,search):
        return self.browser.find_element_by_name('q').send_keys(search)

    #Клик на подтверждение
    def click_button(self):
        return self.browser.find_element_by_name('q').send_keys(Keys.RETURN)

    #проверка на ссылку www.mvideo.ru 
    def checking_link(self):
        try:
            self.browser.find_element_by_xpath('//a[@href="https://www.mvideo.ru/products/kofeinaya-stanciya-bork-c804-4000182"]').click()
            print('www.mvideo.ru - Есть' )
        except:
            print("отсутствует")
        time.sleep(5)
        self.browser.quit()
    

class YandexHelper(BasePage):
    #Ввод Email
    def enter_Email(self):
        return self.browser.find_element_by_xpath('//input[@data-t="field:input-login"]').send_keys(email)

    #Клик на подтверждение
    def click_button(self):
        return self.browser.find_element_by_xpath('//button[@data-t="button:action:passp:sign-in"]').click()

    #Ввод пароля
    def enter_Password(self):
        return WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-t="field:input-passwd"]')
            )
        ).send_keys(password)
