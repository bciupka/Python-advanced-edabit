def num_grid(lst):
    import copy
    num = [-1, 0, 1]
    lstCopy = copy.deepcopy(lst) # kopiowanie tablic kilkuwymiarowych, zwykłe copy() czy slicing [:] nie działają
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '#':
                pass
            else:
                temp = []
                for k in range(3):
                    if i+num[k] < 0 or i+num[k] > len(lst) - 1:
                        continue
                    else:
                        x = lst[i+num[k]]
                    for l in range(3):
                        if j+num[l] < 0 or j+num[l] > len(lst[i]) - 1:
                            continue
                        else:
                            temp.append(x[j+num[l]])

                lstCopy[i][j] = str(temp.count('#'))
    return lstCopy


x = [
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-']
]


for i in x:
    print(i)
y = num_grid(x)
for i in y:
    print(i)

