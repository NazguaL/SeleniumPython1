import mysql.connector
from model.group import Group


class DbFixture:

    def __init__(self, host, database, user, password):
        # self.host = host
        # self.database = database
        # self.user = user
        # self.password = password
        # self.connection = mysql.connector.connect(host=self.host, database=self.database, user=self.user,
        #                                           password=self.password)
        self.connection = mysql.connector.connect(host=host, database=database, user=user,
                                                  password=password)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=id, name=name, header=header, footer=footer))
        finally:
            self.connection.close()
        return list


    def teardown(self):
        self.connection.close()

