addThree = lambda x, y, z : x + y + z

print(addThree(5, 7, 9))
print((lambda x,y,z:x+y+z)(5, 7, 9))

abs_value = lambda x : x if x >= 0 else -x

print(abs_value(-733))
print(abs_value(56))
