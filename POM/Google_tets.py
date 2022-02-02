from Page_methods import GoogleHelper
from BaseApp import BasePage

class google_(GoogleHelper,BasePage):
    pass
google = google_(base_url="https://www.google.ru/")
google.go_to_site()
google.search_obj('купить кофемашину bork c804')
google.click_button()
google.checking_link()
