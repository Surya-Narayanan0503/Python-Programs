a,b=map(int,(input()))
for i in range(a+1,b):
	if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
		print (i, end = " ")
		
