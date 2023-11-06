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



