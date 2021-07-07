

file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.write("This is my testing file \n")
file1.close()
#
file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
file1.close()

#Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
try:
	for tempdata in L :
		# Writing to file
		with open("myfile.txt", "a") as file1:
			# Writing data to a file
			file1.writelines(tempdata)
		
		# Reading from file
		with open("myfile.txt", "r+") as file1:
			# Reading form a file
			print(file1.read())
except:
	print("error")
finally:
	file1.close()
	
	
