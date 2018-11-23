

a=0
b=1
solution=0

while b<=4000000:
	if b%2==0:
		solution+=b
	a,b = b, a+b       		


print(solution)


