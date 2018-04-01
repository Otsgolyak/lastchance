import string
import random

pass_len = 8

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
lower_q = 3
upper_q = 2
num_q = 3
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
print (password)
print(lower)
print(upper)
print(num)