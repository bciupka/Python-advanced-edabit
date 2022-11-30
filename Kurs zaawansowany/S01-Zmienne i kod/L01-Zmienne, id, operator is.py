# 1

a = b = c = 10
print(a, b, c, id(a), id(b), id(c))
a = 20
print(a, b, c, id(a), id(b), id(c))

# 2

A = B = C = [1,2,3]
print(A, B, C, id(A), id(B), id(C))
A.append(4)
print(A, B, C, id(A), id(B), id(C))

# 3

x = 10
y = 10
print(id(x), id(y))
y = y-1+1
print(id(x), id(y))
y = y-1234567890+1234567890
print(id(x), id(y))
