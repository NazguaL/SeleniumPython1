import mysql.connector
import json
import os.path
from fixture.db import DbFixture
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
dbfixture = DbFixture(host=db_config["host"], database=db_config["database"], user=db_config[ "user"], password=db_config["password"])

try:
    cursor = dbfixture.connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    dbfixture.connection.close()