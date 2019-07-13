def scramble(s1, s2):
    # sort the strings as lists
    l1, l2 = sorted(list(s1)), sorted(list(s2))
    # iterate thru both concurrently, removing items from l1 as necessary
    idx1, idx2 = 0, 0
    while idx1 < len(s1) and idx2 < len(s2):
        # check if s1 char == s2 char
        if l1[idx1] == l2[idx2]:
            # bump up both indices
            idx1 += 1
            idx2 += 1
        # otherwise, move forwards in s1
        else:
            idx1 += 1
    # check if all s2 has been 'seen' via idx2
    if idx2 == len(s2):
        return True
    # otherwise, there's chars left to be 'seen'
    else:
        return False