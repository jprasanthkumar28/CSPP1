'''Lowercase'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''Vowels'''
    vowelCount=0
    value = input()
    for char in value:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            vowelCount += 1
    print(vowelCount)

if __name__== "__main__":
    main()