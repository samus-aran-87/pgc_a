import re

s = ['dfsdfdsf-12f2', '12', '23g-asd']

b = [sum([int(s) for s in re.findall('[0-9]+', i)]) for i in s]
print(b)


from itertools import groupby 
my_str = "hello 12d hi ad89--9999" 
l = [int(''.join(i)) for is_digit, i in groupby(my_str, str.isdigit) if is_digit]
print(l)





result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))

result = re.search(r'Analytics', 'AV Analytics Vidhya AV Analytics')
print(result.group(0))

