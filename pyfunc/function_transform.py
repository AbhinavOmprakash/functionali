"""higher order functions that consume other functions and return a modified function."""

from typing import Callable, Any
from inspect import signature


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


def partial(fn: Callable, *args, **kwargs) -> Callable:
    """Takes a function and fewer than normal arguments, and returns a function
    That will consume the remaining arguments and call the function"""

    def partial_fn(*rem_args, **rem_kwargs):
        return fn(*args, *rem_args, **kwargs, **rem_kwargs)

    return partial_fn

def flip(fn: Callable, *args, **kwargs) -> Any:
    """flips the order of *args"""
    return fn(*reversed(args), **kwargs)
