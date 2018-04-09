ver_1 = float(input('Введите первое число: '))
ver_2 = float(input('Введите второе число: '))
def nearest_num(ver_1, ver_2):
    center = 10
    if abs(center - abs(ver_1)) < abs(center - abs(ver_2)):
        print('Число %.3f ближе к 10' % (ver_1))
    else:
        print('Число %.3f ближе к 10' % (ver_2)) 

nearest_num(ver_1, ver_2)