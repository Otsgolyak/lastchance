def gen_primes(n):
    list_of_ints = []
    for i in range(2, n+1):
        for j in list_of_ints:
            if i % j ==0:
               break
        else: 
            list_of_ints.append(i)  
      
    return list_of_ints
print(gen_primes(100))