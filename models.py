import peewee

database = peewee.SqliteDatabase('pyeng.db')


class BaseModel(peewee.Model):
    """Base model.

    Dictates that each model uses the same database.
    """
    class Meta:
        database = database


class User(BaseModel):
    """Representation of the user model.

    Because the applications are to be stored for many users statistics
    therefore there is a need to have a User model.

    User has only its own unique name.
    """
    name = peewee.CharField(unique=True)