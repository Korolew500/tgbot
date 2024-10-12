from database.user import User
from peewee_data.db_file import db


def create_tables():
    # Создается таблица user
    db.connect()
    db.create_tables([User], safe=True)
