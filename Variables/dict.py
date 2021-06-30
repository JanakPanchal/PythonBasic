# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

#dict()
#{}
student = dict(
	#key = value
	name = "Janak",
	lastname = "panchal",
     colors =  ["red", "white", "blue"]
)

print(student)
print(student["name"])
print(student["colors"])

student["typeofjob"] = "Prog"
print(student)

#updating value
student.update({"hometown" : "mumbai"})
print(student)

details  = {
	"name" : "Janak",
	"lastname" : "panchal",
     "colors" : ["red", "white", "blue"]
}

print(details)

for x  in student.values():
  print("{}".format(x))
  
for x  in student.keys():
  print("{}".format(x))
  
for x , y in student.items():
	print(" key {}  value {}".format(x , y))

z = student.copy()
print(student)
print(z)
