# Question 1
x = int(input("enter a number: "))
if (x % 2) == 0:
    print(x,  "is even") 
else:
    print(x,  "is odd")

# Question 2
height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
if weight <= 0:
    w = 28
elif weight <= 70:
    w = 30
elif weight <= 80:
    w = 32
else:
    w = 34
print("your waist size is", w, "inches")