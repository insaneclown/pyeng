
"""
Module with the tools to work with the database.
"""

from core.models import User
from plugins.sample.models import Sample


def sync_database():
    """Synchronizes the database.

    Creates the database tables for core and all plugins
    whose tables have not already been created.
    """
    create_tables(get_model_classes())


def get_model_classes():
    """Loads all classes of models.

    Returns:
        List of model based on BaseModel.
    """
    # TODO: add automatic models detection from plugins
    return [User, Sample]


def create_tables(model_classes):
    """Creates the database tables for given model classes
    whose tables have not already been created.

    Args:
        model_classes:
            List of model based on BaseModel.
    """
    for model_class in model_classes:
        model_class.create_table(fail_silently=True)
