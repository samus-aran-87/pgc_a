class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def isDigit(self):
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            return True
        return False

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp:Point, ep:Point, color:str="red", width:int=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")


class Line(Prop):
    def drawLine(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def __setOneCoord(self, sp):
        if sp.isInt():
            self._sp = sp
        else:
            print("Координата должны быть целыми числами")

    def __setTwoCoord(self, sp, ep):
        if sp.isInt() and ep.isInt():
            Prop.setCoords(self, sp, ep)
        else:
            print("Координаты должны быть целыми числами")

    def setCoords(self, sp:Point, ep:Point=None):
        if ep is None:
            self.__setOneCoord(sp)
        else:    
            self.__setTwoCoord(sp, ep)


l = Line(Point(1,2),Point(10,20))
l.drawLine()
l.setCoords(Point(5,15))
# l.setCoords(Point(10.1,20),Point(100,200))
l.drawLine()

