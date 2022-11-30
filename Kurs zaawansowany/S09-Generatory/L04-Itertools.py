import itertools, math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
count = 0

for i in itertools.permutations(notes, 4): #wariacja bez powtórzeń (kolejność jest ważna), combinations (kolejnośc nie jest ważna)
    print(i)
    count += 1
print(count)

count1 = math.factorial(7)/math.factorial(7-4)
print(count1)

count = 0
for i in itertools.product(notes, repeat=4): #taka jakby zagnieżdżona pętla for - wariacja z powtórzeniami
    print(i)
    count += 1
print(count)

count1 = pow(7, 4) #pow jest też w math
print(count1)

# set - elementy nie mają kolejności, bez powtórzeń
