# put your python code here
from math import *
a, b, c = float(input()), float(input()), float(input())

dis = (b**2)-4*a*c

if dis < 0:
    print("Нет корней")
    quit()

x1 = (-b+sqrt(dis))/(2*a)
x2 = (-b-sqrt(dis))/(2*a)

if x1 > x2:
    print(x2)
    print(x1)
elif x2 > x1:
    print(x1)
    print(x2)
elif dis == 0:
    print(x1)