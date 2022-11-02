import pytest
from rand_param import Prod_range

@pytest.fixture
def pr_3_2():
    return Prod_range([3, 2])


def test_prod_range_zeroth_item(pr_3_2):
    assert (pr_3_2.iget(0) == (0, 0))


def test_prod_range_first_item(pr_3_2):
    assert (pr_3_2.iget(1) == (0, 1))


def test_prod_range_negative_index(pr_3_2):
    assert (pr_3_2.iget(5) == pr_3_2.iget(-1))


@pytest.mark.parametrize("i,expected", [(2, (1, 0)), (3, (1, 1)), (4, (2, 0)), (5, (2, 1))])
def test_prod_items(pr_3_2, i, expected):
    assert pr_3_2.iget(i) == expected


def test_get_integer_too_high(pr_3_2):
    with pytest.raises(IndexError):
        pr_3_2.iget(6)


def test_Prod_range_len(pr_3_2):
    assert(len(pr_3_2) == 6)

@pytest.mark.skip
def test_noninteger_inputs():
    assert False
