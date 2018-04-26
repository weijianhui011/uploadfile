import pymssql
from public import Config


class SqlServer:
    def __init__(self, host, user, pwd, db):
        self.host = host  # 主机名
        self.user = user  # 用户名
        self.pwd = pwd  # 密码
        self.db = db  # 数据库名

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
            # 连接数据库
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):  # 执行查询语句
        cur = self.__GetConnect()
        cur.execute(sql)
        data = cur.fetchall()  # 一次获取全部数据
        row = cur.fetchone()  # 一次获取一行数据
        rows = cur.fetchmany(10)  # 获取10行数据

        # 查询完毕后必须关闭连接
        self.conn.close()
        return data

    def ExecNonQuery(self, sql):  # 执行非查询语句
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def main():
    # 使用sa登录，密码为自设sa登录密码
    ss = SqlServer(**Config.mssql_conn_dic)
    data = ss.ExecQuery("SELECT * FROM [dbo].[Nb_File]")
    for row in data:
        print (row)
       # row[0], row[1].encode("utf8")



if __name__ == '__main__':
    main()