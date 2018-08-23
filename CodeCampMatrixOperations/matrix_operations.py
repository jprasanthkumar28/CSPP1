'''Mathematical Operations on Matrix'''
import copy
def mult_matrix(mat1, mat2):
    '''check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"'''
    if len(mat1) != len(mat2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    res = []
    for index in range(0, len(mat1), 1):
        list1 = []
        for jindex in range(0, len(mat2[0]), 1):
            mul = 0
            for k in range(0, len(mat2), 1):
                mul += int(mat1[index][k]) * int(mat2[k][jindex])
            list1.append(mul)
        res.append(list1)
    return res


def add_matrix(mat1, mat2):
    '''check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"'''
    # pass
    msum = copy.deepcopy(mat1)
    if len(mat1) == len(mat2):
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                temp = int(msum[i][j])
                temp += int(mat2[i][j])
                msum[i][j] = temp
        return msum
    print("Error: Matrix shapes invalid for addition")
    return None


def read_matrix(size):
    '''read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"'''
    # pass
    rows = int(size[0])
    columns = int(size[1])
    total = 0
    matrix = []
    for _ in range(0, rows, 1):
        row = input().split()
        matrix.append(row)
        total += len(row)
    if total != rows * columns:
        print("Error: Invalid input for the matrix")
    else:
        return matrix

def main():
    '''Main Function'''
    # read matrix 1
    num1 = input().split(',')
    # print(n1)
    mat1 = read_matrix(num1)
    # print(mat1,"<-------------first")
    # read matrix 2
    numat2 = input().split(',')
    mat2 = read_matrix(numat2)
    if mat1 is None or mat2 is None:
        return None
    # print(mat2,"<-------------second")
    # add matrix 1 and matrix 2
    print(add_matrix(mat1, mat2))
    # multiply matrix 1 and matrix 2
    print(mult_matrix(mat1, mat2))

if __name__ == '__main__':
    main()
