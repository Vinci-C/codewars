# Initial idea
def is_valid_walk(walk):
    n = 0
    e = 0
    s = 0
    w = 0
    if len(walk) == 10:
        for i in range(len(walk)):
            if walk[i] == "n": n+= 1
            elif walk[i] == "e": e+= 1
            elif walk[i] == "s": s+= 1
            elif walk[i] == "w": w+= 1
        if n == s and e == w: return True
        else: return False
    else: return False

  # using COUNT
  def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
