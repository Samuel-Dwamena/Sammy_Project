#sleeve of Erastosthenes

noprimes = [j for i in range(2,8) for j in range(i*2,100,i)]
primes = [x for x in range(2,100) if x not noprimes]

print("Not primes; ", noprimes)
print("Primes; ", primes)
