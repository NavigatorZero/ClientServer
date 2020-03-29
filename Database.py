import pymysql


class Database:
    conn = pymysql.connect('localhost',
                           'root',
                           'DBPASSWORDHEHE',
                           'mainChema')

    cur = conn.cursor()

    def getTable(self, table: str):
        with self.conn:
            result = []
            self.cur.execute("SELECT * FROM " + table)
            rows = self.cur.fetchall()
            for row in rows:
                result.append(str(row).encode())

            return result

    def updateTable(self, data):
        with self.conn:
            if data[0] == 1:
                self.cur.execute(""" Insert into `tablesubject` (`subject`, `teacher`) SET (%s, %s)""",
                                 (data[1], data[2]))

                self.conn.commit()
                print("sucess")
