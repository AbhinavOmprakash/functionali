from functionali import (
    equals,
    is_,
    less_than,
    less_than_eq,
    greater_than,
    complement,
    is_even,
    is_odd,
    is_prime,
    is_numeric,
    is_divisible,
    is_divisible_by,
    is_numeric,
    is_atom,
    contains,
    is_empty,
    is_nested,
    all_predicates,
    some_predicates,
)

import pytest

def test_equals():
    assert equals(1)(1) == True
    assert equals(1,1) == True
    assert equals(1,1,1,1,1,1,1) == True
    
    assert equals(1)(2) == False
    assert equals(1,2) == False
    assert equals(1,1,1,1,1,1,2) == False
    assert equals(1,2,1,1,1) == False

def test_is_():
    assert is_(1)(1) == True
    assert is_(1,1) == True
    assert is_(1,1,1,1,1,1,1) == True

    assert is_({1:"a"})({1:"a"}) == False
    assert is_({1},{1},{1}) == False


def test_less_than():
    assert less_than(2)(1) == True
    assert less_than(1)(1) == False
    assert less_than(1, 2) == True
    assert less_than(1,2,3,4,5,6) == True

    assert less_than(1)(1) == False
    assert less_than(1,2,3,0) == False
    assert less_than(1,2,3,1) == False
    assert less_than(1,1,2,3) == False


def test_less_than_eq():
    assert less_than_eq(2)(1) == True
    assert less_than_eq(1)(1) == True
    assert less_than_eq(1, 2) == True
    assert less_than_eq(1,2,3,4,5,6) == True

    assert less_than_eq(1)(1) == True
    assert less_than_eq(1,2,3,0) == False
    assert less_than_eq(1,1,2,3) == True

def test_greater_than():
    assert greater_than(1)(2) == True
    assert greater_than(1)(1) == False
    assert greater_than(2, 1) == True
    assert greater_than(4,3,2,1) == True

    assert greater_than(1)(1) == False
    assert greater_than(4,3,2,4) == False
    assert greater_than(4,4,3,2) == False

def test_complement_():
    assert complement(False) == True
    assert complement(True) == False

    assert complement(0) == True
    assert complement(1) == False

    assert complement([]) == True
    assert complement([1, 2, 3]) == False

    # test negated functions.
    def fn(el):
        return bool(el)

    negated_fn = complement(fn)
    assert negated_fn(True) != fn(True)
    assert negated_fn(False) == fn(True)


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False


def test_is_odd():
    assert is_odd(3) == True
    assert is_odd(2) == False


def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(101) == True
    assert is_prime(150) == False


def test_is_divisible():
    assert is_divisible(4, 2) == True
    assert is_divisible(4, 3) == False

    with pytest.raises(ZeroDivisionError):
        is_divisible(4, 0)


def test_is_divisible_by():
    is_divisible_by_five = is_divisible_by(5)
    assert is_divisible_by_five(10) == True
    assert is_divisible_by_five(7) == False

    is_divisible_by_zero = is_divisible_by(0)
    with pytest.raises(ZeroDivisionError):
        is_divisible_by_zero(10)


def test_is_numeric():
    assert is_numeric(1) == True
    assert is_numeric(1.253) == True
    assert is_numeric(complex("1+2j")) == True
    assert is_numeric("String") == False


def test_is_atom():
    assert is_atom("plain string") == True
    assert is_atom(1) == True
    assert is_atom(1.2) == True

    assert is_atom([1, 2]) == False
    assert is_atom({1: "a"}) == False


def test_contains():
    assert contains(1, [1, 2]) == True
    assert contains(100, [1, 2]) == False
    assert contains(1, {1: "a"}) == True
    assert contains(2, {1: "a"}) == False


def test_is_empty():
    assert is_empty([]) == True
    assert is_empty([1]) == False


def test_is_nested():
    assert is_nested([]) == False
    assert is_nested([[]]) == True
    assert is_nested([(), ()]) == True


def test_all_predicates():
    is_even_and_prime = all_predicates(is_even, is_prime)

    assert is_even_and_prime(1) == False
    assert is_even_and_prime(2) == True
    assert is_even_and_prime(4) == False


def test_some_predicates():
    is_even_or_prime = some_predicates(is_even, is_prime)

    assert is_even_or_prime(1) == False
    assert is_even_or_prime(2) == True
    assert is_even_or_prime(3) == True
    assert is_even_or_prime(4) == True
