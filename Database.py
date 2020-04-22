import pymysql
import pickle

class Database:
    conn = pymysql.connect('localhost',
                           'root',
                           '$password',
                           'mainChema')
    cur = conn.cursor()

    def getTable(self, table: str):
        with self.conn:
            result = [[] for i in range(2)]

            self.cur.execute("SELECT * FROM " + table)
            rows = self.cur.fetchall()
            for row in rows:
                result[0].append(row)

            self.cur.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME=%s", table)
            rows2 = self.cur.fetchall()

            for row in rows2:
                result[1].append(str(row[3]))

            result = pickle.dumps(result)
            return result

    def updateTable(self, data):
        with self.conn:
            try:
                self.cur.execute('DELETE FROM tablesubject')
                self.conn.commit()
                for item in data:
                    print(item[1])
                    print(item[2])
                    self.cur.execute("INSERT INTO tablesubject(Subject,Teacher) values (%s,%s)",
                                     (str(item[1]), str(item[2])))
                    self.conn.commit()
            except:
                print("error")