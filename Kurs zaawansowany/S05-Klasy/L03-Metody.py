class cake:
    def __init__(self, name, kind, taste, additives=[], filling=""):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy() #lista jest mutable, przypominajka
        self.filling = filling

    def show_info(self):
        print(f'Name: {self.name.upper()}\nTaste: {self.taste}')
        print(f'Additives: {self.additives}') if len(self.additives) != 0 else False #None również działa
        print(f'Filling: {self.filling}') if len(self.filling) != 0 else False
        print(30*'-')

    def set_filling(self, newFilling):
        self.filling = newFilling

    def add_additives(self, *newAdditives):
        self.additives.extend(newAdditives)


applepie = cake('Apple pie', 'Pie', 'Fruity', ['Crumble'], 'Apple puree')
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese')
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate')

bakery_offer = [applepie, cheesecake, chocolateuffin]

cheesecake.show_info()

chocolateuffin.set_filling('Crushed Nesquik')
chocolateuffin.show_info()

applepie.add_additives('Vanilla Ice Cream', 'Whipped Cream')
applepie.show_info()
