import math
a=int(input('Введите переменную a: '))
b=int(input('Введите переменную b: '))
c=int(input('Введите переменную c: '))
d=(math.log1p(c)/-b)**4+math.fabs(a)
print('Ответ:',(d))
