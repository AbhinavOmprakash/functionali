"""A file containing useful predicates."""

from typing import List, Iterable, Callable, Any, Sequence, Union
from .higher_order_functions import partial, flip

def equals(a,b=None, *args):
    """

    Added in version: 0.1.0
    """

    if not b:
        return lambda x: x==a
    elif not args:
        return a==b
    else:
        # TODO ugly. refactor
        if a==b:
            for arg in args:
                if a != arg:
                    return False

            else:
                return True
        else:
            return False


def complement(
    expr: Union[bool, Callable[[Any], bool]]
) -> Union[bool, Callable[[Any], bool]]:
    """Takes in a predicate or a Boolean expression and
    returns a negated version of the predicate or expression.

    >>> not_(True)
    >>> False

    >>> def fn(el): # returns the Boolean of el
        return bool(el)
    >>> negated_fn = not_(fn)
    >>> fn(1)
    >>> True
    >>> negated_fn(1)
    >>> False

    Added in version: 0.1.0
    """

    if not isinstance(expr, Callable):
        # Wrapped around bool to handle cases like not_(1).
        # where 1 returns a boolean value of true.
        return not bool(expr)

    else:

        def negated(*args, **kwargs):
            return not expr(*args, **kwargs)

        return negated


def is_even(num: int) -> bool:
    """Returns true when num is even.
    Added in version: 0.1.0
    """
    return num % 2 == 0


def is_odd(num: int) -> bool:
    """Returns true when num is odd
    Added in version: 0.1.0
    """
    return num % 2 != 0


def is_prime(num: int) -> bool:
    """Returns true when num is prime
    Added in version: 0.1.0
    """
    if is_even(num) and num != 2:
        # You don't need to compute the whole Sieve if num is even.
        return False

    primes = [True for i in range(num + 1)]
    p = 2
    primes[0] = False
    primes[1] = False

    while p * p <= num:
        if primes[p] == True:
            # Update all multiples of p
            for i in range(p * 2, num + 1, p):
                primes[i] = False

        p += 1

    return primes[num]


def is_divisible(divident: Union[int, float], divisor: Union[int, float]) -> bool:
    """Returns true if dividend is divisible by divisor
    Added in version: 0.1.0
    """
    return divident % divisor == 0


def is_divisible_by(divisor: Union[int, float]) -> Callable[[Union[int, float]], bool]:
    """Takes a ``divisor`` And returns a function (closure) That expects a dividend.
    returns true if it passes the divisibility test.
    for e.g.

    >>> f = is_divisible_by(5)
    >>> f(10)
    True
    >>> f(7)
    False

    This is particularly useful to use with a filter.

    >>> list(filter(is_divisible_by(5), [1,2,3,4,5,6,7,8,9,10]))
    [5, 10]

    Suppose you want to filter out numbers that are divisible by 2 or 3

    >>> list(filter(some_predicates([is_divisible_by(2), is_divisible_by(3)]), range(1, 10)))
    [2, 3, 4, 6, 8, 9, 10]

    Added in version: 0.1.0
    """
    return lambda dividend: dividend % divisor == 0


def is_numeric(entity: Any) -> bool:
    """Return True if ``entity`` Is an ``int``,  ``float``, or a ``complex``.
    Added in version: 0.1.0
    """
    return any(map(isinstance, [entity, entity, entity], [int, float, complex]))


def is_atom(entity: Any) -> bool:
    """Everything that is NOT an iterable( except strings ) Are considered atoms.

    >>> is_atom("plain string")
        True
    >>> is_atom(1)
        True
    >>> is_atom([1, 2])
        False

    Added in version: 0.1.0
    """
    if isinstance(entity, str):
        return True
    else:
        return not isinstance(entity, Iterable)


def contains(entity: Any, collection: Iterable) -> bool:
    """Checks whether collection contains the given entity.
    Added in version: 0.1.0
    """
    return entity in collection


def is_empty(collection: Iterable) -> bool:
    """Returns true if the collection is empty.
    Added in version: 0.1.0
    """
    return not bool(collection)


def is_nested(collection: Iterable) -> bool:
    """return true if a collection is nested

    Added in version: 0.1.0
    """
    return any(map(complement(is_atom), collection))


def all_predicates(*predicates: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies all the predicates.

    Added in version: 0.1.0
    """
    return lambda entity: all((p(entity) for p in predicates))


def some_predicates(*predicates: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies some of the predicates.

    Added in version: 0.1.0
    """

    return lambda entity: any((p(entity) for p in predicates))
