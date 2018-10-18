import mysql.connector
import json
import os.path
from model.group import Group
from fixture.orm import ORMFixture
 # connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")


"""
try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
"""
json_config = None


def load_config(file):
    global json_config
    if json_config is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file_path) as config_file:
            json_config = json.load(config_file)
    return json_config


db_config = load_config("config.json")["db"]
dbfixture = ORMFixture(host=db_config["host"], database=db_config["database"], user=db_config[ "user"], password=db_config["password"])

try:
    groups = dbfixture.get_groups_list()
    for group in groups:
        print(group)
    print(len(groups))
    contacts = dbfixture.get_contacts_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
    gs = dbfixture.get_contacts_not_in_group(Group(id="331"))
    for g in gs:
        print(g)
    print(len(gs))

finally:
    pass # dbfixture.teardown()
