square_of_sums=[]
squares=[n for n in range(1,101)]

for i in range(1,101):
	square_of_sums.append(i**2)

sum_of_squares=sum(squares)**2
print(sum(square_of_sums))	
print(sum_of_squares)
print(sum_of_squares-sum(square_of_sums))