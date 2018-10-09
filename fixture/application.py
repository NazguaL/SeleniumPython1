from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def destroy_fixture(self):
        self.wd.quit()
