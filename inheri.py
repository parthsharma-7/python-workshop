##inheritance:allows you to create new classes that inherit properties amd methods from existing classes## 
class Animal:
  def __init__(self,name):
    self.name=name
  def speak(self):
    pass
class Dog(Animal):
 def speak (self):
   return"wooff"
class Cat(Animal):
 def speak (self):
   return"yeah daddy"
dog=Dog("buddy")
cat=Cat("ahh fuck me")
print(dog.name,dog.speak())
print(cat.name,cat.speak())