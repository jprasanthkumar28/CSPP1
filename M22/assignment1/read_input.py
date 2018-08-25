'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    doc = ''
    lines = int(input())
    for index in range(lines):
    	# doc.append(input())
    	doc = ''.join(input())
    	print(doc)

if __name__ == '__main__':
    main()
