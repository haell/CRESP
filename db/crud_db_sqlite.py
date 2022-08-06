import sqlite3


class CRUD:
    def __init__(self):
        self.con = sqlite3.connect('cresp.db')
        self.cur = self.con.cursor()

    def create(self):
        CRUD.temporizador()
        # Create table
        self.cur.execute('''CREATE TABLE stocks
                       (date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        self.cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        self.con.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.con.close()

    @classmethod
    def temporizador(cls, b):
        from time import sleep
        a = b
        sleep(a)

