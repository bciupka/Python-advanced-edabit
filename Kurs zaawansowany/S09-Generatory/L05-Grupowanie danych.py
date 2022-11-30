import os, itertools

def scantree(path):
    for i in os.scandir(path):
        if os.path.isdir(i):
            yield i
            yield from scantree(i.path) # WAŻNA FUNKCJA DO ZAPAMIĘTANIA!!! przydatna do implementacji rekurencji
        else:
            yield i

# listing = scantree(r'D:\Projekty\PyCharm\temp')
#
# for i in listing:
#     print(i.is_dir(), i.path)

listing = scantree(r'D:\Projekty\PyCharm\temp')
listing = sorted(listing, key = lambda x: os.path.dirname(x))
for i, j in itertools.groupby(listing, key = lambda x: os.path.dirname(x)):
    print(i, len(list(j)))

listing = scantree(r'D:\Projekty\PyCharm\temp')
listing = sorted(listing, key = lambda x: x.is_dir())
for i, j in itertools.groupby(listing, key = lambda x: x.is_dir()):
    print('FOLDER' if i else 'FILE', len(list(j)))