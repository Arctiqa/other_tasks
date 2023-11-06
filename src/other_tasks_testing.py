from math import pi, sqrt
from typing import Optional


def sum_divisible_by_3_or_5(lst: list[int]) -> int:
    """
    Функция принимает на вход список чисел и возвращает сумму всех элементов списка, которые делятся на 3 или  5 без остатка.
    """
    result = 0
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


def check_email(email: str) -> bool:
    if email == '' or '@' not in email or '.' not in email:
        return False
    elif '@.' in email:
        return False
    elif email.find('@') > email.find('.'):
        return False
    elif email.count('@') > 1 or email.count('.') > 1:
        return False
    elif email.find('@') == 0 or email.find('.') == len(email) - 1:
        return False
    else:
        return True


def count_number_in_list(lst: list[int], num: int) -> int:
    return lst.count(num)


def calculate_area(shape: str, sides: list[int]) -> Optional:
    if shape.lower() in ['circle', 'круг']:
        return pi * sides[0] ** 2
    elif shape.lower() in ['square', 'квадрат']:
        return sides[0] ** 2
    elif shape.lower() in ['triangle', 'треугольник']:
        p = sum(sides) / 2
        a, b, c = sides
        return sqrt(p * (p - a) * (p - b) * (p - c))
    elif shape.lower() in ['rectangle', 'прямоугольник']:
        return max(sides) * min(sides)
    else:
        return None


def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_slice(a, -10, 7))
print(a[0:-6])