class Animal: # животные
    alive = True # живой
    fed = False # накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}")


class Plant: # растения
    edible = False # съедобность
    def __init__(self, name):
        self.name = name


class Mammal(Animal): # млекопитающее
    pass

class Predator(Animal): # хищник
    pass

class Flower(Plant): # цветы
    pass

class Fruit(Plant): # фрукты
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)