import random

def diff_min_max (num_limit, lower_bound, upper_bound):
    maximum_number = 0
    minimum_number = upper_bound
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print('random num: ', rand_num)
        if rand_num > maximum_number:
           maximum_number = rand_num
           print('max: ', maximum_number) 
        elif rand_num < min_1:
             min_1 = rand_num 
        print('min: ', min_1)     
    return maximum_number - min_1
print("result: ", diff_min_max(12, 100, 250)) 