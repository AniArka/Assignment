import math

#eqation = "a*x**2+b*x+c"
a = int(input("enter value of a[a!=0]"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))
if a!= 0:
    dis = b ** 2 - 4 * a * c
    root1 = (-b + math.sqrt(dis)) / 2 * a
    root2 = (-b - math.sqrt(dis)) / 2 * a
    print(f"value of positive root is {root1}")
    print(f"value of negative root is {root2}")
else:
    print("please enter valid input")