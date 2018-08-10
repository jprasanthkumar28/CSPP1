'''Division'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.

def integer_division(val1, val2):
    '''Division'''

    count = 0
    while val1 >= val2:
        count += 1
        val1 = val1 - val2
    return count

def main():
    '''Division'''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
