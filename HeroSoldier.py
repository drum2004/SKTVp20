#Hero_Soldier
from random import randint

class Person:
    count=0
    def __init__(self,c):
        self.id=Person.count # уникальный номер объекта
        Person.count+=1
        self.command=c

class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.level=1
    def upLevel(self):
        self.level+=1 # метод увеличения собственного уровня

class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.my_hero=None
    def follow(self,hero): # следовать  "иду за героем"
        self.my_hero=hero.id
            
h1=Hero(1) # по одному герою для каждой команды
h2=Hero(2)

army1=[]
army2=[]
for i in range(20):
    n=randint(1, 2) 
    if n==1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))
if len(army1)>len(army2):
    h1.upLevel()
else:
    h2.upLevel()

army1[0].follow(h1)
print(army1[0].id, h1.id)



        