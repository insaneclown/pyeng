import peewee

from core.models import BaseModel


class Sample(BaseModel):
    """Representation of the sample model.

    This class is temporary. It's created for the testing
    of automatic synchronization of the database.
    """
    value = peewee.IntegerField()