def fibnacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibnacci(n-1) + fibnacci(n-2)

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

pi_num = 3.14159
e = 2.71
