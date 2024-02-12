#Intial idea:
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

#Final answer after doing some googling to find the best solution:
import string
def is_pangram(s):
    return(set(s.lower()) >= set(string.ascii_lowercase))
