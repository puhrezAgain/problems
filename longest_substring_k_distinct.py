def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Return the length of longest substring where there are at most k unique characters in a string xs. 
    
    Two pointers L, a pointer to the start of the current window, and R, a pointer the next possible window element, determine our current validity window. 
    Everything before is owned but irrelevant and afterthing after is unknown. We iterate until each index is known. 
    A valid window is when in the indexes between L and R there are at most k distinct elements, tracked as a char->count map. 
    After tracking the value at R, if the window is invalid, L advances while there are more than k distinct elements to repair the validity window. 
    When valid, R advances and max_length updates if the current window is longer
    """
    L, R = 0, 0
    char_count = dict()
    max_length = 0

    while R < len(s):
        char_count[s[R]] = char_count.get(s[R], 0) + 1

        while len(char_count) > k:
            char_count[s[L]] -= 1
            if not char_count[s[L]]:
                del char_count[s[L]]
            L += 1
            
        R += 1
        max_length = max(max_length, R - L)
            
    return max_length


print("Test: empty string")
assert longest_substring_k_distinct("", 2) == 0

print("Test: k = 0")
assert longest_substring_k_distinct("abc", 0) == 0

print("Test: single character, k = 1")
assert longest_substring_k_distinct("a", 1) == 1

print("Test: single character, k > 1")
assert longest_substring_k_distinct("a", 5) == 1

print("Test: all same characters")
assert longest_substring_k_distinct("aaaaaa", 1) == 6

print("Test: all unique, k large enough")
assert longest_substring_k_distinct("abcdef", 10) == 6

print("Test: all unique, k too small")
assert longest_substring_k_distinct("abcdef", 2) == 2

print("Test: basic example")
assert longest_substring_k_distinct("eceba", 2) == 3  # "ece"

print("Test: shrinking required multiple times")
assert longest_substring_k_distinct("aaabbbcccd", 2) == 6  # "aaabbb" or "bbbccc"

print("Test: alternating characters")
assert longest_substring_k_distinct("abababab", 2) == 8

print("Test: alternating with k = 1")
assert longest_substring_k_distinct("abababab", 1) == 1

print("Test: overlapping windows")
assert longest_substring_k_distinct("abcadcacacaca", 3) == 11

print("Test: numbers and letters")
assert longest_substring_k_distinct("a1b2c3d4", 4) == 4

print("Test: unicode characters")
assert longest_substring_k_distinct("åß∂ƒåß∂", 3) == 3


print("Test: k equals distinct count")
assert longest_substring_k_distinct("abcabcbb", 3) == 8

print("Test: k equals distinct count minus one")
assert longest_substring_k_distinct("abcabcbb", 2) == 4

print("All tests passed ✅")
