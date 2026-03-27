def dir_reduc(arr):
    opp = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST",
    }
    
    final = []
    
    for dir in arr:
        if final and (final[-1]) == opp[dir]:
            final.pop()
        else:
            final.append(dir)
            
    return final
