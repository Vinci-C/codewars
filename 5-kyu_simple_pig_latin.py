#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
def pig_it(text):
    text, rev, result =  text.split(" "), "", []
    for i in text:
        rev = i[1:] + i[0] + "ay"
        result.append(rev)
    result = " ".join(result)
    if result[-3].isalpha() == False:
        return(result.strip("ay"))
    else: return(result)
