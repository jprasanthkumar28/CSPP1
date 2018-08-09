'''Biggest in dictionary'''
#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding
#to the entry with the largest number of values associated with it.
#If there is more than one such entry, return any one of the matching keys.

def biggest(animals):
    '''Biggest in dictionary'''
    # Your Code Here
    flag = 0
    value = animals.values()
    bigger = max(value)
    for word in animals:
        if animals[word] == bigger:
            return word
        flag = 1
        return flag

def main():
    '''Biggest in dictionary'''
    number = input()
    animals = {}
    for _ in range(int(number)):
        data = input()
        splitting = data.split()
        if splitting[0][0] not in animals:
            animals[splitting[0][0]] = [splitting[1]]
        else:
            animals[splitting[0][0]].append(splitting[1])
    print(biggest(animals))

if __name__ == "__main__":
    main()
