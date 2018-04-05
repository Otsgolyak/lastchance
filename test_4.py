number = str(input('Введите число: ', ))

def sum_of_odd(number):
    result = 0
    for num in number:
        if int(num) % 2 != 0:
            result += int(num) 
    return print('Сумма нечетных чисел: ', result)
sum_of_odd(number)