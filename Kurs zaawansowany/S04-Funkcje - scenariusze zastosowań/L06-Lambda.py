text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)
print(f(text_list[2]), 2*'\n')
print(list(map(f, text_list)), 2*'\n')
print(list(map(lambda x: len(x), text_list)))

