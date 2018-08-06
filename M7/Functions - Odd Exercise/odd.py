'''Odd'''
# Exercise: odd

# Write a Python function, odd, that takes in one number and returns True
#when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.


def odd(var):
    '''Odd'''

    # Your code here
    return bool(var % 2)

def main():
    '''Odd'''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
