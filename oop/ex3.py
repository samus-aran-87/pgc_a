class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# pt = Point(1, 2)
# print(pt.x, pt.y)

# pt.x = 100
# pt.y = 100

# print(pt.x, pt.y)


class Points:
    WIDTH = 5
    __slots__ = ["__x", "__y", "z"]

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(other):
        if isinstance(other, (int, float)):
            return True
        else:
            return False

    def set_coords(self, x, y):
        if Points.__check_value(x) and Points.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print("x или y не я вляются int или float")

    def get_coords(self):
        return self.__x, self.__y

    # def __getattribute__(self, item):
    #     if item == "_Points__x":
    #         return "Частная перменная"
    #     else:
    #         return object.__getattribute__(self, item)
    #
    # def __setattr__(self, key, value):
    #     if key == "WIDTH":
    #         raise AttributeError
    #     else:
    #         self.__dict__[key] = value
    #
    # def __getattr__(self, item):
    #     print("__getattr__: " + item)
    #
    # def __delattr__(self, item):
    #     print(f"__delattr__: " + item)


# pts = Points(1, 2)

# print(pts.__x)
# print(pts.get_coords())
# pts.set_coords(10, '20')
# print(pts.get_coords())

# print(pts._Points__x, pts._Points__y)
# print(Points._Points__check_value(4))

# __setattr__
# __getattribute__
# __getattr__
# __delattr__

# print(pts.get_coords()) # __getattribute__(self, item)
# print(pts._Points__x)

# pts.WIDTH = 5 # def __setattr__(self, key, value)

# pts = Points(1, 2)
# pts.zzz
# pts.zzz = 1
# del pts.zzz

pt = Points(1, 2)
pt.z = 1
