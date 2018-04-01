import math
ver_1 = int(input('Введите значение первого катета: '))
ver_2 = int(input('Введите значение второго катета: '))
def triangle_square (cateter_1, cateter_2):
    triangle_square_1 = (cateter_1 * cateter_2) / 2
    perimetr = (math.sqrt(cateter_1 **2 + cateter_2 **2)) + cateter_1 + cateter_2
    return triangle_square_1, perimetr
result_1, result_2 = triangle_square(ver_1, ver_2)
print(result_1)
print(result_2)
# gipothenuse = math.sqrt(cateter_1**2 + cateter_2**2)
# print('Площадь треугольника равна %d \nГипотенуза треугольника равна %d' % (triangle_square, gipothenuse))
# import math
# cateter_1 = int(input('Введите значение первого катета: '))
# cateter_2 = int(input('Введите значение второго катета: '))
# triangle_square = (cateter_1 * cateter_2) / 2
# gipothenuse = math.sqrt(cateter_1**2 + cateter_2**2)
# print('Площадь треугольника равна %d \nГипотенуза треугольника равна %d' % (triangle_square, gipothenuse))
