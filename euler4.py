three_digit=[n for n in range(100, 1000)]
l=[]
for digit in three_digit:
	
	for i in range(100,1000):
		temp=i*digit
		s=str(temp)
		if s==s[::-1]:
			l.append(int(s))
l.sort()			
print(l)


	