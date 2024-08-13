# duck typing

def drive(car):
    car.drive()    # object is deciding which class method to call.

class Creta:
    def drive(self):
        print('creta is driving')

class Mercedis:
    def drive(self):
        print('mercedes is driving')

c = Creta()
drive(c)


#

def petLover(pet):
    pet.talk()
    if hasattr(pet,'walk'):   #hasattr = if object doesnt has walk attribute than it will not call pet.walk()
        pet.walk()

class Duck:
    def talk(self):
        print('duck is talking')
    def walk(self):
        print('duck is walking')

class Cat:
    def talk(self):
        print('cat is talking')
    # def walk(self):
    #     print('cat is walking')

d = Duck()
petLover(d)

c = Cat()
petLover(c)
