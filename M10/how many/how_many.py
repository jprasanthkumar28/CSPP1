'''Length of Dictionar'''
#Exercise : how many
# write a procedure, called how_many, which returns the sum of the
# number of values associated with a dictionary.


def how_many(animals):
    '''Length of Dictionar'''
    # Your Code Here
    count = 0
    value = animals.values()
    for index in value:
        count += len(index)
    return count

def main():
    '''Length of Dictionar'''
    #animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    #animals['d'] = ['donkey']
    #animals['d'].append('dog')
    #animals['d'].append('dingo')
    data = input()
    animals = {}
    for _ in range(int(data)):
        number = input()
        value1 = number.split()
        if value1[0][0] not in animals:
            animals[value1[0][0]] = [value1[1]]
        else:
            animals[value1[0][0]].append(value1[1])
    print(animals)
    print(how_many(animals))
if __name__ == "__main__":
    main()
