def gen(products, promotions, customers):

    for i in products:
        for j in promotions:
            for k in customers:
                yield i, j, k


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = gen(products, promotions, customers)

# for c in combinations:
#     print(c)

print(next(combinations))
print(next(combinations))
print(next(combinations))
