#initial idea
def duplicate_encode(word):
    word=word.lower()
    encode = ("")
    for i in range(len(word)):
        if word.count(word[i]) == 1: encode += "("
        else: encode += ")"
    return encode

#concatenated version
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
