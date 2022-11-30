class Cake:
    '''Ta klasa jest sztosem'''
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        '''To robi klase'''

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

    @property
    def full_name(self):
        '''To wyświetla pełną nazwe klasy'''

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
print(30 * '-', '\n')
help(Cake.__init__)
print(30 * '-', '\n')
help(Cake.full_name)

# lol = Cake() i w nawiasie Ctrl + Q - wyświtla helpa (również dla metod itp.)