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

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling) #super(SpecialCake, self).__init__(...)
        self.ocasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print('Occasion: {}\nShape: {}\nOrnaments: {}\nText: {}'.format(self.ocasion, self.shape, self.ornaments, self.text))

birthday = SpecialCake('BD Cake', 'Pie', 'Lemon', ['coconut','chocolate'], 'Creamy', 'Birthday', 'Square', 'Red bows', 'Best wishes')
wedding = SpecialCake('Wed Cake', 'Cake', 'Fruity', [], 'Fresh', 'Wedding', 'High tower', 'Heart Stickers', 'Happy life together')

# birthday.show_info()
# wedding.show_info()

for i in SpecialCake.bakery_offer:
    print(i.full_name)
    i.show_info()