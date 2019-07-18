a=int(input())
order=len(str(num))
sum=0
temp=a
while(temp>0):
	digits=temp%10
	sum+=digits**order
	temp//=10
if a == sum:
	print("yes")
else:
	print("no")
