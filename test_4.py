number = str(input('Введите число: ', ))

def multiplication_of_odd_numbers(number):
    result = 1
    for num in number:
        if int(num) % 2 != 0:
            result = int(num) * result
         
    print('Произведение нечетных чисел: ', result)
multiplication_of_odd_numbers(number)
