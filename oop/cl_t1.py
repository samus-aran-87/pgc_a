class Hero:
    def __init__(self,name,level,race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    
    def show_hero(self):
        discription = f"Hero name: {self.name} \
            \nLevel is: {self.level} \
            \nRace is:{self.race} \
            \nHealth is: {self.health}"
        print(discription)

    def lvl_up(self):
        self.level += 1
    
    def move(self):
        print(f"Hero name {self.name} start moving...")
    
    def set_heath(self, new_health):
        self.health = new_health
    

class SuperHero(Hero):
    def __init__(self,name,level,race,magic_level):
        super().__init__(name,level,race)
        self.magic_level = magic_level
        self.__magic = 100
    
    def use_magic(self):
        self.__magic -= 10

    def show_hero(self):
        discription = f"Hero name: {self.name} \
            \nLevel is: {self.level} \nRace is: {self.race} \
            \nHealth is: {self.health} \
            \nMagic is: {self.__magic}"
        print(discription)

myhero = Hero('Alex', 5, 'Human')
mysuperhero = SuperHero('Isaac', 10, 'Orc', 2)

myhero.show_hero()
print()
mysuperhero.show_hero()
mysuperhero.use_magic()
mysuperhero.use_magic()
mysuperhero.use_magic()
mysuperhero.lvl_up()
print()
mysuperhero.show_hero()