n = int(input())
# def OddComp():
count = 0
for i in range(2,n):
	for j in range(2,i):
		if ((i % 2 != 0) and (i % j == 0)):
			count += 1
			if count > 0:
				print(i)
				break