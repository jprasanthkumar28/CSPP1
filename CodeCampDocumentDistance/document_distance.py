'''
    Document Distance - A detailed description is given in the PDF
'''
import collections
import math
def similarity(dict1, dict2):
    import string
    '''
        Compute the document distance as given in the PDF
    '''
    '''file = open('hi.txt', 'r')
                text = file.read().strip()
                print(text)
                file.close()
                file = open('stopwords.txt', 'r')
                text = file.read().strip()
                print(text)
                file.close()'''
    # str2 = open("input002.txt").read()
    # text2 = str2.read().strip()
    char = string.ascii_letters + ' '
    dict1 = ''.join(index for index in dict1 if index in char)
    dict2 = ''.join(index for index in dict2 if index in char)
    dict1 = dict1.lower().strip().split('\n')
    dict2 = dict2.lower().strip().split('\n')
    # str1 = re.findall(r"^\w", dict1, re.MULTILINE)
    finaldict = load_stopwords("stopwords.txt")
    for word in list(dict1):
        if word in finaldict:
            dict1.remove(word)
    for word in list(dict2):
        if word in finaldict:
            dict2.remove(word)
    #print(dict1)
    #print(dict1, dict2)
    dict1_freq = collections.Counter(dict1)
    dict2_freq = collections.Counter(dict2)
    # print(dict1_freq, dict2_freq)
    dict1_list = []
    dict2_list = []
    dict3_list = []
    for word in dict1_freq:
        if word in dict2_freq:
            dict1_list.append(dict1_freq[word] * dict2_freq[word])

    for word in dict1_freq:
        dict2_list.append(dict1_freq[word]**2)

    for word in dict2_freq:
        dict3_list.append(dict2_freq[word]**2)
    return sum(dict1_list)/(math.sqrt(sum(dict2_list))*math.sqrt(sum(dict3_list)))


'''def data_format(data):
    lower = data.lower()
    case = re.sub('[^a-z/ ]', '', lower)
    return case'''


def load_stopwords(stopwords):
    '''
        loads stop words from a file and returns a dictionary
    '''
    dup_stopwords = []
    with open(stopwords, 'r') as words:
        for line in words:
            dup_stopwords.append(line.strip())
    return dup_stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
