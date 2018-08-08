'''Square'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(listval):
    '''Square'''
    return listval * listval

def apply_to_each(listval, f):
    '''Square'''
    res = map(square,listval)
    return list(res)
    
    
def main():
    '''Square'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__== "__main__":
    main()