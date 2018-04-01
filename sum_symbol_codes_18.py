# symbol_1 = str(input('Введите первый символ: '))
# symbol_2 = str(input('Введите второй символ: '))
# def sum_symbol_codes (symbol_1, symbol_2):
#     num_1 = ord(symbol_1)
#     num_2 = ord(symbol_2)
#     if num_1 > num_2:
#         return sum(range(num_2,num_1 + 1))
#     else:
#         return sum(range(num_1,num_2 + 1))
# result = sum_symbol_codes(symbol_1, symbol_2)    
# print(result)

symbol_1 = input('Введите первый символ: ')
symbol_2 = input('Введите второй символ: ')
def sum_symbol_codes (symbol_1, symbol_2):
    num_1 = ord(symbol_1)
    num_2 = ord(symbol_2)
    min_symbol = min(num_1, num_2)
    max_symbol = max(num_1, num_2)
    return sum(range(min_symbol, max_symbol + 1))
result = sum_symbol_codes(symbol_1, symbol_2)    
print(result)