
x = 4.2

y = 10

z = "42"

print(not (((x * y == z) and not (x < y)) or y % 2 == 0)); # false

#print(not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0));# true

#print(not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z)))))); # true

print(not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))));