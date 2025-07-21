import math

a = float(input())
b = float(input())

c = float(input())
d = float(input())

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(distance(a, b, c, d))

