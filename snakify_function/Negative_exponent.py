def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    else:
        return (power(a, n-1) * a)

a = float(input())
n = int(input())
print(power(a, n))
