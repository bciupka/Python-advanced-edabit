import time
import functools

# 1

@functools.cache  # lru_cache - starsza wersja ale z możliwością parametryzacji wielkośći i osobnego zapisu danych różnych typów (3 != 3.0)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for i in range(300):
    print('Fib od {} = {}'.format(i, fib(i)))
stop = time.time()
print(stop - start)
print(fib.cache_info())

# 2

# @functools.cache
def fib2(n):
    list = []
    for i in range(n+1):
        if i <= 2:
            list.append(i)
        else:
            list.append(list[i-2]+list[i-1])
    return list[n]

start = time.time()
for i in range(300):
    print('Fib od {} = {}'.format(i, fib2(i)))
stop = time.time()
print(stop - start)
# print(fib2.cache_info())