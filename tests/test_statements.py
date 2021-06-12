from functionali import if_, or_, and_


def test_if_():
    assert if_(True, 1, 2) == 1
    assert if_(False, 1, 2) == 2


def test_or_():
    assert or_(True, True, False) == True
    assert or_(True, False, False) == True
    assert or_("a" == "a", 5 % 5) == True

    assert or_(False, False, 0) == 0
    assert or_(0, 1, 2, 3, 4, 5) == 1
    assert or_(1, [1, 2, 3, 4, 5, 6, 7]) == 1
    assert or_([], [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_and_():
    assert and_(True, True, False) == False
    assert and_(True, True, 2) == 2
    assert and_(True, False, 2) == False
    assert and_(0, 1, 2, 3, 4, 5) == 0
    assert and_("a" == "a", 5 % 2) == 1
    assert and_(1, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert and_([], [1, 2, 3, 4, 5, 6, 7]) == []
