x = 300

def myfunc():
  print(x)

myfunc()
print(x)

x = 300
def myfunc():
  x = 200
  print(x)

myfunc() #200 or #300
print(x)  #300  or #300

def myfunc():
  global x
  x = 300

myfunc()
print(x)


"NO of Tyer : 4"
"No of door: 4"
"Type of enign : Micro or Mini"