class cake:

    known_types = ['cake', 'pie', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives=[], filling=""):
        self.name = name
        self.kind = kind if kind.lower() in self.known_types else 'Other'
        self.taste = taste
        self.additives = additives.copy() #lista jest mutable, przypominajka
        self.filling = filling
        self.bakery_offer.append(self) #cake.bakery_offer.append(self) - również działa

    def show_info(self):
        print(f'Name: {self.name.upper()}\nTaste: {self.taste}')
        print(f'Additives: {self.additives}') if len(self.additives) != 0 else False
        print(f'Filling: {self.filling}') if len(self.filling) != 0 else False
        print(30*'-')

    def set_filling(self, newFilling):
        self.filling = newFilling

    def add_additives(self, *newAdditives):
        self.additives.extend(newAdditives)


applepie = cake('Apple pie', 'ie', 'Fruity', ['Crumble'], 'Apple puree')
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese')
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate')

for i in cake.bakery_offer:
    i.show_info()

print(applepie.kind)

print(isinstance(cheesecake, cake))
print(type(chocolateuffin) is cake)
print(chocolateuffin.__class__)

print(vars(cake))
print(vars(applepie))
print(dir(cake))
print(dir(applepie))