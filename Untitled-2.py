class Grandparent:
 height = 168
 age = 65
 
class Parent(Grandparent):
 height = 173
 age = 39  

class Child(Parent):
 height = 175
 age = 14
 def init(self):
    print(self.height)
    print(self.age)
 
mike = Child()