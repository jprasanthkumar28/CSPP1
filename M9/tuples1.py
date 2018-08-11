# x = (1, 2, (3, 'John', 4), 'Hi')
#x = [1, 2, [3, 'John', 4], 'Hi']
#x[0]=8
'''listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA.sort()
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listB.sort()
listB.pop()
listA.extend([4, 1, 6, 3, 4])
#print(listA)
listA = listA.reverse()
print(listA)
===========================================
aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList
print(bList)
===========================================
cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
	dList.append(num)
print(List is dList)
===========================================
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
#del animals['b']
print(animals.values())
=================================================
def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

        def main():
    Hangman-Game
    #secretword = chooseword(wordlist).lower()
    #hangman(secretword)
    a=input()
    b=input()
    c=input()
if __name__ == "__main__":
    main()
==========================================
def rem(val1, val2):
    Division

    if val1 == val2:
        return 0
    elif val1 < val2:
        return val1
    else:
        return rem(val1-val2, val2)

def main():
    Division
    data = input()
    data = data.split()
    print(rem(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
========================================='''
def f(n):
    n = int(input())
    if n == 0:
      return 1
    else:
      return n * f(n-1)

