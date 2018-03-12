variable_a = int(input('Введите переменную a: '))
variable_b = int(input('Введите переменную b: '))
variable_c = (variable_a**2 + variable_b**2) % 2
print('при переменной a равной: %d \nпеременной b равной: %d \nОтвет равен: %.2f' % (variable_a, variable_b, variable_c))