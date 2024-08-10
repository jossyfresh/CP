from collections import Counter
def subString(s):
    freqTable = Counter(s)
    counter = 0
    for char in freqTable:
        val = freqTable[char]
        val = (val*(val+1)) // 2
        counter += val
        
    return counter
s = "abcba"

print(subString(s))