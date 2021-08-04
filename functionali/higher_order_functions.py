from typing import Callable, Any, Iterable
from inspect import signature
from functools import partial, reduce
from .seq_traverse import reversed_


def flip(fn: Callable) -> Callable:
    """returns a function that takes in a flipped order of args.
    Usage:

    >>> f = lambda a,b : a-b
    >>> f(1,3)
    -2
    >>> f(3,1)
    2
    >>> flipped_f = flip(f)
    >>> flipped_f(3,1)
    -2
    >>> flipped_f(1,3)
    2

    Added in version: 0.1.0
    """

    def flipped(*args, **kwargs):
        return fn(*reversed_(args), **kwargs)

    return flipped


def foldr(fn: Callable, iterable: Iterable, initial: Any = None) -> Any:
    """Fold right. Stack safe implementation

    Added in version: 0.1.0
    """
    # Implement with reduce, for this we reverse the iterable
    # and then we flip fn since the Function signature for fn is fn(element, accumulator)
    # This is the standard function signature of any function passed to Foldright
    # the flipping is necessary because reduce expects the reducing function to have a function signature of
    # fn(accumulator, element) Which is the opposite of fn(element, accumulator)
    reversed_it = reversed_(iterable)

    if initial is None:
        initial = next(reversed_it)

    return reduce(flip(fn), reversed_it, initial)


def comp(*fn: Callable):
    """
    returns a function composition of functions passed to comp.

    Added in version: 0.1.1
    """

    def inner(f, result):  # flipped order of args since you're passing to foldr
        return f(result)

    return lambda args: foldr(inner, fn, args)


def curry(fn: Callable) -> Callable:
    """Returns a curried version of the function.

    >>> def fn(arg1, arg2, arg3):  # test function
        return [arg1, arg2, arg3]
    >>> curried_fn = curry(fn)
    >>> curried_fn(1)(2)(3)
        [1, 2, 3]

    Added in version: 0.1.0
    """
    num_args = len(signature(fn).parameters)

    def curried(arg, fn, num_args):
        if num_args <= 1:
            # call fn if the final arg is passed
            return fn(arg)
        else:
            # call partial fn if not final arg
            f = partial(fn, arg)
            return lambda arg: curried(arg, f, num_args - 1)

    return lambda arg: curried(arg, fn, num_args)
