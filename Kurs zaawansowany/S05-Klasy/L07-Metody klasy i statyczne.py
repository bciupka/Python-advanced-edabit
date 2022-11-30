import pickle
import os
import glob

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

    def save_to_file(self, path):
        file = os.path.join(path, self.name+'.bakery')
        with open(file, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_obj = pickle.load(f)
        cls.bakery_offer.append(new_obj)
        return new_obj

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(os.path.join(path, '*.bakery'))


    Text = property(__get_text, __set_text, None, 'trying to change text')

applepie = cake('Apple pie', 'Pie', 'Fruity', ['Crumble'], 'Apple puree', True, 'Najlepszego!')
cheesecake = cake('Cheesecake', 'Cake', 'Cheesy', ['Raisins', 'Powdered sugar'], 'Cottage cheese', False)
chocolateuffin = cake('Chocholate Muffin', 'Muffin', 'Sweet', ['Meringue'], 'White chocolate', False, 'Tutaj nie')

for i in cake.bakery_offer:
    i.show_info()

path = r'D:\Projekty\PyCharm\temp\S05-L07'
file = r'D:\Projekty\PyCharm\temp\S05-L07\Apple pie.bakery'


applepie.save_to_file(path)
cheesecake.save_to_file(path)

newApplepie = cake.read_from_file(file)

newApplepie.show_info()
print(vars(cake))
print(cake.get_bakery_files(path))

