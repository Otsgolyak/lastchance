
def gen_primes(n):
    num = []
    for i in range(2, n+1):
        for j in num:
            if i % j ==0:
               break
        else: 
            num.append(i)  
      
    return num
print(gen_primes(100))