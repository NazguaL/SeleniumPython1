class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_login_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.if_logged_in():
            self.logout()

    def if_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def if_logged_in_as(self, userame):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+userame+")"

    def ensure_login(self, username, password):
        if self.if_logged_in():
            if self.if_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)