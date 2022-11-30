import os
import urllib.request

output = r'D:\Projekty\PyCharm\temp\L06'

pages = [{ 'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
        { 'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'},
        { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' }]

for i in pages:
    try:
        path = os.path.join(output,i['name']+'.html')
        urllib.request.urlretrieve(i['url'], path)
        print(f'Strona {i["name"]} dodana')
    except:
        print('Koniec przetwarzania - BŁĄD')
        break
else:
    print('Udało się')

