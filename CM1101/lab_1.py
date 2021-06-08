# Question 2
print(2+3)
print(4*12)
# To the power of '**'
print (2**8)

# Question 3
# Zero division error it should be a non zero number
# print(5/0)

# Question 4
print(12 % 10)
print(5 % 9)
print( 7 % 7)
print(0 % 7)
print(-1 % 7)
print(-8 % 7)
print(-15 % 7)
print(1 % -7)
print(-5 % -7)

# Question 5
print(3 * 2 + 7 % 3 ** 2)
print(3 * (2 + 7) % 3 ** 2)
print(3 * 2 + (7 % 3) ** 2)
print((3 * 2 + 7) % 3 ** 2)
print(3 * (2 + (7 % 3)) ** 2)
print(((3 * 2 + 7) % 3) ** 2)
print(((3 * (2 + 7)) % 3) ** 2)

# Question 6
print(type(4))
print(type(5.0))
print(type("Six"))
print(type(True))

# Question 7
a = 5
b = 4
print(a)
print(b)
print(a + b)
b = 3
print (a + b)

# Question 8
C = 21
F = ((9/5 * C) + 32)
print(F)

# Quesion 9
F = 69.8
C = ((F - 32) * 5/9)
print(C)


# Question 10
import math
print(math.sqrt(4))

# Question 11
print(True)
print(not True)
print(False and True)
print(False or True)
print((not False) and (False or True))
print( (False or True) and (False or (True and True)))
print( ((not False) and (not True)) or ((not True) and (not False)))

# Question 12
print(4>5)
print((12 % 5) < 5)
print( 3 + 4 == 4 + 3)
print(((1 > 2) or (3 < 4)) and (5 <= 5))
print( (2 < 5) == (3 < 4))

x = 0
y = 1.2
print(x >= 0 and y < 1)
print(x >= 0 or y < 1)
print(x > 0 or y > 1)
print(x > 0 or not y > 1)
print(-1 < x <= 0)
print( not (x > 0 or y > 0))

# Question 13
print("hello" + ", " + "world")
a = "abra"
b = "cad"
s = a + b + a 
print(s)
# how many characters the string is
print(len(s))
# how many times the letter a appears
print(s.count("a"))
print(s[0])
print(s[2])
print(s[0:3])
print(s[:5])
print(s[5:])
print(s[-5])
