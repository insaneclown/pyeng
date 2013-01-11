from mock import Mock

from core.db import create_tables


def test_when_given_few_model_classes():
    first_class = Mock()
    second_class = Mock()
    create_tables([first_class, second_class])
    first_class.assert_called_with(fail_silently=True)
    second_class.assert_called_with(fail_silently=True)
