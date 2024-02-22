#Final solution
def strip_comments(strng, markers):
    str_list = strng.split('\n')
    for marker in markers:
        str_list = [item.split(marker)[0].rstrip() for item in str_list]
    return '\n'.join(str_list)
pass
# Initial idea was to run for item in stringlist as the outer loop, but realised that you can't have two variables as split()
# https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/ helped a lot
