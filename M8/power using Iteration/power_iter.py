'''Power'''
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iterPower(base, exp):
    '''Power'''
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    '''if exp == 1:
        return base
    else:
        return base * iterPower(base, exp-1)'''
    res = 1
    for i in range(exp):
        res = res * base
    return res
def main():
    '''Power'''
    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()