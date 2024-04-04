def find_nb(m):
    n = 1
    total_volume = 0
    while total_volume < m:
        total_volume += n ** 3
        if total_volume == m:
            return n
        n += 1
    return -1
