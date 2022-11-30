import random

# 1

def KSI():
    for i in range(10):
        sweet = sour = salty = trials = 0
        while sweet + sour + salty != 100:
            sweet = random.randint(1, 100)
            sour = random.randint(1, 100)
            salty = random.randint(1, 100)
            trials += 1
        yield trials, [sweet, sour, salty]

mix = KSI()

for i in mix:
    print(i)

# 2

def random_with_sum(numberOfVal, assertedSum):
    trial = 0
    numbers = list(range(numberOfVal))
    while True:
        trial += 1
        for i in range(numberOfVal):
            numbers[i] = random.randint(1,100)
        if sum(numbers) == assertedSum:
            yield trial, numbers
            trial = 0


for i in range(10):
    (numberOfTrials, numbers) = next(random_with_sum(3, 100))
    print(numberOfTrials, numbers)