""" Functions to traverse the sequence"""
from typing import Iterable, Any, TypeVar, Iterator

T = TypeVar("T")


def first(iterable: Iterable[T]) -> T:
    """
    >>> first([1,2,3,4,5])
    1
    """
    if not isinstance(iterable, Iterator):
        return next(iter(iterable))
    else:
        return next(iterable)


def last(iterable: Iterable[T]) -> T:
    """
    >>> last([1,2,3,4])
    4
    """
    try:
        return iterable[-1]
    except SyntaxError:  # extend
        return "non iter"


def rest(iterable: Iterable[T]) -> Iterator[T]:
    """
    >>> list(rest([1,2,3,4,5]))
    [2, 3, 4, 5]
    """
    it = iter(iterable)
    next(it)  # discard value
    return it  # return iterator


def second(iterable: Iterable[T]) -> T:
    """
    >>> second([1,2,3,4,5])
    2
    """
    if len(iterable) < 2:
        return last(iterable)
    else:
        return first(rest(iterable))


def third(iterable: Iterable[T]) -> T:
    """
    >>> third([1,2,3,4,5])
    3
    """
    if len(iterable) < 3:
        return last(iterable)
    else:
        return first(rest(rest(iterable)))


def fourth(iterable: Iterable[T]) -> T:
    """
    >>> fourth([1,2,3,4,5])
    4
    """
    if len(iterable) < 4:
        return last(iterable)
    else:
        return first(rest(rest(rest(iterable))))


def fifth(iterable: Iterable[T]) -> T:
    """
    >>> fourth([1,2,3,4,5])
    5
    """
    if len(iterable) < 5:
        return last(iterable)
    else:
        return first(rest(rest(rest(rest(iterable)))))
