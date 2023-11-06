from math import pi
import pytest
from src.other_tasks_testing import (sum_divisible_by_3_or_5, check_email,
                                     count_number_in_list, calculate_area, my_slice)


@pytest.mark.parametrize('lst, expected', [([3, 4, 5, 6, 7, 10], 24),
                                           ([1, 2, 3, 4, 5, 15, 21], 44),
                                           ([1, 4, 7, 8], 0),
                                           ([], 0)])
def test_sum_divisible_by_3_or_5(lst, expected):
    assert sum_divisible_by_3_or_5(lst) == expected


def test_check_email():
    assert check_email('rewq@afagads.dfd') is True


@pytest.mark.parametrize('email, expected', [('@trrqw.tre', False),
                                             ('fafdfa@.fdgfa', False),
                                             ('rsfgg.graa@gasd', False),
                                             ('rewq@reqer.', False),
                                             ('trww@fgs@gsd', False),
                                             ('qwer@rqt.tqt.tqwt', False)])
def test_check_email_with_invalid_email(email, expected):
    assert check_email(email) is expected


def test_check_email_with_empty_email():
    assert check_email('') is False


@pytest.fixture()
def lst_test():
    return [1, 2, 34, 5, 3, 5, 3, 2, 65, 43, 2, 34, 57, 5, 5, 0, 0, 0]


@pytest.fixture()
def number_for_count():
    return 5


def test_count_number_in_list(lst_test, number_for_count):
    assert count_number_in_list(lst_test, number_for_count) == 4


def test_count_number_in_empty_list(number_for_count):
    assert count_number_in_list([], number_for_count) == 0


def test_count_number_out_of_number(lst_test):
    assert count_number_in_list(lst_test, 90) == 0


@pytest.mark.parametrize('shape, sides, expected', [('Круг', [10], pi * 100),
                                                    ('rectangle', [3, 2, 3, 2], 6),
                                                    ('квадрат', [5], 25),
                                                    ('triangle', [5, 4, 3], 6),
                                                    ('another', [4, 2, 5], None)])
def test_calculate_area(shape, sides, expected):
    assert calculate_area(shape, sides) == expected


@pytest.fixture
def lst():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize('start, end, expected', [(3, 7, [4, 5, 6, 7]),
                                                  (-3, -7, []),
                                                  (-10, 7, [1, 2, 3, 4, 5, 6, 7]),
                                                  (5, None, [6, 7, 8, 9]),
                                                  (2, -3, [3, 4, 5, 6])])
def test_my_slice(lst, start, end, expected):
    assert my_slice(lst, start, end) == expected


def test_my_slice_empty_list():
    assert my_slice([], 3, 6) == []

