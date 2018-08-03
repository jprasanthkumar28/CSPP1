'''Newton-Rapson'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Newton-Rapson'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    epsilon = 0.01
    num = int(input())
    guess = num/2.0
    while abs(guess*guess-num) >= epsilon:
        guess = guess - (((guess**2) - num)/(2*guess))
    print(guess)
    #step = 0.1
    # your code starts here

if __name__ == "__main__":
    main()
