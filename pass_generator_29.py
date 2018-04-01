import string
import random

pass_len = 8

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
lower_q = 3
upper_q = 2
num_q = 3
qoute = [1, 1, 1]
passw = ''
def password_generator(lower_q, upper_q, num_q):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    passw = ''
    for i in range(lower_q):
        passw += random.choice(lower)
    for i in range(upper_q):
        passw += random.choice(upper)
    for i in range(num_q):
        passw += random.choice(num)
    passw = list(passw)
    random.shuffle(passw)
    password = ''.join(passw)
    return password
print (password_generator(3, 2, 3))
