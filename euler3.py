import math 

def odd_num(x):

	odds=[i for i in range(3, x, 2)]
	return(odds)	

def largest_prime_factor(n):
	
	factors=[]
	primes = odd_num(int(math.floor(n**0.5)))

	for prime in primes:
		if n%prime==0:
			if len(largest_prime_factor(prime))==0:
				factors.append(prime)	

	return factors

print(largest_prime_factor(600851475143))