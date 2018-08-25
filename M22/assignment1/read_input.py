'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''To read the input and print'''
    doc = ''
    lines = int(input())
    for _ in range(lines):
        # doc.append(input())
        doc = ''.join(input())
        print(doc)

if __name__ == '__main__':
    main()
