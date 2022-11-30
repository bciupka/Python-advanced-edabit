ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# print(['{0:s} - {1:s}'.format(a,b) for a in ports for b in ports])
# print([(a,b) for a in ports for b in ports])

pairs = [(a,b) for a in ports for b in ports]
print(pairs)
print(len(pairs))

pairs = [(a,b) for a in ports for b in ports if a != b]
print(pairs)
print(len(pairs))

## ŹLE!!!

# pairs = [(a,b) for a in ports for b in ports if ports.index(a) % 2 == 0 and ports.index(b) % 2 == 1]
# print(pairs)
# print(len(pairs))



routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))

# porównywanie stringów odbywa się litera po literze z Unicodu, WAW WMI W==W A<M --> WAW<WMI