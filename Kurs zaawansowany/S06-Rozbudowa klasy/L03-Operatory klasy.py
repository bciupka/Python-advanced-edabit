class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return 'Cake: {}, Kind: {}, Additives: {}'.format(self.name, self.kind, self.additives)

# 1

    # def __iadd__(self, *other):
    #     new = self.additives.copy()
    #     type(*other) == tuple and new.extend(*other)
    #     not type(*other) == tuple and new.append(*other)
    #     return Cake(self.name, self.kind, self.taste, new, self.filling)

# 2

    # def __iadd__(self, *other):
    #     new = self.additives.copy()
    #     type(*other) == tuple and new.extend([i for i in list(*other) if type(i) == str])
    #     type(*other) == str and new.append(*other)
    #     return Cake(self.name, self.kind, self.taste, new, self.filling)

# 3

    # def __iadd__(self, *other):
    #     print(type(*other))
    #     if type(*other) == tuple or type(*other) == list:
    #         x = 0
    #         for i in list(*other):
    #             x += 1 if type(i) == str else 0
    #         if x == len(*other):
    #             new = self.additives.copy()
    #             new.extend(*other)
    #             return Cake(self.name, self.kind, self.taste, new, self.filling)
    #         else:
    #             raise Exception('Zły typ zmiennej!!!')
    #     elif type(*other) == str:
    #         new = self.additives.copy()
    #         new.append(*other)
    #         return Cake(self.name, self.kind, self.taste, new, self.filling)
    #     else:
    #         raise Exception('Zły typ zmiennej!!!')

    def __iadd__(self, *other): #wersja bez .copy() działająca bezpośrednio na atrybucie instancji
        print(type(*other))
        if type(*other) == tuple or type(*other) == list:
            x = 0
            for i in list(*other):
                x += 1 if type(i) == str else 0
            if x == len(*other):
                self.additives.extend(*other)
                return self
            else:
                raise Exception('Zły typ zmiennej!!!')
        elif type(*other) == str:
            self.additives.append(*other)
            return self
        else:
            raise Exception('Zły typ zmiennej!!!')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

print(cake01)
cake01 += 'New'
print(cake01)
cake01 += ['More', 'Much more', 'Final']
print(cake01)
cake01 += 'One more', 'Try'
print(cake01)
cake01 += ('One tuple', 'For fun')
print(cake01)
# cake01 += "Again", 1
# print(cake01)
cake01 += ['Last', 2]
print(cake01)
