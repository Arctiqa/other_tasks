def non_empty_truths(lst: list[list]) -> list:
    false_elems = [[], False, None, 0, '']
    new_lst = [[el for el in lst_0 if el not in false_elems] for lst_0 in lst if lst_0 not in false_elems]
    return new_lst


def is_int(x):
    return isinstance(x, int)


def each2d(test, matrix):
    result = all(test(i) for row in matrix for i in row)
    return result


def some2d(test, matrix):
    result = any(test(i) for row in matrix for i in row)
    return result


def sum2d(test, matrix):
    result = (i for row in matrix for i in row)
    return sum(filter(test, result))

# print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
#
# print((each2d(is_int, [[1, 2], [3, 4]])))
# # True
# print(each2d(is_int, [[1, None], [3, 4]]))
# # False
# # В пустой матрице нет ни одного элемента, который бы завалил тест
# print(each2d(is_int, []))
# # True
# print(some2d(is_int, [[None, "foo"], [(), {}]]))
# # False
# print(some2d(is_int, [[None, "foo"], [0, {}]]))
# # True
# # В пустой матрице нет ни одного элемента, который бы прошел тест
# print(some2d(is_int, []))
# # False
# print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))
# # 111
