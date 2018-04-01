import math
#ver = int(input("Введите значение угла: "))
def degrees_2_radians (angle):
   radians =  (angle * math.pi) / 180
   return radians
print('Косинусом угла 40\xb0 является %f \nКосинусом угла 45\xb0 является %f \nКосинусом угла 60\xb0 является %f \n' % 
(math.cos(degrees_2_radians(40)), math.cos(degrees_2_radians(45)), math.cos(degrees_2_radians(60))) )

# angle = float(input('Введите значение угла: '))
# radians = math.radians(angle)                                    #####(angle * math.pi) / 180
# cos_of_radians = math.cos(radians)
# print("Косинусом угла %d\xb0 \nявляется: %.4f радиан " % (angle, cos_of_radians))

