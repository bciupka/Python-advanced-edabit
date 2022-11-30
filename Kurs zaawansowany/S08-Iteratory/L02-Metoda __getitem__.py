class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item > len(self.products)*len(self.promotions)*len(self.customers):
            raise StopIteration()
        pos_products = item // (len(self.promotions)*len(self.customers))
        item = item % (len(self.promotions)*len(self.customers))
        pos_promotions = item // len(self.customers)
        item = item % len(self.customers)
        pos_customers = item
        ret = (self.products[pos_products], self.promotions[pos_promotions], self.customers[pos_customers])
        return ret


products = ["Product {}".format(i) for i in range(1, 5)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 6)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 4)]
print(customers)


combinations = Combinations(products, promotions, customers)


for c in combinations:
    print(c)

print(combinations[5])

iterator = iter(combinations)

print(next(iterator))
print(next(iterator))
print(next(iterator))

