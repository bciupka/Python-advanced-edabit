colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def slice(list, n):
    return list[:n]

print(slice(colors, 4))

for i in range(len(colors)):
    print(colors[:i+1])

for i in range(1,len(colors)+1):
    print(slice(colors, i))



text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod ' \
       'przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji ' \
       'pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania ' \
       'człowieka w imię postępu. Rządzi w niej prawo dżungli.'

# print(text)

print(text[text.index('(') + 1:text.index(')')])


text = text.replace(text[text.index('(') + 1:text.index(')')], '')

print(text)

