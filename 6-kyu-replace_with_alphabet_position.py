#own solution
import string
def alphabet_position(text):
    index_s = ""
    for i in text.lower():
        if i in string.ascii_lowercase:
            index_s += str(string.ascii_lowercase.index(i)+1) + ' '
    return index_s.rstrip()

#best solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
  
