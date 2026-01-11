from collections import Counter
def min_window(s: str, t: str) -> str:    
    """
    Return the shortest substring of s that contain characters of t, ensuring at least required number of occurances of all characters in t and, just to be explicit, potentially have characters only in s. 
    Like always with window problems, two pointers L and R determine our current valid window, everything before is irrelevant and everything after is unknown. 
    Evaluation ends when every element is known. 

    Original spec
    A valid window is one where the indexes between L and R contain every character in t all(current_window_char[k] >= v for k, v in t_char_count.items())
    A invalid window is one that the indexes between L and R where at least one t character's required count is not met
    R advances whether or not it increments or adds t characters to current_window_char 
    If validity is achieved, while not removing a character would break validity, L advances whether or not it decreases or removes t chars from current_window_char when t characters are encountered, 
    updating the smallest substring if the current window is smalller.

    TODO REDO, solved but not well at first
    """
    L, R = 0, 0
    t_count = Counter(t)
    smallest_subset = ""
    missing = len(t)

    if not t:
        return ""
    
    for R, ch in enumerate(s):
        # had four main problems here, 
        # 1. the use of two loops, one for until valid and one for until not valid, had termination problems
        # solved by using a until unvalid loop within a is valid confitional
        # 2. ordering to ensure cases like validity case functioned properly
        # solved by moving R operations before validity check
        # 3. smallest subset being ""
        # solved by instatiating correctly in after validity check 
        # 4. non optimal state, had both a t_char_count and a window_char_count
        # solved by using Counter of t t_count, which maintains a t_char_count
        # decrementing during invalidity/incrementing during validity to represent the current windows count
        # in parallel a missing counter is maintained to represent validity
        if ch in t_count:
            if t_count[ch] > 0:
                missing -= 1    
            t_count[ch] -= 1

        while not missing:
            curr_window = s[L:R+1]
            if not smallest_subset or len(smallest_subset) > len(curr_window):
                smallest_subset = curr_window

            if s[L] in t_count:
                t_count[s[L]] += 1
                if t_count[s[L]] > 0:
                    missing +=1
            L += 1
        
    return smallest_subset
 

print("Test: both strings empty")
assert min_window("", "") == ""

print("Test: empty s")
assert min_window("", "a") == ""

print("Test: empty t")
assert min_window("abc", "") == ""

print("Test: s shorter than t")
assert min_window("a", "aa") == ""

print("Test: exact match")
assert min_window("abc", "abc") == "abc"

print("Test: single character match")
assert min_window("a", "a") == "a"

print("Test: single character no match")
assert min_window("a", "b") == ""

print("Test: basic example")
assert min_window("ADOBECODEBANC", "ABC") == "BANC"

print("Test: repeated characters in t")
assert min_window("AAABBC", "AABC") == "AABBC"

print("Test: multiple possible windows, choose shortest")
assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"

print("Test: window at start")
print(min_window("abcde", "ab"))
assert min_window("abcde", "ab") == "ab"

print("Test: window at end")
assert min_window("abcde", "de") == "de"

print("Test: window in middle")
assert min_window("xxabcxx", "abc") == "abc"

print("Test: overlapping valid windows")
assert min_window("abdabca", "abc") == "abc"

print("Test: non-t characters padding")
assert min_window("xxAxxBxxCxx", "ABC") == "AxxBxxC"

print("Test: unicode characters")
assert min_window("åß∂ƒåß∂", "ß∂") == "ß∂"

print("Test: case sensitivity")
assert min_window("aAbBcC", "ABC") == "AbBcC"

print("Test: duplicate letters in s, single in t")
assert min_window("aaab", "ab") == "ab"

print("Test: t characters scattered")
assert min_window("this is a test string", "tist") == "t stri"

print("Test: no possible window")
assert min_window("abcdef", "xyz") == ""

print("All tests passed ✅")
