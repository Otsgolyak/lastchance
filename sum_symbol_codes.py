symbol_1 = str(input('Введите первый символ: '))
symbol_2 = str(input('Введите второй символ: '))
def sum_symbol_codes (symbol_1, symbol_2):
    num_1 = ord(symbol_1)
    num_2 = ord(symbol_2)
    if num_1 > num_2:
        return sum(range(num_2,num_1 + 1))
    else:
        return sum(range(num_1,num_2 + 1))
result = sum_symbol_codes(symbol_1, symbol_2)    
print(result)