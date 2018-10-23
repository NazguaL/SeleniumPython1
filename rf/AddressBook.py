import json
import os.path
import importlib
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="config.json", browser="Chrome"):
        self.browser = browser
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        print(config_file_path)
        with open(config_file_path) as config_file:
            self.json_config = json.load(config_file)

    def create_group(self, group):
        self.fixture.group.init_new_group_creation()
        self.fixture.group.fill_group_form(group)
        self.fixture.group.submit_new_group_creation()

    def delete_group(self, group):
        self.fixture.group.del_group_by_id(group.id)

    def get_group_list(self):
        return self.dbfixture.get_groups_list()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def init_fixtures(self):
        web_config = self.json_config["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        db_config = self.json_config["db"]
        self.dbfixture = DbFixture(host=db_config["host"], database=db_config["database"], user=db_config["user"],
                                   password=db_config["password"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])

    def destroy_fixtures(self):
        self.fixture.teardown()
        self.dbfixture.teardown()
