import pytest

import intresting


@pytest.mark.parametrize("num1, num2, listres", [(1, 4, {1, 2, 3}), (1, 8, {1, 2, 3, 5, 7}), ('a', 4, {1, 3})])
def test_find_primes(num1, num2, listres):
    assert intresting.find_primes(num1, num2) == listres


@pytest.mark.parametrize("list_befor, list_after", [([1, 3, 8, 5], [1, 3, 5, 8])])
def test_sort_list(list_befor, list_after):
    assert intresting.sort_list(list_befor) == list_after


@pytest.mark.malka
def test_sort_list():
    assert intresting.sort_list([1, 3, 8, 5]) == [1, 3, 5, 8]


@pytest.mark.skip(reason="not interesting!!!")
def test_sort_list():
    assert intresting.sort_list([1, 3, 8, 5]) == [1, 3, 5, 8]
