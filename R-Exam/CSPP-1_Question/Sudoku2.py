data = list(input())
# for i in range(9):
if '.' not in data:
	print("Sudoku Solved")
elif len(data) != 81:
	print("Invalid input")
else:

	string = ''
	for i in range(len(data)):
		if string == '.':
			print(i+1)