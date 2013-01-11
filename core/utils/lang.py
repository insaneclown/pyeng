from os import path


def is_package(dir):
    """Checks if the specified path is a package.

    Checks whether a given path is a directory
    that contains the file __init__.py.

    Args:
        dir:
            Directory path specified package.

    Returns:
        True if it's a package, otherwise False.
    """
    return path.isdir(dir) and path.isfile(path.join(dir, '__init__.py'))


