class cake:
    def __init__(self, name, kind, taste, additives=[], filling=""):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy() #lista jest mutable, przypominajka
        self.filling = filling

applepie = cake('Apple pie', 'Pie', 'Fruity', ['Crumble'], 'Apple puree')
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese')
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate')

bakery_offer = [applepie, cheesecake, chocolateuffin]


print("Today's offer:\n")
for i in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {}, filled with {}\n'.format(i.name, i.kind, i.taste, i.additives, i.filling))

