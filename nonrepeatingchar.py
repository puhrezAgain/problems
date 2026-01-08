from typing import OrderedDict
def getFirstNonRepeatChar(s):
    """returns the index of the first character to not repeat in s, otherwise -1"""
    seen = set()
    unique_index = OrderedDict()
    
    for i, c in enumerate(s):
        if c in seen:
            del unique_index[c]
        else:
            unique_index[c] = i
            seen.add(c)
            
    if unique_index:
        return unique_index.popitem(last=False)
    return -1

assert getFirstNonRepeatChar("leetcode") == 0
assert getFirstNonRepeatChar("loveleetcode") == 2
assert getFirstNonRepeatChar("aabb") == -1
