from mock import patch

from core.db import sync_database
from core.models import User


@patch('core.db.create_tables')
@patch('core.db.get_model_classes')
def test(get_model_classes, create_tables):
    get_model_classes.return_value = [User]
    sync_database()
    get_model_classes.assert_called_with()
    create_tables.assert_called_with([User])