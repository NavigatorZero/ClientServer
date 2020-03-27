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
            rows = self.cur.fetchall()git
