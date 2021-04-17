def lastOf(pattern):
    last = {}
    i = 0
    for char in pattern:
        last.update({char: i})
        i += 1
    return last

def boyer_moore(text, pattern):
    # hitung panjang text & pattern
    n = len(text)
    m = len(pattern)

    if (n < m) :
        # jika panjang pattern lebih besar, return INVALID
        return -1
    
    last = lastOf(pattern)
    i = m - 1
    j = m - 1

    while (i <= n - 1):
        print(text[i], pattern[j])
        if (text[i] == pattern[j]): # looking glass technique
            if (j == 0):
                return i
            else :
                i -= 1
                j -= 1
        else : # character-jump technique
            if text[i] not in last:
                # case 3. text[i] not found in pattern
                i = i + m
                j = m - 1
            elif (last[text[i]] < j) :
                # case 1. last of text[i] found in leftside of pattern[j]
                i = i + m - last[text[i]] - 1
                j = m - 1
            else : # (last[text[j]] > j)
                # case 2. last of text[i] found, but not in lefside of pattern[j]
                i = i + m - j
                j = m - 1

    # if not match, return INVALID
    return -1    
