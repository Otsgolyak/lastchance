import math
a=int(input('Введите переменную a: '))
b=int(input('Введите переменную b: '))
c=int(input('Введите переменную c: '))
d=math.fabs(a-b)/(a+b)**3-math.cos(c)
print('Ответ:',(d))
