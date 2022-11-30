import itertools


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


# canditate_list = []
# for i in range(1,10001):
#     canditate_list.append(i)



candidate_list = list(range(1, 10001)) # LEPSZY SPOSÓB!!!

filtered_list = itertools.filterfalse(lambda x: sum(get_factors(x)) != x, candidate_list)

for i in filtered_list:
    print('{}, dzielniki: {}'.format(i, get_factors(i)))


# not optimal:
prime_numbers = list(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10001)))
# print(prime_numbers)

print(prime_numbers[:10])

# optimal
prime_numbers = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000001)), 10)
print(list(prime_numbers))