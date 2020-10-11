# Объекты-свойства (property)
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(x):
        if isinstance(x, (int, float)):
            return True
        else:
            return False

    def __get_coords(self):
        # print("Вызов __get_coords")
        return self.__x

    def __set_coords(self, x):
        # print("Вызов __set_coords")
        # self.__x = x
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных!")

    def __del_coords(self):
        print("Удаление свойства")
        del self.__x

    coords = property(__get_coords, __set_coords, __del_coords)


# pt = Point(1, 2)
# pt.coords = 100  # запись значения
# # pt.coords = "100"
# x = pt.coords  # чтение значения
# print(x)
# del pt.coords
# pt.coords = 7
# pt.coords


# Пример объявления свойств, через декораторы
class Pt:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(x):
        if isinstance(x, (int, float)):
            return True
        else:
            return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Pt.__check_value(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных!")

    @coordX.deleter
    def coordX(self):
        print("Удаление свойства")
        del self.__x

    # coordX = property(__get_coords, __set_coords, __del_coords)


# pt = Pt(1, 2)
# pt.coordX = 100  # запись значения
# x = pt.coordX  # чтение значения
# print(x)
# del pt.coordX
# pt.coordX = 7
# pt.coordX


# Пример объявления свойств, через дескрипторы
class CoordValue:
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value


class Points:
    # coordX = CoordValue("coordX")
    # coordY = CoordValue("coordY")
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt = Points(1, 2)
pt2 = Points(10, 20)
# pt.coordX = 5
print(pt.coordX, pt.coordY)
# print(id(pt.coordX), id(Points.coordX))
print(pt2.coordX, pt2.coordY)
