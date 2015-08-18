string = "abcdefggf"


# Get next greatest permutation
def rec_permute(sofar, rest, original):

    found = False
    if len(rest) == 0:
        if sofar > original:
            return sofar
        else:
            sofar=""
            return sofar
    else:
        for i in range(len(rest)):
            remaining = rest[0:i] + rest[i+1:]
            found = rec_permute(sofar+rest[i], remaining, original)
            if len(found)>0:
                return found

    return ""

print rec_permute("", string, string)