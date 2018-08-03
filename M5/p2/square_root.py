'''Square'''
# Write a python program to find the square root of the given number 
# using approximation method

def main():
    '''Square'''
    #s = raw_input()
    #your code here
    num = int(input())
    value = 0.01
    guess = 0.0
    inc = 0.01
    guess_count = 0
    while abs(guess*3 -  num) >= value:
        guess += inc
        guess_count += 1
    print('guesses_count = ', guess_count)
    if abs(guess*3 - num) >= value:
        print("Failed to get cube", num)
    else:
        print(guess, 'is close to the root', num)

if __name__ == "__main__":
    main()