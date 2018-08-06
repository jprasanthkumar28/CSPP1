'''Quadratic Equation'''
# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
#that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.

def evalQuadratic(num1, num2, num3, res):
    '''Quadratic equation function'''
    return num1 * res * res + num2 * res + num3

def main():
    '''Quadratic Equation'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for res in enumerate(len(data)):
        temp = str(data[res]).split('.')
        if temp[1] == '0':
            data[res] = int(float(str(data[res])))
        else:
            data[res] = data[res]
    print(evalQuadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
