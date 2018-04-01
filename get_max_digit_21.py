import random
number = random.randint(100000000000, 999999999999)
string = str(number)
print('The random number is: ', string)
def get_max_digit (string):
    result = ''
    for count in string:
        if count > result:
           result = count
    result_1 = int(result)
    return result_1
print('The upper num is: ', get_max_digit(string))
