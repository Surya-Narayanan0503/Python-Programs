n=int(input())
sum=0
a=1
b=1
for i in range(0,n):
	b=sum+a
	sum=a
	a=b
	print(b,end=' ')
		
