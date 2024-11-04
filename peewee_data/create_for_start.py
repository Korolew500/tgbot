from database.user import User
from peewee_data.db_file import db


def create_tables():
    # Используем контекстный менеджер для подключения
    with db.connection_context():
        try:
            # Создаем таблицу user, если она не существует
            db.create_tables([User], safe=True)
            print("Таблицы успешно созданы.")
        except Exception as e:
            print(f"Произошла ошибка при создании таблиц: {e}")
