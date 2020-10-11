# полиморфизм в ООП на Python

class Rectangle:
    def __init__(self, w,h):
        self.w = w
        self.h = h
    
    def getPerAll(self):
        return 2*(self.w + self.h)
    

class Square:
    def __init__(self, a):
        self.a = a

    def getPerAll(self):
        return self.a * 4


class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getPerAll(self):
        return self.a + self.b + self.c

r1 = Rectangle(1,2)
r2 = Rectangle(3,4)
# print(r1.getPerRect(), r2.getPerRect())

s1 = Square(10)
s2 = Square(20)
# print(s1.getPerSq(), s2.getPerSq())

t1 = Triangle(1,2,3)
t2 = Triangle(4,5,6)
# print(t1.getPerTr(), t2.getPerTr())


# тут код до создания нового класса треугольник на 56 продолжение
# geom = [r1,r2,s1,s2]

# for i in geom:
#     print(i.getPerRect()) # тут будет ошибка по понятным причинам

# можно решить проблему выше добавлением проверок
# for i in geom:
#     if isinstance(i, Rectangle): 
#         print(i.getPerRect())
#     else:
#         print(i.getPerSq())


geom = [r1,r2,s1,s2,t1,t2] # после добавления треугольника также сново возникают ошибки
# for i in geom:
#     if isinstance(i, Rectangle): 
#         print(i.getPerRect())
#     else:
#         print(i.getPerSq())
# наша программа не имеет гибкости чтобы выполнить такое действие для этого воспользуемся полиморфизмом
# конечно можно вызвать еще проверок но это не лучшая практика

# далее поменяе метод который возвращает периметр на одинаков название во всех классах


# и так был изменены названия функций внутри классов которые возвращали периметр прямоугольника, квадрата, треугольника
# на одинаковое getPerAll

for i in geom:
    print(i.getPerAll()) # ошибка исчезла нам помог полиморфизм
