# 1

def wrap(fun):
    def func(*args, **kwargs):
        from datetime import datetime
        from datetime import timedelta
        start = datetime.now()
        x = fun(*args, **kwargs)
        stop = datetime.now()
        print('Wynik = {}\nWykonanie funkcji {} trwało {} sekundy'
              .format(x, fun.__name__, round(timedelta.total_seconds(stop-start), 2)))
    return func


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

wrapped = wrap(get_sequence)

wrapped(18)


# 2

import functools

def wrap2(fun):
    def newFun(*args, **kwargs):
        import time
        start = time.time()
        x = fun(*args, **kwargs)
        stop = time.time()
        print('Wykonanie funkcji {} trwało {} sekundy'.format(fun.__name__, round(stop-start, 2)))
        return x
    return newFun


@wrap2
def get_sequence2(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence2(i - 1) + get_sequence2(i)) / 2
        return v


# print(get_sequence2(18))