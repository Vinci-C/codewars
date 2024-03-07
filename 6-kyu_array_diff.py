#mycode
def array_diff(a, b):
    c = []
    for i in range(len(a)):
        if a[i] not in b:
            c.append(a[i])
    return c

#best solution
def array_diff(a, b):
    return [i for i in a if i not in b]
#takeaway: try to compact code
