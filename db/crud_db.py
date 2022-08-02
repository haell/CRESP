from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class CRUD:
    def __init__(self):
        self.engine = create_engine("sqlite:///cresp.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_table(self):
        self.session.execute('CREATE TABLE cidade('
                             'id INT primary key, '
                             'name varchar(30), '
                             'email varchar(100)) ')

    def update(self):
        self.session.execute('INSERT INTO "cidade" (id, name, email) VALUES '
                             "(1, 'admin', 'admin@example.com') ")
        self.session.execute('INSERT INTO "cidade" (id, name, email) VALUES '
                             "(2, 'user', 'user@example.com') ")
        self.session.execute('INSERT INTO "cidade" (id, name, email) VALUES '
                             "(3, 'client', 'client@sample.com') ")
        self.session.execute('INSERT INTO "cidade" (id, name, email) VALUES '
                             "(4, 'haell', 'haell@haell.com') ")

    def get(self):
        result = self.session.execute('SELECT * FROM cidade')
        print()
        for row in result:
            print(row)

    def delete(self):
        self.session.execute(f'DELETE FROM cidade WHERE name="user"')


if __name__ == '__main__':
    hh = CRUD()
    # hh.create_table()
    # hh.update()
    hh.delete()
    hh.get()
