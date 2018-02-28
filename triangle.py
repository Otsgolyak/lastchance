import math
cateter_1 = int(input('Введите значение первого катета: '))
cateter_2 = int(input('Введите значение второго катета: '))
triangle_square = (cateter_1 * cateter_2) / 2
gipothenuse = math.sqrt(cateter_1**2 + cateter_2**2)
print('Площадь треугольника равна %d \nГипотенуза треугольника равна %d' % (triangle_square, gipothenuse))
