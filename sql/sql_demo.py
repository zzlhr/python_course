from sql import database


def insert_demo():
    d = database.DB()
    sql = "insert into user(user_name, password, sex, age) values ('%s', '%s', '%s', '%s')"
    try:
        d.cursor.execute(sql % ('张三', '123456', 0, 20))
        d.db_link.commit()
    except:
        print("insert error")
        d.db_link.rollback()
    d.db_link.close()


def update_demo():
    d = database.DB()
    sql = "update user set password='%s' where uid=1"
    try:
        d.cursor.execute(sql % '234567')
        d.db_link.commit()
    except:
        print("update error")
        d.db_link.rollback()
    d.db_link.close()


def select_demo():
    d = database.DB()
    sql = "select * from user"
    d.cursor.execute(sql)
    results = d.cursor.fetchall()
    for row in results:
        print("user={uid:%s, user_name: %s, password: %s, sex:%s, age:%s, create_time:%s}"
              % (row[0], row[1], row[2], man_or_woman(row[3]), row[4], row[5]))


def man_or_woman(code):
    if code == 0:
        return "男"
    else:
        return '女',


select_demo()
