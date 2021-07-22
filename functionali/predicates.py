"""A file containing useful predicates."""

from typing import List, Iterable, Callable, Any, Sequence, Union
from .higher_order_functions import partial, flip


def equals(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the``arg`` passed to it is equal
    to ``a``; else returns True when ``a``,``b`` and ``*args`` are equal.

    with one argument

    >>> equals_one = equals(1)
    >>> equals_one(1)
    True
    >>> equals_one(2)
    False

    with two or more arguments

    >>> equals(1,1,1)
    True
    >>> equals(1,1,2)
    False

    Added in version: 0.1.0
    """
    if not b:
        return lambda x: a == x
    elif not args:
        return a == b
    else:
        # TODO ugly. refactor
        if a == b:
            for arg in args:
                if a != arg:
                    return False
            else:
                return True
        else:
            return False


def is_(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the ``arg`` passed is the same object
    as ``a`` ; else returns True when ``a``,``b`` and ``*args`` are.

    with one argument

    >>> d1 = {1,2,3}
    >>> d2 = {1,2,3}
    >>> is_d1 = is_(d1)
    >>> is_d1(d2)
    >>> False
    >>> d1 == d2 
    >>> True

    with two or more arguments

    >>> is_(d1,d1)
    >>> True
    >>> is_(d1,d1,d2)
    >>> False


    Added in version: 0.1.0
    """
    if not b:
        return lambda x: a is x
    elif not args:
        return a is b
    else:
        # TODO ugly. refactor
        if a is b:
            for arg in args:
                if not a is arg:
                    return False
            else:
                return True
        else:
            return False


def less_than(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the ``arg`` passed to is less than ``a``;
    else returns True when ``a`` is less than``b`` and ``*args``.

    with one argument

    >>> less_than_one = less_than(1)
    >>> less_than_one(2)
    False
    >>> less_than_one(0)
    True


    with two or more arguments

    >>> less_than(1,2)
    >>> True
    >>> less_than(1,2,3)
    True
    >>> less_than(1,2,3,1)
    False

    Useful to use with filter

    >>> list(filter(less_than(5),range(10)))
    [0,1,2,3,4]

    Added in version: 0.1.0
    """
    if not b:
        return lambda x: x < a
    elif not args:
        return a < b
    else:
        # TODO ugly. refactor
        if a < b:
            for arg in args:
                if a >= arg:
                    return False
            else:
                return True
        else:
            return False


def less_than_eq(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the ``arg`` less than or equal to ``a``;
    else returns True when ``a`` is less than or equal to ``b`` and ``*args``.

    with one argument 

    >>> less_than_or_eq_to_one = less_than_eq(1)
    >>> less_than_or_eq_to_one(2)
    False
    >>> less_than_or_eq_to_one(1)
    True

    with two or more arguments

    >>> less_than_eq(1,2)
    >>> True
    >>> less_than_eq(1,2,3)
    True
    >>> less_than_eq(1,2,3,1)
    True

    Useful to use with filter

    >>> list(filter(less_than_eq(5),range(10)))
    [0,1,2,3,4,5]

    Added in version: 0.1.0
    """
    if not b:
        return lambda x: x <= a
    elif not args:
        return a <= b
    else:
        # TODO ugly. refactor
        if a <= b:
            for arg in args:
                if a > arg:
                    return False
            else:
                return True
        else:
            return False


def greater_than(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the ``arg`` passed to is greater than ``a``;
    else returns True when ``a`` is greater than``b`` and ``*args``.

    with one argument

    >>> greater_than_one = greater_than(1)
    >>> greater_than_one(2) 
    True
    >>> greater_than_one(0) 
    False

    with two or more arguments

    >>> greater_than(2,1)
    >>> True
    >>> greater_than(3,2,1)
    True
    >>> greater_than(3,2,1,3)
    False

    Useful to use with filter

    >>> list(filter(greater_than(5),range(10)))
    [6,7,8,9]

    Added in version: 0.1.0
    """
    if not b:
        return lambda x: x > a
    elif not args:
        return a > b
    else:
        # TODO ugly. refactor
        if a > b:
            for arg in args:
                if a <= arg:
                    return False
            else:
                return True
        else:
            return False


def greater_than_eq(a, b=None, *args):
    """
    if only ``a`` is passed, a function is returned that returns True when the ``arg`` greater than or equal to ``a``;
    else returns True when ``a`` is greater than or equal to ``b`` and ``*args``.

    with one argument 

    >>> greater_than_eq_one = greater_than_eq(1)
    >>> greater_than_eq_one(2) 
    True
    >>> greater_than_eq_one(1) 
    True

    with two or more arguments

    >>> greater_than_eq(2,1)
    >>> True
    >>> greater_than_eq(3,2,1)
    True
    >>> greater_than_eq(3,2,1,3)
    True

    Useful to use with filter

    >>> list(filter(greater_than_eq(5),range(10)))
    [5,6,7,8,9]

    Added in version: 0.1.0
    """
    if not b:
        return lambda x: x >= a
    elif not args:
        return a >= b
    else:
        # TODO ugly. refactor
        if a >= b:
            for arg in args:
                if a < arg:
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

    >>> complement(True)
    >>> False

    >>> def fn(el): # returns the Boolean of el
        return bool(el)
    >>> negated_fn = complement(fn)
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
    """Returns true if dividend is divisible by divisor.
    
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
    """returns true if a collection is nested

    Added in version: 0.1.0
    """
    return any(map(complement(is_atom), collection))


def all_predicates(*predicates: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies all the predicates.

    >>> even_and_prime = all_predicates(is_even, is_prime)
    >>> even_and_prime(2)
    True
    >>> even_and_prime(4)
    False
    >>> even_and_prime(3)
    False

    Added in version: 0.1.0
    """
    return lambda entity: all((p(entity) for p in predicates))


def some_predicates(*predicates: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """Takes a set of predicates and returns a function that takes an entity
    and checks if it satisfies some of the predicates.

    >>> even_or_prime = some_predicates(is_even, is_prime)
    >>> even_or_prime(2)
    True
    >>> even_and_prime(4)
    True
    >>> even_and_prime(3)
    True

    Added in version: 0.1.0
    """

    return lambda entity: any((p(entity) for p in predicates))
