import os
# os.remove("myfile.txt")

if os.path.exists("a.txt"):
  os.remove("a.txt")
else:
  print("The file does not exist")
  
try:
	os.rmdir("myfolder")
except:
	print("error")