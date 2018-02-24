# put your code here.

filename = "twain.txt"


def count_words(file):

    file = open(filename, "r")
    word_count = {}

    #loop through lines in file
    for line in file:
        #remove /n from line
        line = line.rstrip()
        #create a list of words split on white space
        words = line.split()
        #iterate through list of words add word and count to dictioary
        #if word does not exist in dictionary default to 0, otherwise increment by 1
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.iteritems():
        print " {} {}".format(key, value)

    return word_count

count_words(filename)
