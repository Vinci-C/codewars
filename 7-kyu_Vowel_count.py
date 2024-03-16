def getCount(sentence):
    return sum(char in 'aeiou' for char in sentence)
