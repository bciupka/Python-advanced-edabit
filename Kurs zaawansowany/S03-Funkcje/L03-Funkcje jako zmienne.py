def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

number = 8

transformations = ([double, root, div2, negative], [root, root, div2, double])

# transformations2 = [(double, root, div2, negative), (root, root, div2, double)] # też śmiga

for i in transformations:
    tmp_return_value = number
    for fun in i:
        tmp_return_value = fun(tmp_return_value)
        print(tmp_return_value)


