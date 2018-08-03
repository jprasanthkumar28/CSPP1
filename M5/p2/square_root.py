'''Square'''
# Write a python program to find the square root of the given number
# using approximation method

def main():
    '''Square'''
    #s = raw_input()
    #your code here
    num = int(input())
    value = 0
    while value**2 < num:
        value += 1
    if value**2 != num:
        print(num, "is not a perfect square")
    else:
        print(num, "is a perfect square")
if __name__ == "__main__":
    main()
    