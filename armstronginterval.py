a,b=map(int,input().spilt())
for i in range(a,b+1):
	sum=0
	order=len(str(i))
	temp = i
	while temp>0:
		digits=temp%10
		sum+=digits**order
		temp//=10
	if i == sum:
		print(i)
