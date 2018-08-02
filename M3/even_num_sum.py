n = int(input("Enter Number"))
sum=0
i=0
for i in range(n+1):
	if (i%2==0):
		sum += i
print(sum)