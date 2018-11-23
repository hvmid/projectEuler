from math import sqrt

l=[]	

for i in range(1, 450):
	for j in range(1, 450):
		if sqrt((i**2)+(j**2)).is_integer():

			print()
			print("a= "+str(i))
			print("b="+str(j))
			print("c="+str((i**2)+(j**2)))
			if (i+j+sqrt((i**2)+(j**2)))==1000:
				print()
				print("-----ANSWER------")
				print("a= "+str(i))
				print("b="+str(j))
				print("c="+str((i**2)+(j**2)))
				print(i*j*sqrt((i**2)+(j**2)))