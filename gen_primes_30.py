
def gen_primes():
    n = 100
    num = []
    for i in range(2, n+1):
        for j in num:
            if i % j ==0:
               break
        else: 
            num.append(i)  
      
    return num
print(gen_primes())