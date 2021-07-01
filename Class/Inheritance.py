# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname ,age = None):
	  self.firstname = fname
	  self.lastname = lname
	  self.age = age

  def printname(self):
    print(self.firstname, self.lastname , self.age)


# x = Person("John", "Doe")
# x.printname()


class Student(Person):
	def __init__(self, fname, lname , age = None ):
		super().__init__(fname, lname , age )
		

x = Student("Mike", "Olsen" , 23)
x.printname()

y = Student("Mike", "Olsen" , 42)
y.printname()