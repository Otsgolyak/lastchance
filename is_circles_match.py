import math
x_1 = int(input("Введите координату x_1: "))
y_1 = int(input("Введите координату y_1: "))
r_1 = int(input("Введите координату r_1: "))
x_2 = int(input("Введите координату x_2: "))
y_2 = int(input("Введите координату y_2: "))
r_2 = int(input("Введите координату r_2: "))
def circles (x_1,y_1,r_1,x_2,y_2,r_2):
    distance = math.sqrt((x_1 - x_2) **2 + (y_1 - y_2) **2)
    sum_of_radiuses = r_1 + r_2
    sum_of_radiuses_2 = abs(r_1 - r_2)
    if distance == sum_of_radiuses or distance == sum_of_radiuses_2 or distance > sum_of_radiuses_2 and distance < sum_of_radiuses and distance != 0: 
        return True
    else:
        return False 
print(circles(x_1,y_1,r_1,x_2,y_2,r_2))



#or r_1 == r_2 and D == 0:
#r_1 == r_2 and D == 0 or D <= SR and D != 0