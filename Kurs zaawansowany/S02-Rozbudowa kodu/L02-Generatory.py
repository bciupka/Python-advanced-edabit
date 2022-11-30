ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# routes = [(start, stop) for start in ports for stop in ports]
# print(routes)
# print(len(routes))
#
# routes = [(start, stop) for start in ports for stop in ports if start != stop]
# print(routes)
# print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))


gen = ((start, stop) for start in ports for stop in ports if start < stop)

length = 0

for i in gen:
    print(i)
    length += 1
print(length)

# poniżej spec mode

gen = ((start, stop) for start in ports for stop in ports if start < stop)

length = 0

for i, y in gen:
    print(f'Połączenie z {i} do {y}')
    length += 1
print(length)



