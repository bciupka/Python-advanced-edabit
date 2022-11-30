class Cake: #https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
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

    def add_additives(self, additives):
        self.additives.extend(additives)

class noDuplicates:

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, cake, list):
        notUsed = []
        for i in list:
            not i in cake.additives and notUsed.append(i)
        return self.fun(cake, notUsed)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

@noDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)

cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts', 'shit'])
cake01.show_info()