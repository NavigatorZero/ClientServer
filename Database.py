import pymysql


class Database:
    conn = pymysql.connect('localhost',
                           'root',
                           'Savelev01',
                           'mainChema')

    cur = conn.cursor()

    def getTable(self, table: str):

        with self.conn:
            self.cur.execute("SELECT * FROM " + table)
            rows = self.cur.fetchall()

        return rows

    def getTableList(self):
        with self.conn:
            self.cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='mainChema'")
            rows = self.cur.fetchall()
            for row in rows:
                print(row)

