"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
 	raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
	raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
	raise an exception
"""
def validateSudoku(sudoku):
	# pass
	for i in range(9):
		if '.' in sudoku:
			print("Invalid sudoku")
		elif len(sudoku) != 81:
			print("Invalid")
		elif len(sudoku) == 81 and '.' not in sudoku:
			print("Suduko solved")
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues():
	pass
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues():
	pass

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues():
	pass
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues():
	pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
	data = input()
	data = list(input())
	row = []
	# print(row)
	validateSudoku(data)