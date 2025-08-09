code = """
sum = 0
for i in range(10):
    tmp = i ** 3
    print(tmp)
    sum += tmp
print(sum)
"""

exec(code)
