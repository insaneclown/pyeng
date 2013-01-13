from core.db import get_model_classes
from core.models import User
from plugins.sample.models import Sample


def test_whether_loads_all_models():
    assert [User, Sample] == get_model_classes()
