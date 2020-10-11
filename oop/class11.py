#функторы и менеджеры контекста

#функторы
class Counter:
    def __init__(self):
        self.__counter = 0
    
    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(self.__counter)
        return self.__counter

# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
    
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")

#         return args[0].strip(self.__chars)


def StripChars(chars):
    def stringStrip(string):
        if not isinstance(string, str):
            raise ValueError("Аргумент должен быть строкой")
        return string.strip(chars)
    return stringStrip

# s1 = StripChars("?:!.; ")
# print(s1(" Hello World! "))
# s2 = StripChars("?:!.; ")
# print(s2(" Hello? "))
# print(id(s1), id(s2), sep=' ')


#менеджеры контекста
# try:
#     with open("myfile.txt") as fp:
#         for t in fp:
#             print(t)
# except Exception as e:
#     print(e)


class DefenerVector:
    def __init__(self, v):
        self.__v = v
    
    def __enter__(self):
        self.__temp = self.__v[:] # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False

v1 = [1,2,3]
v2 = [1,2,3]
with DefenerVector(v1) as dv:
    for i in range(len(dv)):
        dv[i] += v2[i]

print(v1)

try:
    with open("myfile.txt") as fin:
        with open("out.txt") as fout:
            for line in fin:
                fout.write(line)
except Exception as e:





