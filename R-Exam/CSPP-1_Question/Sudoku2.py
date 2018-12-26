def validInput(data):
    if len(data) != 81:
        raise Exception("Invalid input")
    elif '.' not in data:
        raise Exception("Given sudoku is solved")

def validSudoku(sudoku):
    for x in range(0,9):
        var = getRow(x, sudoku)
        if len(set(var)) != len(var):
            raise Exception("duplicates are present")   
            # print("duplicates are present")
        colVar = getCol(x, sudoku)
        if len(set(colVar)) != len(colVar):
            raise Exception("duplicates are present")   
            # print("duplicates are present")

def getRow(cell, sudoku):
    row = []
    for x in sudoku[cell]:
        if x != '.':
            row.append(x)
    # print(row)
    return row

def getCol(cell, sudoku):
    col = []
    for row in sudoku:
        if row[cell] != '.':
            col.append(row[cell])
    # print(col)
    return col


def getSubGrid(cell):
    pass

def possibilites(sudoku):
    # print(len(sudoku))
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            # print(i, j)
            if sudoku[i][j] == ".":
                rowVal = getRow(i, sudoku)
                colVal = getCol(j, sudoku)
                newData = rowVal + colVal
                string = ''
                for l in range(1,10):
                    if str(l) not in newData:
                        string += str(l)
                print(string)


def main():
    data1 = input()
    data = list(data1)
    # print(data)
    i = 0
    sudoku = []

    try:
        while(i < 81):
            row = []
            for k in range(0,9):
                row.append(data[i])
                i = i + 1
            sudoku.append(row)
        validInput(data1)
        validSudoku(sudoku)
        possibilites(sudoku)
    except Exception as e:
        print(e)
    # print(sudoku)

if __name__ == '__main__':
    main()
