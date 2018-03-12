digit = int(input('Введите число: '))
def is_even_number (digit):
    result = digit % 2 == 0;
    return bool(result)
result_2 = is_even_number(digit)
print(result_2 )