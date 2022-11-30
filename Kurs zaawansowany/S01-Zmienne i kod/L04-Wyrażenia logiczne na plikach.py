import os

def linesAmount(path):
    with open(path, 'r') as file:
        x = len(file.readlines())
    return x

path = r'D:\Projekty\PyCharm\temp\L04.txt'

# if os.path.isfile(path):
#     amount = linesAmount(path)
#     print(amount)
# else:
#     print('Nie ma pliczku')

ok = os.path.isfile(path) and linesAmount(path)
print(ok)

## to niżej pogchamp

def CountWords(path):
    with open(path, 'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


# if os.path.isfile(path):
#     print("There are {} words in the file {}".format(CountWords(path), path))

os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))