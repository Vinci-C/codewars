#A very tricky kata!
#Initial idea of not using re, pascal triangle not yet added
def expand(expr):
    if int(expr.split("^")[1]) == 0:
        return "1"
    else:
        a = int(list(expr)[1])
        x = list(expr)[2]
        b = int(list(expr)[4])
        n = int(list(expr)[7])
        if n == 1:
            return str(expr.split("^")[0][1:].replace("(", "").replace(")", ""))
        for i in range(1, n+2):
            if i == 1:
                result = str(f"{a**(n)}{x}^{n} + ")
            elif i != 1 and i != n+1:
                result += str(f"{a**(n-i+2)*b}{x}^{i} + ")
            else:
                result += str(f"{b**n}")
        return result  
#works quite well, only problem is that it returns x^1 when it should return x
#best solution
import re
P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

def expand(expr):
    a,v,b,e = P.findall(expr)[0]
    
    if e=='0': return '1'
    
    o   = [int(a!='-' and a or a and '-1' or '1'), int(b)]
    e,p = int(e), o[:]
    
    for _ in range(e-1):
        p.append(0)
        p = [o[0] * coef + p[i-1]*o[1] for i,coef in enumerate(p)]
    
    res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef in enumerate(p) if coef)
    
    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
