
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
sum=0
for i in range(1, 2000000):
	if isPrime(i)==True:
		count=count+1
		sum=sum+i	
		print(i, count)
		if i==1000001:
			break

print(sum)
print(count)	





	
	