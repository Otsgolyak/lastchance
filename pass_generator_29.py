import string
import random


def password_generator():
    quotas = [1, 1, 1] # to guarantee min values
    what_to_increase = 0
    while sum(quotas) < 7:
        what_to_increase = random.randint(0, len(quotas)-1)
        quotas[what_to_increase] += random.randint(1, 2)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    passw = ''
    
    for i in range(quotas[0]):
        passw += random.choice(lower)
    for i in range(quotas[1]):
        passw += random.choice(upper)
    for i in range(quotas[2]):
        passw += random.choice(num)
    if len(passw) == 7:
        passw += '_'
        passw = list(passw)
        random.shuffle(passw)
        
    return ''.join(passw)
print (password_generator())
