banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]


dict_denominations = {}
for i in banknotes_coins:
    dict_denominations.setdefault(i,0)

print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for i, j in zip(dict_denominations.keys(),dict_denominations.values()):
    if j != 0:
        print('Denominate: {0:6.2f} - amount {1:5d}'.format(i, j))
    else:
        print('No %4.2f denominate' % i)


print(2*'\n', 30*'-', 2*'\n')

for i in dict_denominations:
    if dict_denominations[i] != 0:
        print('Denominate: {0:6.2f} - amount {1:5d}'.format(i, dict_denominations[i]))
    else:
        print('No %4.2f denominate' % i)
