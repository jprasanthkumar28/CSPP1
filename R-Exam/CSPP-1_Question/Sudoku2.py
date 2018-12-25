data = list(input())
# for i in range(9):
if '.' not in data:
	print("Sudoku Solved")
elif len(data) != 81:
	print("Invalid input")
else:
	check = [False] * 9
	count = 0
	string = ''
	for string in data:
		if count == 9:
			for i in range(9):
				if check[i] == False:
					print(i+1)
			count = 0
		count = count + 1
		if (string == '.'):
			continue
		check[int(string) - 1] = True
	if count == 9:
		for j in range(9):
			if check[j] == False:
				print(j+1)