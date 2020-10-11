import re

text = "vasia@mail.ru, hello 123hello, \
    19727777, Vladimir 1999, Irina 1989, \
        eeee@yandex.ru, annn@intel.com, \
            Alex asdasda, tututu@giv.gav, 2020, \
                Sonia, Vasia"

"""
\d - any digit [0-9]
\D - any not digit [^0-9]
\w - any alpabet symbol [A-Za-z]
\W - any not alphabet symbol [^A-Za-z]
\s - breakspace
\S - not breakspace

[0-9]{3} - три числа подряд
[A-Z][a-z]+ - первая большая а дальше все с маленькой (неразравно)
\w+\@\w+\.\w+
"""

text_find = r"\w+\@\w+\.\w+"
all_results = re.findall(text_find, text)
print(all_results)

