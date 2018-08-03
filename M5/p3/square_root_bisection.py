'''Bisection Method'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Bisection Method'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    #step = 0.1
    # your code starts here
    num = int(input())
    epsilon = 0.01
    low = 0.0
    high = num
    med = (low+high)/2.0
    while abs(med**2 - num) >= epsilon:
        if med**2 < num:
            low = med
        else:
            high = med
        med = (high+low)/2
    print(med)
if __name__ == "__main__":
    main()
