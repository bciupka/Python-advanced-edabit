class noDuplicates:

    def __init__(self):
        self.list = []

    def __call__(self, newItems):
        for i in newItems:
            not i in self.list and self.list.append(i)

test = noDuplicates()

print(test.list)

test([1, 2, 3, 4, 1, 5, 3, 6])

print(test.list)

test([2, 3, 5, 7, 8])

print(test.list)
