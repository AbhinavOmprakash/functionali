""" Functions to traverse the sequence"""
from collections import deque
from typing import Iterable, Any, TypeVar, Iterator, Tuple, Mapping, Union

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def iter_(iterable: Iterable) -> Iterator:
    """Returns appropriate iterator for the given iterable.
    If iterable is already an iterator, it is returned as is.
    This is mainly created because python's `iter` 
    returns an iterable of keys instead of keys and values.
    """

    if isinstance(iterable, dict):
        # since iter(dict) returns a tuple of keys.
        # I want a tuple of key-value pairs
        return iter(iterable.items())

    elif not isinstance(iterable, Iterator):
        return iter(iterable)

    else:  # if iterable is already an iterator
        return iterable


def first(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    Returns the first item in an iterable.
    If iterable is a dict, returns a tuple of the First key-value pair
    >>> first([1,2,3,4,5])
    1
    >>> first({1:"a", 2:"b"})
    (1, "a")
    """
    if iterable:
        return next(iter_(iterable))

    else:  # If iterable is empty
        return None


def ffirst(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """same as first(first(iterable))
    expects a nested iterable."""

    return first(first(iterable))


def last(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    >>> last([1,2,3,4])
    4
    >>> last({1: 'a', 2: 'b', 3: 'c'})
    (3, "c")
    """
    try:
        # using a deque is an efficient way to get the last element
        dq = deque(iter_(iterable), maxlen=1)

        return dq.pop()

    except IndexError:  # If iterable is empty, dq is empty
        return None


def rest(iterable: Iterable) -> Iterator:
    """
    Returns an iterator of all but the first element in the iterable.
    If iterable is empty it returns an empty iterator.

    >>> list(rest([1,2,3,4,5]))
    [2, 3, 4, 5]

    >>> tuple(rest({1:"a", 2:"b", 3:"c"}))
    ((2,"b"), (3, "c"))

    >>> tuple(rest([]))
    ()
    """
    try:
        it = iter_(iterable)
        next(it)  # discard value
        return it

    except StopIteration:  # If iterable is empty
        return iter([])


def second(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    >>> second([1,2,3,4,5])
    2
    """
    if len(iterable) < 2:
        return last(iterable)
    else:
        return first(rest(iterable))


def third(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    >>> third([1,2,3,4,5])
    3
    """
    if len(iterable) < 3:
        return last(iterable)
    else:
        return first(rest(rest(iterable)))


def fourth(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    >>> fourth([1,2,3,4,5])
    4
    """
    if len(iterable) < 4:
        return last(iterable)
    else:
        return first(rest(rest(rest(iterable))))


def fifth(iterable: Union[Iterable[T], Mapping[K, V]]) -> Union[T, Tuple[K, V]]:
    """
    >>> fifth([1,2,3,4,5])
    5
    """
    if len(iterable) < 5:
        return last(iterable)
    else:
        return first(rest(rest(rest(rest(iterable)))))


def butlast(
    iterable: Union[Iterable[T], Mapping[K, V]]
) -> Union[Tuple[T], Tuple[K, V]]:
    """returns an iterable of all but the last element
    in the iterable

    """
    # TODO Check efficiency of the operation
    # since it's iterating through it twice.
    t = tuple(iter_(iterable))[:-1]
    if t:
        return t
    else:
        return None


def take(n: int, iterable: Iterable) -> Tuple:
    """Returns the first n number of elements in iterable.
    Returns an empty tuple if iterable is empty
    >>> take(3, [1,2,3,4,5])
    (1, 2, 3)
    >>> take(2, {1: "a", 2: "b", 3: "c"})
    ((1, "a"), (2, "b"))
    """
    it = iter_(iterable)

    accumulator = []
    i = 1
    while i <= n:
        try:
            accumulator.append(next(it))
            i += 1
        except StopIteration:
            break

    return tuple(accumulator)


def drop(n: int, iterable: Iterable) -> Tuple:
    """Returns All the Elements after the first
    n number of elements in iterable.
    Returns an empty tuple if iterable is empty

    >>> drop(3, [1,2,3,4,5])
    (4,5)
    >>> drop(2, {1: "a", 2: "b", 3: "c"})
    ((3, "c"),)
    """

    it = iter_(iterable)

    i = 1
    while i <= n:
        try:
            next(it)  # discard values
            i += 1
        except StopIteration:
            break

    return tuple(it)

def take_while(predicate: Callable, iterable: Iterable) -> Tuple:
    """

    >>> take_while(is_even, [2,4,6,7,8,9,10])
    (2,4,6)

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> take_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((2, "a"), (4, "b"))
    """

    if isinstance(iterable, dict):
        it = iter(iterable.items())
    else:
        it = iter(iterable)

    accumulator = []
    elem = next(it)
    while predicate(elem):
        accumulator.append(elem)
        elem = next(it)

    return tuple(accumulator)


def drop_while(predicate: Callable, iterable: Iterable) -> Tuple:
    """

    >>> drop_while(is_even, [2,4,6,7,8,9,10])
    (7,8,9, 10)

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> drop_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((5, "c"),)
    """

    if isinstance(iterable, dict):
        it = iter(iterable.items())
    else:
        it = iter(iterable)

    elem = next(it)
    while predicate(elem):
        # discard values
        elem = next(it)

    # Since elem is the first element
    # that fails the predicate.
    # and the iterator has already moved ahead.
    # we need to include elem
    return (elem,) + tuple(it)


def split_with(predicate: Callable, iterable: Iterable) -> Tuple[Tuple]:
    # consider implementing with reduce
    # since we are iterating through iterable twice.
    return (take_while(predicate, iterable), drop_while(predicate, iterable))
