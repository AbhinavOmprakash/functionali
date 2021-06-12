"""A file containing useful predicates."""

from typing import List, Iterable, Callable, Any, Sequence, Union
from seq_transform import argzip

def not_(
    expr: Union[bool, Callable[[Any], bool]]
) -> Union[bool, Callable[[Any], bool]]:
    """Takes in a predicate or a Boolean expression and
    returns a negated version of the predicate or expression."""

    if not isinstance(expr, Callable):
        # Wrapped around bool to handle cases like not_(1).
        # where 1 returns a boolean value of true.
        return not bool(expr)

    else:

        def negated(*args, **kwargs):
            return not expr(*args, **kwargs)

        return negated


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_odd(num: int) -> bool:
    return num % 2 != 0


def is_prime(num: int) -> bool:
    pass


def is_divisible(divident: Union[int, float], divisor: Union[int, float]) -> bool:
    return divident % divisor == 0


def is_divisible_by(divisor: Union[int, float]) -> Callable[[Union[int, float]], bool]:
    """returns a closure that expects a number.
    for e.g.
    >>> f = is_divisible_by(5)
    >>> f(10)
    True
    >>> f(7)
    False

    This is particularly useful to use with a filter.
    >>> list(filter(is_divisible_by(5), [1,2,3,4,5,6,7,8,9,10]))
    [5, 10]
    You can still use a lambda, but I think this is more readable.

    Advanced example.
    Suppose you want to filter out numbers that are divisible by 2 or 3
    >>> list(filter(some_predicates([is_divisible_by(2), is_divisible_by(3)]),
                    [1,2,3,4,5,6,7,8,9,10]))
    [2, 3, 4, 6, 8, 9, 10]
    """
    return lambda dividend: dividend % divisor == 0


def is_numeric(entity: Any) -> bool:
    return any(map(isinstance, [entity, entity, entity], [int, float, complex]))


def contains(collection: Sequence, entity: Any) -> bool:
    """Checks whether collection contains the given entity."""
    return entity in collection


def is_empty(collection: Sequence) -> bool:
    """Returns true if the collection is empty."""
    return not bool(collection)

def is_nested(collection: Sequence) -> bool:
    return any( map( isinstance, argzip(collection, list)))

def all_predicates(
    predicates: Iterable[Callable[[Any], bool]]
) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies all the predicates.
    """
    return lambda entity: all((p(entity) for p in predicates))


def some_predicates(
    predicates: Iterable[Callable[[Any], bool]]
) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies some of the predicates.
    """

    return lambda entity: any((p(entity) for p in predicates))
