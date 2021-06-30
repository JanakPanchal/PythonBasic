# Tuples are used to store multiple items in a single variable.
#
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#
# A tuple is a collection which is ordered and unchangeable.
#
# Tuples are written with round brackets


# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

#()
#example of taple
thistuple = ("apple", "banana", "cherry", ["1","Name"], 1 )
print(thistuple)
print(len(thistuple))
print(thistuple[1])
print(thistuple[1:3])
print(list(thistuple))

y = list(thistuple)
y = ["Janak", "Rohan","Somil"]
thistuple = tuple(y)
print(thistuple)

for x in thistuple:
  print(x)

a = ("MNNIT Allahabad", 5000, "Engineering" , ["com","bio","cham","maths"])

# this lines UNPACKS values
# of variable a
(college, fees, type_ofcollege,subject) = a

# print college name
print(college)
print(subject)