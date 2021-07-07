
# >>> try:
# ...     raise NameError('HiThere')
# ... except NameError:
# ...     print('An exception flew by!')
# ...     raise


# try:
# 	print("try block")
# except:
# 	print("error")
# finally:
# 	print("finally")

try:
	k = 5 // 0  # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exceptionss generation.
	print('This is always executed')