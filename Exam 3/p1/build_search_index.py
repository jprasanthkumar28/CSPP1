'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
    }
'''
import string
import collections
# helper function to load the stop words from a file
def load_stopwords(stopwords):
    '''
        loads stop words from a file and returns a dictionary
    '''
    dup_stopwords = []
    with open(stopwords, 'r') as f_stopwords:
        for line in f_stopwords:
            dup_stopwords.append(line.strip())
    return dup_stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    char = string.ascii_letters + ' '
    text = ''.join(index for index in text if index in char)
    text = text.lower().split()
    finaldict = load_stopwords("stopwords.txt")
    for word in list(text):
        if word in finaldict:
            text.remove(word)
    return text
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    dict1 = {}
    length = len(docs)
    for index in range(length):
        res = word_list(docs[index])
        for value in res:
            word1 = res.count(value)
            if value in dict1:
                if (index, word1) not in dict1[value]:
                    dict1[value].append(index, word1)
            else:
                dict1[value] = [(index, word1)]
        dict1 = load_stopwords(dict1)
    return dict1
    # for count,l_index in enumerate(docs, 0):
    #     dic = {}
    #     for e_index in l_index:
    #         if e_index not in dic:
                
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for _ in range(lines):
        documents.append(input())
        #i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
