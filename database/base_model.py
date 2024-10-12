from peewee import Model
from peewee_data.db_file import db

class BaseModel(Model):
    class Meta:
        database = db
