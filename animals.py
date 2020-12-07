class Animals:#родительский класс Животные
    #методы
    def __init__(self,n,w,s,c,f): #название,вес,размер,цвет,питание,
        self.name=n
        self.weight=w
        self.size=s
        self.color=c
        self.feeds=f
    
    def show_info_animals(self):
        print(self.name,self.weight,self.size,self.color,self.feeds)    

#Добавляем объект newAnimal1       
#newAnimal1=Animals('bear','300kg', 'big', 'white', 'fish/meat')
#newAnimal1.show_info_animals()        

class Birds(Animals):#подкласс Птицы
    def get_bird(self,wings,feathers):
        self.wings=wings #крылья
        self.feathers=feathers #перья
    def show_bird(self):
        print(self.name,self.wings,self.feathers)
        
class Fishes(Animals):#подкласс Животные
    def get_fish(self,fins,scales):
        self.fins=fins #плавники
        self.scales=scales #чишуя
    def show_fish(self):
        print(self.fins,self.scales,self.color)

#объект для подкласса Птицы
Penguin=Birds('Пингвин','10 kg','королевский','белый','ананасы/люди')
Penguin.get_bird('несгибающиеся','как чещуя')
Penguin.show_bird()
#создать еще один объект для подкласса птицы

#создать два объекта для подкласса рыбы




        