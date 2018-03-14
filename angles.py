import math
ver = int(input("Введите значение угла: "))
def degrees_2_radians (angle):
   cosinus_from_angle =  math.cos((angle * math.pi) / 180)
   return cosinus_from_angle
print(degrees_2_radians(ver))
# angle = float(input('Введите значение угла: '))
# radians = math.radians(angle)                                    #####(angle * math.pi) / 180
# cos_of_radians = math.cos(radians)
# print("Косинусом угла %d\xb0 \nявляется: %.4f радиан " % (angle, cos_of_radians))

