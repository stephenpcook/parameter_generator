import pytest
from rand_param import Prod_range


def test_prod_range_zeroth_item():
    pr = Prod_range([3, 2])
    assert (pr.iget(0) == (0, 0))


def test_prod_range_first_item():
    pr = Prod_range([3, 2])
    assert (pr.iget(1) == (0, 1))


@pytest.mark.parametrize("i,expected", [(2, (1, 0)), (3, (1, 1)), (4, (2, 0)), (5, (2, 1))])
def test_prod_items(i, expected):
    pr = Prod_range([3, 2])
    assert pr.iget(i) == expected

@pytest.mark.skip
def test_noninteger_inputs():
    assert False


@pytest.mark.skip
def test_get_integer_too_high():
    assert False
