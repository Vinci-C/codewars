def get_participants(handshakes):
    i,k = 0,1
    if handshakes == 0: return 0
    else:
        while i < handshakes:
            i += k
            k += 1
        return k
