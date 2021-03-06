'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''Function to tokenize'''
    # pass
    newdict = {}
    string = re.sub('[^A-Z,a-z,0-9 ]', '', string)
    string = string.split()
    # print(string)
    for word in string:
        if word in newdict:
            newdict[word] += 1
        else:
            # newdict[word][0].append(docs.index(line))
            newdict[word] = 1
    return newdict

def main():
    '''Main Function'''
    doc = ''
    lines = int(input())
    for _ in range(lines):
        doc += ''.join(input())
    print(tokenize(doc))

if __name__ == '__main__':
    main()
