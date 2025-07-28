fib = [-1] * 60
fib[1] = fib[2] = 1;
	 
def fibnacci(n):
    if fib[n] != -1:
        return fib[n]
    else:
        fib[n] = fibnacci(n-1) + fibnacci(n-2)
        return fib[n]

