'''Guessed Words'''
def get_guessed_word(secret_word, letters_guessed):
    '''Guessed Words'''
    result = ''
    # FILL IN YOUR CODE HERE...
    for index in secret_word:
        if index in letters_guessed:
            result += index
        else:
            result += '_'
    return result

def main():
    '''Guessed Words'''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
