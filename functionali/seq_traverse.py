""" Functions to traverse the sequence"""
from collections import deque
from typing import Iterable, Any, TypeVar, Iterator, Tuple, Mapping, Union, Callable


def iter_(iterable: Iterable) -> Iterator:
    """Returns appropriate iterator for the given iterable.
    If iterable is already an iterator, it is returned as is.
    This is mainly created because python's ``iter``
    returns an iterable of keys instead of keys and values for ``dict``.

    >>> tuple(iter_({1: "a", 2: "b", 3: "c"}))
    ((1, "a"),(2, "b"), (3, "c"))

    Added in version: 0.1.0
    """

    if isinstance(iterable, dict):
        # since iter(dict) returns a tuple of keys.
        # I want a tuple of key-value pairs
        return iter(iterable.items())

    elif not isinstance(iterable, Iterator):
        return iter(iterable)

    else:  # if iterable is already an iterator
        return iterable


def reversed_(iterable: Iterable) -> Iterator:
    """Returns appropriate reversed iterator for the given iterable.
    If iterable is already an iterator, it is returned as is.
    This is mainly created because python's ``reversed``
    returns an iterable of keys instead of keys and values for ``dict``.

    >>> tuple(reversed_({1: "a", 2: "b", 3: "c"}))
    ((3, 'c'), (2, 'b'), (1, 'a'))

    Added in version: 0.1.0
    """
    if isinstance(iterable, dict):
        # since iter(dict) returns a tuple of keys.
        # I want a tuple of key-value pairs
        return reversed(iterable.items())

    elif not isinstance(iterable, Iterator):
        return reversed(iterable)

    else:  # if iterable is already an iterator
        return iterable


def first(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """
    Returns the first item in an iterable.
    If iterable is a dict, returns a tuple of the First key-value pair

    >>> first([1,2,3,4,5])
    1
    >>> first({1:"a", 2:"b"})
    (1, "a")

    Added in version: 0.1.0
    """

    if iterable:
        return next(iter_(iterable))

    else:  # If iterable is empty
        return None


def ffirst(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """same as ``first(first(iterable))``
    expects a nested iterable.

    >>> ffirst([[1,2], [3,4], [5,6]])
    1

    Added in version: 0.1.0
    """

    return first(first(iterable))


def last(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """
    returns the last element in the iterable.

    >>> last([1,2,3,4])
    4
    >>> last({1: 'a', 2: 'b', 3: 'c'})
    (3, "c")

    Added in version: 0.1.0
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

    Added in version: 0.1.0
    """
    try:
        it = iter_(iterable)
        next(it)  # discard value
        return it

    except StopIteration:  # If iterable is empty
        return iter([])


def second(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """ Returns the second item in iterable, or the last item if length is less than 2
    >>> second([1,2,3,4,5])
    2

    Added in version: 0.1.0
    """
    if len(iterable) < 2:
        return last(iterable)
    else:
        return first(rest(iterable))


def third(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """ Returns the third item in iterable, or the last item if length is less than 3 
    >>> third([1,2,3,4,5])
    3

    Added in version: 0.1.0
    """
    if len(iterable) < 3:
        return last(iterable)
    else:
        return first(rest(rest(iterable)))


def fourth(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """ Returns the fourth item in iterable, or the last item if length is less than 4
    >>> fourth([1,2,3,4,5])
    4

    Added in version: 0.1.0
    """
    if len(iterable) < 4:
        return last(iterable)
    else:
        return first(rest(rest(rest(iterable))))


def fifth(iterable: Union[Iterable, Mapping[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
    """ Returns the fifth item in iterable, or the last item if length is less than 5
    >>> fifth([1,2,3,4,5])
    5

    Added in version: 0.1.0
    """
    if len(iterable) < 5:
        return last(iterable)
    else:
        return first(rest(rest(rest(rest(iterable)))))


def butlast(
    iterable: Union[Iterable, Mapping[Any, Any]]
) -> Union[Tuple[Any], Tuple[Tuple[Any, Any]]]:
    """returns an iterable of all but the last element
    in the iterable

    >>> butlast([1, 2, 3])
    (1, 2)

    Added in version: 0.1.0
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

    Added in version: 0.1.0
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

    Added in version: 0.1.0
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
    Constructs a iterable list by taking elements from ``iterable`` while ``predicate`` is true,
    Stop taking after the first element falsifies the predicate.


    >>> take_while(is_even, [2,4,6,7,8,9,10])
    (2,4,6) # Notice that it does not include 8 and 10

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> take_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((2, "a"), (4, "b"))

    Added in version: 0.1.0
    """

    it = iter_(iterable)

    accumulator = []
    elem = next(it)
    while predicate(elem):
        accumulator.append(elem)
        elem = next(it)

    return tuple(accumulator)


def drop_while(predicate: Callable, iterable: Iterable) -> Tuple:
    """
    Drops elements from ``iterable`` while ``predicate`` is true, 
    And returns a tuple of the remaining elements in ``iterable``.

    >>> drop_while(is_even, [2,4,6,7,8,9,10])
    (7,8,9, 10)

    >>> def is_even_dict(d):
            #checks if the key of dict d is even
            return d[0]%2==0
    >>> drop_while(is_even_dict, {2:"a", 4:"b",5:"c"})
        ((5, "c"),)

    Added in version: 0.1.0
    """

    it = iter_(iterable)

    elem = next(it)
    while predicate(elem):
        # discard values
        elem = next(it)

    # Since elem is the first element
    # that fails the predicate.
    # and the iterator has already moved ahead.
    # we need to include elem
    return (elem,) + tuple(it)


def split_with(predicate: Callable, iterable: Iterable) -> Tuple[Tuple, Tuple]:
    """Equivalent to ``(take_while(predicate, iterable), drop_while(predicate, iterable))``

    >>> split_with(is_even, [2, 4, 6, 7, 8, 9, 10])
    ((2, 4, 6), (7, 8, 9, 10))

    Added in version: 0.1.0
    """
    # consider implementing with reduce
    # since we are iterating through iterable twice.
    return (take_while(predicate, iterable), drop_while(predicate, iterable))
