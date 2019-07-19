s,n=map(str,input().split())
len1=len(s)
len2=len(n)
if len1>len2:
	print(s)
elif len2>len1:
	print(n)
else:
	print(n or s)
