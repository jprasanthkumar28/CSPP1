'''Guessing_Number'''
#Guess My Number Exercise

def main():
    '''Guessing_Number'''
    #s = raw_input()
    #your code here
    half = 50
    end = 100
    start = 0
    data = 'l'
    while data != 'c':
        print(half)
        data = input("Enter 'h' if guess is too high, 'l' if its too low.\
            'c' to indicate I guessed correctly")
        if data == 'h':
            end = half
            half = (end+start)//2
        elif data == 'l':
            start = half
            half = (end+start)//2
    print("Your lucky number is :", half)
if __name__ == "__main__":
    main()
