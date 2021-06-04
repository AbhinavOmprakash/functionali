from pyfunc.predicates import (is_even, 
    is_odd, is_prime, is_numeric, all_predicates)


def test_is_even():
    assert is_even(2)== True
    assert is_even(3)== False

    
def test_is_odd():
    assert is_odd(3)== True
    assert is_odd(2)== False


def test_is_numeric():
    assert is_numeric(1)==True 
    assert is_numeric(1.253)==True     
    assert is_numeric(complex("1+2j"))==True 
    assert is_numeric("String")==False


def test_all_predicates():
    pass
    