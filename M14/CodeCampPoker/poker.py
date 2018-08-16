'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def sort(hand):
    '''To sort the hand'''
    len_count = len(hand)
    new_hand = []
    #print(new_hand)
    for index in range(len_count):
        if hand[index][0] == 'A':
            new_hand.append(14)
        elif hand[index][0] == 'K':
            new_hand.append(13)
        elif hand[index][0] == 'Q':
            new_hand.append(12)
        elif hand[index][0] == 'J':
            new_hand.append(11)
        elif hand[index][0] == 'T':
            new_hand.append(10)
        else:
            new_hand.append(int(hand[index][0]))
    #print(new_hand,"My new_hand")
    return new_hand
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check
        if it a straight
        Write the code for it and return True if it is a straight 
        else return False
    '''
    count = len(hand)
    #print(count)
    sorti = sorted(sort(hand))
    #print(sorti)
    #print("<---------->")
    for index in range(count-1):
        if sorti[index+1] - sorti[index] != 1:
            return False
    return True

def is_threeof_kind(hand):
    '''This funtion returns id three of a kind function calls'''
    count = 0
    sorti=[]
    sorti = sorted(sort(hand))
    #print(sorti)
    for index in range(len(sorti)-2):
        if sorti[index] == sorti[index+1] == sorti[index+2]:
            count += 1
    if count == 1:
        return True
    return False

def is_fourof_kind(hand):
    '''This funtion returns when four of a kind function calls'''
    count = 0
    sorti = sorted(sort(hand))
    for index in range(len(sorti)-3):
        if sorti[index] == sorti[index+1] == sorti[index+2] == sorti[index+3]:
            count += 1
    if count ==1:
        return True
    return False

def is_onepair(hand):
    '''This funtion returns when one pair of a kind function calls'''
    _ = 0
    sorti = sorted(sort(hand))
    setlist = set(sorti)
    #print(setlist)
    if len(sorti) - len(setlist) == 1:
        for index in setlist:
            if sorti.count(index) == 2:
            return index/10
    return 100

def is_highcard(hand):
    '''This funtion returns when is high card of a kind function calls'''
    sorti = sorted(sort(hand))
    setlist = set(sorti)
    if len(setlist) == 5 and not is_flush(hand):
        return max(setlist)/100
    return False

def is_twopair(hand):
    '''This funtion returns when three of a kind function calls'''
    sorti = sorted(sort(hand))
    setlist = set(sorti)
    if len(sorti) - len(setlist) == 2:
        return True
    return False

def is_fullhouse(hand):
    '''This funtion returns when fullhouse of a kind function calls'''
    count = 0
    i = 0
    sorti = sorted(sort(hand))
    if sorti[i] == sorti[i+1] == sorti[i+2] or sorti[i+3] == sorti[i+4]:
        count += 1
    elif sorti[i+4] == sorti[i+3] and sorti[i+2] == sorti[i+1] == sorti[i]:
        count += 1
    if count == 1:
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check
        if it is a flush
        Write the code for it and return
        True if it is a flush else return False
    '''
    len_count = len(hand)
    for index in range(len_count-1):
        if hand[index][1] != hand[index+1][1]:
            return False
    return True

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given
        hand is a straight
        or a flush or a straight flush.
    '''
    if is_threeof_kind(hand):
        return 3
    if is_onepair(hand) != 100:
        return is_onepair(hand)
    if is_twopair(hand):
        return 2
    if is_fullhouse(hand):
        return 7
    if is_fourof_kind(hand):
        return 4
    if is_flush(hand) and is_straight(hand):
        return 8
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    return is_highcard(hand)
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    # print(hands)
    # print(max(hands))
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    #print(HANDS)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
