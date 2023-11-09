from functools import wraps


def memoized(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


@memoized
def f(x):
    print('Calculating...')
    return x * 10


def memoizing(cache_len=3):
    def wrapper(func):
        cache = {}

        @wraps(func)
        def inner(arg):
            if arg in cache:
                return cache[arg]
            else:
                result = func(arg)
                if len(cache) >= cache_len:
                    first_key = next(iter(cache))
                    cache.pop(first_key)
                    cache[arg] = result
                    return result
                else:
                    cache[arg] = result
                    return result

        return inner

    return wrapper


@memoizing(cache_len=4)
def f(x):
    print('Calculating...')
    return x * 10


# print(f(1))
# print(f(2))
# print(f(3))
# print(f(1))
# print(f(3))
# print(f(4))
# print(f(1))
# print(f(5))
# print(f(4))
# print(f(4))
# print()
#
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(1))
# print(f(3))
# print(f(4))
# print(f(1))
# print(f(5))
# print(f(4))
# print(f(4))
# print(f(1))
# print(f(6))
