import sqlite3


class CRUD:
    def __init__(self):
        self.con = sqlite3.connect('cresp.db')
        self.cur = self.con.cursor()

    def create(self):
        """
        Método que cria tabela no banco de dados, com uso da biblioteca sqlite3.
        :return: Cria um tabela banco de dados.
        """
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS stocks(date text, trans text, symbol text, qty real, price real)''')

    @classmethod
    def temporizador(cls, b):
        """
        Método que atrasa em 1 segundo a execução.
        :param b: numero inteiro
        :return: 1 segundo de pausa.
        """
        from time import sleep
        aa = b
        sleep(aa)


if __name__ == '__main__':
    db = CRUD()
    db.create()
    help(db.create)
