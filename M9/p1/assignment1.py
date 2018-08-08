'''Game'''
def is_word_guessed(secret_word, letters_guessed):
    '''Game'''
    # FILL IN YOUR CODE HERE...
    count = 0
    for index in secret_word:
        if index in letters_guessed:
            count += 1
    if len(secret_word) == count:
        return True
    return False

def main():
    '''Game'''
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
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
