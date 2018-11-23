

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True	

def isPrime(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	k=3
	while k*k<=n:
		if n%k==0:
			return False
		k+=2	
	return True        



count=0
for i in range(1, 200000):

	if isPrime(i)==True:
		count=count+1	
		print(i, count)
		if count==10001:
			break

print(count)	

print(count)




	
	