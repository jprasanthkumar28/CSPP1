'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    temp = " "
    length = len(str_input)
    for i in range(length):
        if str_input[i] in ['!', '@', '#', '%', '^', '&', '*', '(', ')', '-']:
            temp = str_input[i]
            temp = temp + str_input
        else:
            temp = str_input
    print(temp)

if __name__ == "__main__":
    main()
