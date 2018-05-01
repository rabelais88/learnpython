class Human:
  def __init__ (self,name="noname"):
    self.name = name
    self.food = "nothing"
  def search(self,place):
    pass
  def take(self,food):
    self.food = food
  def open_mouth(self):
    pass
  def eat(self):
    print(self.name + " ate " + self.food)
  
  def __add__(self, other):
    return self.food + other.food

john = Human("john")
john.take("Banana")
john.eat()

jenny = Human()
jenny.eat()

print(john + jenny)

#inherited class
class Lawyer(Human):
  def __init__(self,name="noname"):
    super().__init__(name) # super().xxx => parent.xxx
    self.food = "expensive food"

kim = Lawyer()
kim.eat()


#static method inside class
class Blah:
  @staticmethod
  def saysomething():
    print('blahblah')

Blah.saysomething()