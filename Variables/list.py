name = ["Janak" , "Rohan", "raju" ,1 , 10.5 , 1000 , True]

print(name)
print(name[1])
name.append("Komal")
print(name)
print("rohan".title() in name)

for n in name :
	print(str(n).title())
	
print(name[5])
print(name[2:5])
name.remove("raju")
print(name)

#[]
name.clear()
print(name)

#remove value from list
thislist = ["apple", "banana", "cherry"]
thislist.pop()
thislist.pop()
print(thislist)

