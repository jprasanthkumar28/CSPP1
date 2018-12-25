data = input()
check = [False] * 9
if '.' not in data:
    print("Given sudoku is solved")
elif len(data) != 81:
    print("Invalid input")
else:
    count = 0
    string = ''
    for string in data:
        if count == 9:
            for index in range(9):
                if check[index] == False:
                    print(index + 1)
            # check = [False] * 9
            count = 0
        count = count + 1
        if(string == '.'):
            continue
        check[int(string) - 1] = True
    if count == 9:
	    for j in range(9):
	        if check[j] == False:
	            print(j + 1)
	    check = [False] * 9
	    count = 0
