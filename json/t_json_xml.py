import json
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup as bs
from pprint import pprint

# json
with open('menu.json') as f:
    j = json.load(f)
    t = j['menu']['popup']['menuitem']
    # pprint(t)
    for i in t:
        # print(i)
        for k, v in i.items():
            if k == 'onclick':
                print(v)

print()
# xml
root = et.parse('menu.xml').getroot()
for i in root.findall('popup/menuitem'):
    # print(i.get('value'))
    print(i.get('onclick'))

print()
# xml
y = bs(open('menu.xml', 'r'), features="html.parser")
for i in y.menu.popup.findAll('menuitem'):
    print(i['onclick'])