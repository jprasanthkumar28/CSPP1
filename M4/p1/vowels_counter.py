'''Vowels'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''Vowels'''
    #s = raw_input()
    value = input()
    vowelCount = 0
    for char in value:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowelCount += 1
    print(vowelCount)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()
