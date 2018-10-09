from selenium.webdriver.chrome.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)

    def logout(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def submit_new_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_new_group_creation(self):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_login_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def destroy_fixture(self):
        self.wd.quit()
