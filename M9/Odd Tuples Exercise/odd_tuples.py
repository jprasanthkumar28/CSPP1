'''Odd_Tuples'''
#Exercise : Odd Tuples
#Write a python function oddTuples(aTup)
#that takes a some numbers in the tuple as input
#and returns a tuple in which contains odd index values in the input tuple

def oddtuples(atup):
    '''Odd_Tuples'''
    #aTup = ('I', 'am', 'a', 'test', 'tuple')
    #new = ()
    #for i in range(0, len(atup), 2):
    #    new += (atup[i], )
    #return new
    return atup[0::2]
    #new = tuple((t[i] for i in range(0,len(atup),2)):

def main():
    '''Odd_Tuples'''
    data = input()
    data = data.split()
    atup = ()
    for j in data:
        atup += (j, )
    print(oddtuples(atup))

if __name__ == "__main__":
    main()
