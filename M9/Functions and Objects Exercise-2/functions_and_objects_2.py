'''Plus 1'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(listval):
    '''Plus 1'''
    return listval+1

def apply_to_each(listval, function):
    '''Plus 1'''
    res = map(inc, listval)
    return list(res)

def main():
    '''Plus 1'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
