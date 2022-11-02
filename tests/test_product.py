import pytest
from rand_param import Product


def test_product_init():
    p = Product(['abc', '123'])
    assert (p[0] == ('a', '1'))
