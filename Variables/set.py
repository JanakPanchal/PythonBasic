# Set
# Sets are used to store multiple items in a single variable.
#
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#
# A set is a collection which is both unordered and unindexed.
#
# Sets are written with curly brackets.

myset = {"apple", "banana", "cherry", "apple"}
print(myset)
print(set(myset))
print(len(myset))
#adding the value in set
myset.add("janak")
print(myset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(list(thisset))

#remove any value from set
thisset.remove("banana")
print(thisset)

for x in thisset:
  print(x)
