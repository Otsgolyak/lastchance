number = int(input('Введите число: '))
def is_even (number):
    result = number % 2 == 0;
    return result
result_2 = is_even(number)
print(result_2 )