from Page_methods import YandexHelper
from BaseApp import BasePage
import time
class yandex_(YandexHelper,BasePage):
    pass
yandex = yandex_(base_url="https://passport.yandex.ru/auth/add?origin=home_yandexid&retpath=https%3A%2F%2Fyandex.ru&backpath=https%3A%2F%2Fyandex.ru")
yandex.go_to_site()
yandex.enter_Email()
yandex.click_button()
time.sleep(2)
yandex.enter_Password()
yandex.click_button()