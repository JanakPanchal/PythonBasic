# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.

# def functionName(pr):
	#function body
    #return somevalue


student_name = ["Janak", "Rohan", "Imran","Rahul"]

def removeValue(value):
	value.pop()
	return value

for a in range(3):
	removeValue(student_name)
	
# removeValue(student_name)
# removeValue(student_name)
print(student_name)


def fullname(fname,lname):
	return "{} {}".format(fname,lname)
#
# print(fullname("Janak","Panchal"))

list_of_names = [
	{ "fname": "Janak" , "lname" : "Panchal" },
    { "fname": "Somil" , "lname" : "Gala" },
    { "fname": "Rahul" , "lname" : "Shah" },
]

#Janak Panchal
#Somil Gala
#Rahul Shah
for lof in list_of_names:
	print(fullname(lof["fname"],lof["lname"]))
