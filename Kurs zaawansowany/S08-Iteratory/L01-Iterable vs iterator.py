import time

# funkcja iter() - pozwala na przejście przez obiekt nie będący iteratorem (nie zawsze się sprawdza), dobrze radzi sobie z metodą getitem

# iterator - __next__/iter(), iterable - __iter__/__getitem__
class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotions = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotions +=1
        if self.current_promotions >= len(self.promotions):
            self.current_promotions = 0
            self.current_product +=1
        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()
        ret = (self.products[self.current_product], self.promotions[self.current_promotions], self.customers[self.current_customer])
        self.current_customer += 1
        return ret

    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)

# combinations = []
#
# for i in products:
#     for j in promotions:
#         for k in customers:
#             combinations.append("{} - {} - {}".format(i, j, k))

combinations = Combinations(products, promotions, customers)


for c in combinations:
    pass

