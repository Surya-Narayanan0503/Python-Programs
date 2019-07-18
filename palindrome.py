num = int(input())
 
temp = num
reverse = 0
 
while temp != 0:
	reverse = (reverse * 10) + (temp % 10)
	temp = temp // 10
 
if num == reverse:
	print("yes")
else:
	print("no")
