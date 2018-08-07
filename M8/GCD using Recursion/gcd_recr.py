'''GCD'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b),
# that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdRecur(val1, val2):
    '''GCD'''

    # Your code here
    if val2 == 0:
        return val1
    else:
        gcd = gcdRecur(val2, val1 % val2)
    return gcd


def main():
    '''GCD'''
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
