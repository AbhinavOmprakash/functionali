"""higher order functions that consume other functions and return a modified function."""

from typing import Callable, Any
from inspect import signature
from functools import partial


def curry(fn: Callable) -> Callable:
    """Returns a curried version of the function."""
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


def flip(fn: Callable) -> Callable:
    """returns a function that takes takes in a flipped order of args.
    Usage:
    >>> flipped_fn = flip(fn)
    >>> # call flipped_fn with flipped args
    >>> flipped_fn(<flipped_args>)


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
    """

    def flipped(*args, **kwargs):
        return fn(*reversed(args), **kwargs)

    return flipped
