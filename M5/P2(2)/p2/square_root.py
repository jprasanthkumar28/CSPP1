'''Approx_Method'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Approx_Method'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    num = int(input())
    epsilon = 0.01
    ans = 0.0
    inc = 0.1
    while abs(ans**2-num) >= epsilon:
        ans += inc
    if abs(ans**2 - num) >= epsilon:
        print("Failed on square root of", num)
    else:
        print(ans)

if __name__ == "__main__":
    main()
