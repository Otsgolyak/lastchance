v_1 = int(input('Введите скорость первого поезда: '))
v_2 = int(input('Введите скорость второго поезда: '))
def have_trains_crashed (v_1, v_2, s = 10, s_1 = 4):
    s_2 = s - s_1
    t_1 = v_1/s_1
    t_2 = v_2/s_2
    if t_1 <= t_2:
       return True
    else:
       return False
result = have_trains_crashed (v_1, v_2, s = 10, s_1 = 4)
print(result)