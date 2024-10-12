from peewee import CharField, IntegerField
from database.base_model import BaseModel


class User(BaseModel):
    user_id = IntegerField(unique=True)
    name = CharField()
    start_count = IntegerField(default=0)
    currency_count = IntegerField(default=0)
    metals_count = IntegerField(default=0)
    news_count = IntegerField(default=0)
    help_count = IntegerField(default=0)
