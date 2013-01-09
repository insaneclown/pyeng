import peewee

database = peewee.SqliteDatabase('pyeng.db')


class BaseModel(peewee.Model):
    """Base model.

    Dictates that each model uses the same database.
    """
    class Meta:
        database = database
