# Python is an object oriented programming language.
#
# Almost everything in Python is an object, with its properties and methods.
#
# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
  x = 5
  def addtion(self,x):
	  return x + 10
  

objone = MyClass()
print(objone.x)
print(objone.addtion(15))