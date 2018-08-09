'''Not-Guessed Letters'''
import string
def get_available_letters(letters_guessed):
    '''Not-Guessed Letters'''
    values = string.ascii_lowercase
    result = ''
    # FILL IN YOUR CODE HERE...
    for index in values:
        if index in letters_guessed:
            continue
        else:
            result += index
    return result

def main():
    '''Not-Guessed Letters'''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
