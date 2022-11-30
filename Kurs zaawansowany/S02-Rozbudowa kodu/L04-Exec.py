import os

paths = [r'D:\Projekty\PyCharm\temp\S02-L04\1.txt', r'D:\Projekty\PyCharm\temp\S02-L04\2.txt']



for path in paths:
    print(os.path.basename(path))
    with open(path, 'r') as file:
        exec(file.read())
        print('\n')
