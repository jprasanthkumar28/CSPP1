'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''To remove the special characters and merge the letters'''
    newstring = re.sub('[^a-z]+', '', string)
    return newstring

def main():
    '''Main Function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
