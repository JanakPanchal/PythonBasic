# File Handling
# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)

#f = open("demofile.txt")
#f = open("demofile.txt", "r")

f = open("demofile.txt", "r")
#reading file
# print(f.read())
#reading characters
# print(f.read(5))
#reading line
for a in range(3):
	if "testing" in f.readline():
		print("true")
	else:
		print("false")
f.close()
		


