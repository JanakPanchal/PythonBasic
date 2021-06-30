# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# for a in student:
# 	print(a)

count = 0
fruits = ["apple", "banana", "cherry"]
for f in fruits:
	print(f)
	print(count)
	count = count + 1

for f in range(len(fruits)):
	print(fruits[f])