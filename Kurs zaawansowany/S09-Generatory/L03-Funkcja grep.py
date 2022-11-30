import os, requests

# os.walk() - przechodzi rekurencyjnie przez katalogi i daje informacje o subkatalogach i plikach
# grep - funkcja szukania w systeamch operacyjnych

def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)

def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for i in f:
            yield i.replace('\n', '')

def check_webpage(url):
    try:
        u = requests.get(url)
        return u.status_code == 200
    except:
        return False


try:
    os.mkdir(r'D:\Projekty\PyCharm\temp\S09-L03')
except:
    pass

with open(r'D:\Projekty\PyCharm\temp\S09-L03\pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'D:\Projekty\PyCharm\temp\S09-L03\com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for f in gen_get_files(r'D:\Projekty\PyCharm\temp\S09-L03'):
    for l in gen_get_file_lines(f):
        # x = check_webpage(l)
        # x and print('{} - {} - True'.format(f, l))
        # not x and print('{} - {} - False'.format(f, l))
        print('{} - {} - {}'.format(f, l, check_webpage(l)))