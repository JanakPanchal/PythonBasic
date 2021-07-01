# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.



#lambda arguments : expression

def addtion(number):
	return number + 10

print(addtion(5))
print(addtion(15))
print(addtion(120))

#using expression
x = lambda number : number + 10
#calling other function
x = lambda number : addtion(number)

print(x(5))
print(x(15))
print(x(120))

y  = lambda a, b, c : a + b + c
print(y(5,7,10))



