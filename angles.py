import math
angle = float(input('Введите значение угла: '))
radians = math.radians(angle)                                    #####(angle * math.pi) / 180
cos_of_radians = math.cos(radians)
print("Косинусом угла %d\xb0 \nявляется: %.4f радиан " % (angle, cos_of_radians))

