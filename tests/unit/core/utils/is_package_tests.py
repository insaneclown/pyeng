from mock import patch

from core.utils.lang import is_package


@patch('os.path.isdir')
@patch('os.path.isfile')
def test_when_dir_and__init__file_exists_(isfile, isdir):
    isdir.return_value = True
    isfile.return_value = True
    assert is_package('/home/src/tea')
    isdir.assert_called_with('/home/src/tea')
    isfile.assert_called_with('/home/src/tea/__init__.py')


@patch('os.path.isdir')
@patch('os.path.isfile')
def test_when_dir_exists_without__init__file(isfile, isdir):
    isdir.return_value = True
    isfile.return_value = False
    assert not is_package('/home/src/tea')
    isdir.assert_called_with('/home/src/tea')
    isfile.assert_called_with('/home/src/tea/__init__.py')
    

@patch('os.path.isdir')
def test_when_dir_dont_exist(isdir):
    isdir.return_value = False
    assert not is_package('/home/src/tea')
    isdir.assert_called_with('/home/src/tea')