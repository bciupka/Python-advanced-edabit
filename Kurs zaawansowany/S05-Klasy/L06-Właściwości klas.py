class cake:

    known_types = ['cake', 'pie', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives=[], filling="", gluten_free = False, text = ''):
        self.name = name
        self.kind = kind if kind.lower() in self.known_types else 'Other'
        self.taste = taste
        self.additives = additives.copy() #lista jest mutable, przypominajka
        self.filling = filling
        self.__gluten_free = gluten_free
        self.__text = text if self.kind.lower() == 'pie' or self.kind.lower() == 'cake' else ''
        self.bakery_offer.append(self) #cake.bakery_offer.append(self) - również działa

    def show_info(self):
        print(f'Name: {self.name.upper()}\nTaste: {self.taste}\nGluten free: {self.__gluten_free}')
        print(f'Additives: {self.additives}') if len(self.additives) != 0 else False
        print(f'Filling: {self.filling}') if len(self.filling) != 0 else False
        print(f'Text: {self.__text}') if len(self.__text) != 0 else None
        print(30*'-')

    def set_filling(self, newFilling):
        self.filling = newFilling

    def add_additives(self, *newAdditives):
        self.additives.extend(newAdditives)

    def __get_text(self):
        return self.__text

    def __set_text(self, newText):
        self.__text = newText if self.kind.lower() == 'pie' or self.kind.lower() == 'cake' else ''

    Text = property(__get_text, __set_text, None, 'trying to change text')

applepie = cake('Apple pie', 'Pie', 'Fruity', ['Crumble'], 'Apple puree', True, 'Najlepszego!')
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese', False)
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate', False, 'Tutaj nie')

for i in cake.bakery_offer:
    i.show_info()

chocolateuffin.Text = 'Znowu nie'
print(vars(chocolateuffin))

cheesecake.Text = 'A tutaj tak'
print(vars(cheesecake))

applepie.Text = ''
for i in cake.bakery_offer:
    i.show_info()

