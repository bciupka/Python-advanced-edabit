class cake:

    known_types = ['cake', 'pie', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives=[], filling="", gluten_free = False):
        self.name = name
        self.kind = kind if kind.lower() in self.known_types else 'Other'
        self.taste = taste
        self.additives = additives.copy() #lista jest mutable, przypominajka
        self.filling = filling
        self.__gluten_free = gluten_free
        self.bakery_offer.append(self) #cake.bakery_offer.append(self) - również działa

    def show_info(self):
        print(f'Name: {self.name.upper()}\nTaste: {self.taste}\nGluten free: {self.__gluten_free}')
        print(f'Additives: {self.additives}') if len(self.additives) != 0 else False
        print(f'Filling: {self.filling}') if len(self.filling) != 0 else False
        print(30*'-')

    def set_filling(self, newFilling):
        self.filling = newFilling

    def add_additives(self, *newAdditives):
        self.additives.extend(newAdditives)


applepie = cake('Apple pie', 'Pie', 'Fruity', ['Crumble'], 'Apple puree', True)
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese', False)
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate', False)

for i in cake.bakery_offer:
    i.show_info()

cheesecake.__gluten_free = True

print(dir(cheesecake))
print(vars(cheesecake))

setattr(cheesecake, '_cake__gluten_free', True)
cheesecake.show_info()
cheesecake._cake__gluten_free = False
cheesecake.show_info()
