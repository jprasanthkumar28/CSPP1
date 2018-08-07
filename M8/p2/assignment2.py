'''sumofdigits'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits,
# that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(num):
    '''sumofdigits'''
    # Your code here
    if num == 0:
        return 0
    return (num%10) + (sumofdigits(num//10))


def main():
    '''sumofdigits'''
    ans = input()
    print(sumofdigits(int(ans)))

if __name__ == "__main__":
    main()
