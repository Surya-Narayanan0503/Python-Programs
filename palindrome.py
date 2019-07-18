num = int(input())
temp = num
num=a
a=b
reverse = 0
 
while temp != 0:
	reverse = (reverse * 10) + (temp % 10)
	temp = temp // 10
 
if b == reverse:
	print("yes")
else:
	print("no")
