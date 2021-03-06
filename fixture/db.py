import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=self.host, database=self.database, user=self.user,
                                                  password=self.password)
        # self.connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root",
        #                                          password="")
        self.connection.autocommit = True

    def get_groups_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            # self.connection.commit()
            cursor.close()
            # self.connection.close()
        return list

    def get_contacts_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            # self.connection.commit()
            cursor.close()
            # self.connection.close()
        return list

    def teardown(self):
        self.connection.close()

