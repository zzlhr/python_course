import pymysql


class DB(object):
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = "root"
        self.db_name = "python_course"
        self.db_link = pymysql.connect(self.host, self.username, self.password, self.db_name)
        self.cursor = self.db_link.cursor()

    def test(self):
        self.cursor.execute("select version()")
        result = self.cursor.fetchone()
        print(result)


# db = DB()
# db.test()
