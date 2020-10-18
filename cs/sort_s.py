l = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']

l.sort()

print(l)

l.sort(key=lambda x: x[1], reverse=True)

print(l)

planet = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210)]

size = lambda p: p[1]

planet.sort(key=size)

print(planet[::-1])

#
sorted_l = sorted(l)

print(sorted_l)

data = (1,2,3,4,5,6,12,3,1,4,5,6)

print(sorted(data))

print(sorted("Test"))
