from functionali import (
    not_,
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


def test_not_():
    assert not_(False) == True
    assert not_(True) == False

    assert not_(0) == True
    assert not_(1) == False

    assert not_([]) == True
    assert not_([1, 2, 3]) == False

    # test negated functions.
    def fn(el):
        return bool(el)

    negated_fn = not_(fn)

    assert negated_fn(True) != fn(True)
    assert negated_fn(False) == fn(True)


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False


def test_is_odd():
    assert is_odd(3) == True
    assert is_odd(2) == False


def test_is_numeric():
    assert is_numeric(1) == True
    assert is_numeric(1.253) == True
    assert is_numeric(complex("1+2j")) == True
    assert is_numeric("String") == False


def test_all_predicates():
    pass
