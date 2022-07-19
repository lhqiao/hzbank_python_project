
import sqlite3

def create_table():
        sqlstr = "create table user (sid int(5) primary key, \
        name varchar(10), email varchar(25))"
        conn.execute(sqlstr)
        print("create table successfully")
        conn.close()

def initiate_table():
        cur = conn.cursor()
        sqlstr1 = "insert into user(sid, name, email) values(1001, '张大山', 'zhangds@163.com') "
        cur.execute(sqlstr1)
        sqlstr2 = "insert into user(sid, name, email) values(1002, '李晓丽', 'lixli@163.com') "
        cur.execute(sqlstr2)
        sqlstr3 = "insert into user(sid, name, email) values(1003, '赵四方', 'zaoshi@163.com') "
        cur.execute(sqlstr3)
        conn.commit()
        print("Records created successfully")
        conn.close()
def get_data():
        cur = conn.cursor()
        sqlstr = "select * from  user"
        s = cur.execute(sqlstr)
        for row in s:   #得到的赋值给s
                print("sid=", row[0])
                print("name=", row[1])
                print("email=", row[2], '\n')
        conn.close()
def updata_data():

        cur = conn.cursor()
        sql_update = "update user set email='zhaosf@abc.com' where sid=1003"
        cur.execute(sql_update)
        conn.commit()

        sql_select = "select * from  user where sid=1003"
        s = cur.execute(sql_select)
        for row in s:
                print("sid=", row[0])
                print("name=", row[1])
                print("email=", row[2], '\n')
        conn.close()
def delete_data():
        cur = conn.cursor()
        sql_update = "delete from user  where sid=1002"
        cur.execute(sql_update)
        conn.commit()
        sql_select = "select * from  user"
        s = cur.execute(sql_select)
        for row in s:
                print("sid=", row[0])
                print("name=", row[1])
                print("email=", row[2], '\n')
        conn.close()


if __name__=="__main__":
        conn = sqlite3.connect("d:/groupdatabase.db")
        get_data()
        # conn = sqlite3.connect("d:/groupdatabase.db")
        # updata_data()
        # conn = sqlite3.connect("d:/groupdatabase.db")
        # delete_data()