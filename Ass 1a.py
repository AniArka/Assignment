import math
polygon_type_input = input("which type of polygon do you want to measure? press 'T' for Triangle, 'R' for Rectengle, 'C' for Circle: ")
if "T" in polygon_type_input:
    hight = int(input("enter the length of the hight: "))
    base = int(input("enter the length of the base: "))
    ans = 0.5*base*hight
    print(f"area of triangle is {ans}")
elif "R" in polygon_type_input:
    length = int(input("enter length: "))
    hight = int(input("enter hight: "))
    ans = length*hight
    print(f"area of rectangle is {ans}")
elif "C" in polygon_type_input:
    radius = int(input("enter radius: "))
    ans = math.pi*radius
    print(f"area of circle is {ans}")
else:
    print("Please enter a valid choise")