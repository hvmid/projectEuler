def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
print(factorial(100))
a=factorial(100)
b=str(a)
l=[]
for i in range(0, len(b)):

	c=int(b[i])
	l.append(c)

print(sum(l))

