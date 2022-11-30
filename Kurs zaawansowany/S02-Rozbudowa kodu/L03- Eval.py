import math

formula = input('Podaj wzór funkcji używając "x": ')


xs = []
i = 0

while i < 10:
    xs.append(i)
    i += 0.1

xs.sort()

# for x in xs:
#     y = eval(formula)
#     print('%.2f' % y)

for x in xs:
    print('%.2f' % eval(formula))
