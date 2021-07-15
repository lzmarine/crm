import pymysql
class database:
    def __init__(self):
        import pymysql
        mydb=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='crm',charset='utf8')
        self.cursor= mydb.cursor()
    def excute(self,sql,fetNUM=2):
        self.cursor.execute(sql)
        if fetNUM==1:
            res=self.cursor.fetchone()
        elif fetNUM==2:
            res=self.cursor.fetchall()
        return res


