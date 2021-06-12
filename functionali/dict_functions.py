""" functions to work with dictionaries"""


def keys(dictionary: dict) -> tuple:
    """Return a tuple of keys in a dictionary."""
    return tuple(dictionary.keys())


def values(dictionary: dict) -> tuple:
    """Return a tuple of values in a dictionary."""
    return tuple(dictionary.values())


def items(dictionary: dict) -> tuple:
    """Return a tuple of key/value pairs in a dictionary."""
    return tuple(dictionary.items())
