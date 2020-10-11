import math

#def area(r):
#    return math.pi * (r**2)

areaa = lambda r: math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10, 4.2]
areas = [areaa(r) for r  in radii]
print(areas)

t = list(map(lambda x: math.pi * (x**2), radii))
print(t)


temp = [('Berlin', 29), ('Cairo', 36), ('Buenos aires', 16), ('LA', 40), ('Tokyo', 12)]
c_to_f = lambda d: (d[0], (9/5)*d[1] + 32)
print(list(map(c_to_f, temp)))


import numpy as np
data = [1.3,2.7,0.8,4.1,4.3,-0.1]
mean = np.mean(data)
print(mean)

print(list(filter(lambda x: x > mean, data)))

ttes = ['','','123', 0]
print(list(filter(None, ttes)))

import functools
bb = [1,2,3,4,5]
print(functools.reduce(lambda x, y: x+y, bb))

# o = 0
# for i in bb:
#     o += i
#     print(o)

