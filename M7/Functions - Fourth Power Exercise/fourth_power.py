'''Fourth - Square'''
# Exercise: fourth power

# Write a Python function, fourthPower, that takes in one number and returns
# that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise
#exercise (you don't need to redefine square in this box;

# This function takes in one number and returns one number.

def square(var):
    '''Fourth - Square'''
    # Your code here
    return var * var

def fourthPower(var):
    '''Fourth - Square'''
    # Your code here
    res = square(var)
    return res * res

def main():
    '''Fourth - Square'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__ == "__main__":
    main()
