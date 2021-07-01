


class nameClass:
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = nameClass("John", 36)
print("Name : {}  Age {} ".format(p1.name,p1.age))

del p1

p2 = nameClass("Janak", 24)
print("Name : {}  Age {} ".format(p2.name,p2.age))



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Name : {}  Age {} ".format(self.name,self.age))
#
# p1 = Person("John", 36)
# p1.myfunc()

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#
