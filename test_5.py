ver_1 = float(input('Введите первое число: '))
ver_2 = float(input('Введите второе число: '))
def nearest_num(ver_1, ver_2):
    center = 10
    if center - abs(ver_1) < center - abs(ver_2):
        return print('Число %.2f ближе к 10' % (ver_1))
    else:
        return print('Число %.2f ближе к 10' % (ver_2)) 

nearest_num(ver_1, ver_2)