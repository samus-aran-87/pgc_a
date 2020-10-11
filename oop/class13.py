# методы класса - @classmethod и статические методы - @staticmethod

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self,x,y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls,arg):
        if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x,y):
        return x*x + y*y


print(Vector.validate(5))
print(Vector.validate(500))
print(Vector.norm2(1,2))

# Но мы не можем обратиться к обычному методу класса \
# потому что там есть параметр self который должен ссылкаться на экземпляр класса
# Vector.setCoords(1,2) <= тут будет описанное выше

v = Vector() # а так сработает потому что появился экземпляр класса Vector
v.setCoords(1,2) 
Vector.setCoords(v, 10, 20)
