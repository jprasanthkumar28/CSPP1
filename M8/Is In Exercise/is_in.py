'''Search'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments
# a character and String and returns the isIn(char, aStr) which retuns
# a boolean value.

# This function takes in two arguments character and String
# and returns one boolean value.

def isin(char, astr):
    '''Search'''
    # Your code here
    value = 0
    len1 = len(astr)
    if value == len1:
        return False
    if char == astr[value]:
        return True
    astr = astr[value + 1:len1]
    return isin(char, astr)

def main():
    '''Search'''
    data = input()
    data = data.split()
    print(isin((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
