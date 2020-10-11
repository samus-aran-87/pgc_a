class Clock:
    __DAY = 86400                       # число секунд в дне = 24*60*60
    
    def __init__(self, secs:int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")
        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60            # секунды
        m = (self.__secs // 60) % 60    # минуты
        h = (self.__secs // 3600) % 24  # часы
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0"+str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):             # s3 = s1 + s2
        if not (isinstance(other, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):            # s1 += s2
        if not (isinstance(other, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.__secs += other.getSeconds()
        return self

    def __eq__(self,other):               # True if s1 == s2 else False
        return self.__secs == other.getSeconds()

    def __nq__(self,other):               # True if s1 != s2 else False
        return not self.__eq__(other)

    def __getitem__(self,item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.__secs // 3600) % 24
        elif item == "min":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return self.__secs % 60

        return "Неверный ключ"

    def __setitem__(self,key,value):
        if not isinstance(key,str):
            raise ValueError("Ключ должен быть строкой")

        s = self.__secs % 60            # секунды
        m = (self.__secs // 60) % 60    # минуты
        h = (self.__secs // 3600) % 24  # часы

        if key == "hour":
            self.__secs = s + 60 * m + value * 3600
        elif item == "min":
            self.__secs = s + 60 * value + h * 3600
        elif item == "sec":
            self.__secs = value + 60 * m + h * 3600



s1 = Clock(200)
s2 = Clock(100)

# s3 = s1 + s2
# s4 = Clock(100)

# s5 = s1 + s2 + s4
# print(s5.getFormatTime())
# s9 = s1 + s2
# print(s9.getFormatTime())

# s1 += s2
# print(s1.getFormatTime())

# if s1 == s2:
#     print("Времена равны")

# if s1 != s2:
#     print("Времена не равны") 

# print(s1.getFormatTime())
# print(s1["hour"], s1["min"], s1["sec"])

# s1["hour"] = 10
# print(s1["hour"], s1["min"], s1["sec"])
