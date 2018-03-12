import math
x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
r1 = int(input("Введите координату r1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))
r2 = int(input("Введите координату r2: "))
check
15
def circles (x1,y1,r1,x2,y2,r2):
    D = math.sqrt((x1 - x2) **2 + (y1 - y2) **2)
    SR = r1 + r2
    if r1 == r2 and D == 0 or D <= SR : 
        return True
    else:
        return False 
print(circles(x1,y1,r1,x2,y2,r2))
var = math.sqrt((x1 - x2) **2 + (y1 - y2) **2)
print(var)


#or r1 == r2 and D == 0: