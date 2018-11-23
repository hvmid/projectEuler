l=[]
#function here that checks numbers factor
for n in range(2520, 900000000):
	#if factor(n):
	if n%12==0 and n%11==0 and n%20==0 and n%14==0 and n%16==0 and n%13==0 and n%17==0 and n%19==0 and n%18==0 and n%15==0:

		l.append(n)  

			
print(l)

