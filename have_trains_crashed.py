v1 = int(input('Введите скорость первого поезда: '))
v2 = int(input('Введите скорость второго поезда: '))
def have_trains_crashed (v1, v2, s = 10, s1 = 4):
    s2 = s - s1
    t1 = v1/s1
    t2 = v2/s2
    if t1 <= t2:
       return True
    else:
       return False
result = have_trains_crashed (v1, v2, s = 10, s1 = 4)
print(result)