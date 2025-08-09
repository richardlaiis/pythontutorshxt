eval(input())

a, b, c = 1, 2, 3
eval('print(a, b, c)')

eval('print(a, b, c)', {'a':4, 'b':5, 'c':6})

eval('print(a, b, c)', {'a':4, 'b':5, 'c':6}, {'a':11, 'b':12, 'c':13})
