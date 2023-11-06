import pytest
from src.other_tasks_testing import sum_divisible_by_3_or_5, check_email


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
                                             ('rewq@reqer.', False)])
def test_check_email_with_invalid_email(email, expected):
    assert check_email(email) is expected


def test_check_email_with_empty_email():
    assert check_email('') is False


