# НАСЛЕДОВАНИЕ

from random import randint

class Person:
    count = 0
    def __init__(self, c):
        self.id = Person.count # уникальный номер объекта
        Person.count += 1
        self.command = c
        
class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.level = 1
    def upLevel(self):
        self.level += 1  # метод увеличения собственного уровня

class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.my_hero = None
    def follow(self, hero):   # следовать  "иду за героем"
        self.my_hero = hero.id

h1 = Hero(1) # по одному герою для каждой команды
h2 = Hero(2)

army1 = []
army2 = []
for i in range(20):
    n = randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))        
    else:
        army2.append(Soldier(n))
    
#print ('army1 = ',army1 )
#print ('army2 = ',army2 )
        

    
print()
print("Армия 1-",len(army1), "Армия 2-",len(army2))
if len(army1) > len(army2):
    h1.upLevel()
else:
    h2.upLevel()
    
army1[0].follow(h1)
print('army1',army1[0].id, 'hero1',h1.id)

print('Уровень героев')    
print('H1', h1.id, 'Level H1',h1.level)
print('H2', h2.id, 'Level H2',h2.level)

print('# уникальный код солдатов army1 ')

for i in range (len(army1)):  # уникальный код солдатов 
    print(army1[i].id, army1[i].my_hero)
    

print('Количество экземпляров класса Person = ', Person.count)

