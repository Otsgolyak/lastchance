import random

def diff_even_odd (num_limit, lower_bound, upper_bound):
    even_number = 0
    odd_number = 0
    for _ in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print('random num: ', rand_num)
        if rand_num % 2 == 0:
           even_number += rand_num
           print('even_number: ', even_number) 
        else:
             odd_number += rand_num 
        print('odd_number: ', odd_number)     
    return even_number - odd_number
print("result: ", diff_even_odd(12, 100, 250)) 
  