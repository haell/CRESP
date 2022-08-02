from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///file.db")

Session = sessionmaker(bind=engine)
session = Session()

session.execute('CREATE TABLE users('
                'id INT '
                'name VARCHAR '
                'email VARCHAR)')
