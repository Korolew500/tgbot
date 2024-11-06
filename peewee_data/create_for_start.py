from peewee import CharField, IntegerField, SqliteDatabase
from peewee import Model

# Создаем подключение к базе данных
db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(unique=True)
    name = CharField()
    start_count = IntegerField(default=0)
    currency_count = IntegerField(default=0)
    metals_count = IntegerField(default=0)
    news_count = IntegerField(default=0)
    help_count = IntegerField(default=0)

def create_tables():
    with db.connection_context():
        try:
            # Создаем таблицу user, если она не существует
            db.create_tables([User], safe=True)
        except Exception as e:
            print(f"Произошла ошибка при создании таблиц: {e}")