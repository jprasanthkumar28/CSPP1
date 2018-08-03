'''''Bob'Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''Bob'''
    #s = raw_input()
    first = input()
    count = 0
    for i in range(len(first)-2):
        if first[i] == 'b' and first[i+1] == 'o' and first[i+2] == 'b':
            count += 1
    print(count)
    # the input string is in s
    # remove pass and start your code here

if __name__ == "__main__":
    main()
