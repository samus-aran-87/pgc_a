class Point:
    # def __init__(self):
    #     print("Создание экземпляра класса Point")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Удаление экземпляра: {self.__str__()}")

    x = 1
    y = 1

    def set_coords(self, x, y):
        self.x = x
        self.y = y


# pt = Point()
# Point.set_coords(pt, 5, 10)
# pt.set_coords(5, 10)

pt = Point()
pt1 = Point(5)
pt2 = Point(5, 10)
print(pt.__dict__, pt1.__dict__, pt2.__dict__)
