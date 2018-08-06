'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    mul = 1
    while int_input != 0:
        if int_input > 0:
            rem = int_input%10
            mul = mul * rem
            int_input = int_input//10
            res = mul
        else:
            int_input = -(int_input)
            rem = int_input%10
            mul = mul * rem
            int_input = int_input//10
            res = abs(mul)
    print(res)

if __name__ == "__main__":
    main()
