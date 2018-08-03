'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the
letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've
had a break and cleared your head.'''

def main():
    '''Sequence'''
    string1 = input()
    bigstr = ""
    len1 = len(string1)
    for j in range(len1):
        substr = ""
        dup = string1[j]
        for i in range(j, len(string1)):
            if dup <= string1[i]:
                dup = string1[i]
                substr += dup
            else:
                break
        if len(bigstr) < len(substr):
            bigstr = substr
    print(bigstr)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()