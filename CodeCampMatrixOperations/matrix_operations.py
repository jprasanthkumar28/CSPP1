import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # pass
    msum = copy.deepcopy(m1)
    if len(m1) == len(m2):
    	for i in range(len(m1)):
    		for j in range(len(m2)):
    			temp = int(msum[i][j])
    			temp += int(m2[i][j])
    			msum[i][j] = temp
    	return msum


def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # pass
    rows = int(size[0])
    columns = int(size[1])
    total = 0
    matrix = []
    for index in range(0, rows, 1):
    	row = input().split()
    	matrix.append(row)
    	total += len(row)
    if total != rows * columns:
    	print("Error: Invalid input for the matrix")
    else:
    	return matrix

def main():
    # read matrix 1
    n1 = input().split(',')
    # print(n1)
    m1 = read_matrix(n1)
    # print(m1,"<-------------first")
    # read matrix 2
    n2 = input().split(',')
    m2 = read_matrix(n2)
    # print(m2,"<-------------second")
    # add matrix 1 and matrix 2
    print(add_matrix(m1, m2))
    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
