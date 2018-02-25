import math
variable_a = int(input('Введите переменную a: '))
variable_b = int(input('Введите переменную b: '))
variable_c = int(input('Введите переменную c: '))
variable_d = math.fabs(variable_a - variable_b) / (variable_a + variable_b)**3-math.cos(variable_c)
print('При переменной a равной %d \nпеременной b равной %d \nпеременной c равной %d \nОтвет равен: %.2f' % (variable_a, variable_b, variable_c, variable_a))

