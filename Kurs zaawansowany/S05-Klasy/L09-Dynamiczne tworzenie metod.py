import csv
import types
import os

def export_1_cake_to_csv(obj, path):
    with open(path, 'w', newline='') as f: #newline zeby nie tworzyc podwojnych enterow
        writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerows([('Name', 'Kind', 'Taste', 'Additives', 'Filling'), (obj.name, obj.kind, obj.taste, obj.additives, obj.filling)])

def export_all_cakes_to_csv(cls, path):
    with open(path, 'w', newline='') as f: #newline zeby nie tworzyc podwojnych enterow
        writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(('Name', 'Kind', 'Taste', 'Additives', 'Filling'))
        for c in cls.bakery_offer:
            writer.writerow((c.name, c.kind, c.taste, c.additives, c.filling))

def export_this_cake_to_csv(self, path):
    with open(os.path.join(path, self.name.replace(' ', '_'))+'.csv', 'w', newline='') as f: #newline zeby nie tworzyc podwojnych enterow
        writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerows([('Name', 'Kind', 'Taste', 'Additives', 'Filling'), (self.name, self.kind, self.taste, self.additives, self.filling)])

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

# def export_all_cakes_to_html(cls, path):
#     template = """
# <table border=1>
#      <tr>
#        <th colspan=2>{}</th>
#      </tr>
#        <tr>
#          <td>Kind</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Taste</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Additives</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Filling</td>
#          <td>{}</td>
#        </tr>
# </table><br>"""
#
#     with open(path, "w") as f:
#         for c in cls.bakery_offer:
#             content = template.format(c.name, c.kind, c.taste, c.additives, c.filling)
#             f.write(content)

def export_all_cakes_to_html(cls, path): #opcja z jedna duza tabela  a nie z kilkoma po enterach
    template_header = """
<table border=1>"""
    template_data="""
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer="""</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(os.path.join(path, self.name.replace(' ', '_'))+'.html' , "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)



class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

path1 = r'D:\Projekty\PyCharm\temp\S05-L09\1cake.html'
path2 = r'D:\Projekty\PyCharm\temp\S05-L09\1cake.csv'

path3 = r'D:\Projekty\PyCharm\temp\S05-L09\allcakes.html'
path4 = r'D:\Projekty\PyCharm\temp\S05-L09\allcakes.csv'

path5 = r'D:\Projekty\PyCharm\temp\S05-L09'

export_1_cake_to_html(cake01, path1)
export_1_cake_to_csv(cake01, path2)

# export_all_cakes_to_html(Cake, path3)
Cake.cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.cakes_to_html(path3)

# export_this_cake_to_html(cake04, path5)
for i in Cake.bakery_offer:
    i.to_html = types.MethodType(export_this_cake_to_html, i)
    i.to_html(path5)

Cake.cakes_to_csv = types.MethodType(export_all_cakes_to_csv, Cake)
Cake.cakes_to_csv(path4)

for i in Cake.bakery_offer:
    i.to_csv = types.MethodType(export_this_cake_to_csv, i)
    i.to_csv(path5)