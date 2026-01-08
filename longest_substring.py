def longest_unique_substring(s: str) -> int:
    """
    returns the length of the longest unique substring

    Every index before L is irrelevant, every index after R is unknown, 
    everything inbetween is valid and relevant
    The window is valid iff every element is unique
    If R points to a value that would invalidate the window, L advances while the window is invalid, updating current_window
    R advances when the window is valid, updaing max_window_len 
    Termination occurs when all elements are seen
    """
    L, R = 0, 0
    current_window = set()
    max_window_len = 0
    
    while R < len(s):
        while s[R] in current_window:
            current_window.remove(s[L])
            L += 1

        current_window.add(s[R])
        R += 1
        max_window_len = max(max_window_len, R - L)
            
    return max_window_len

print("Test: empty string")
assert longest_unique_substring("") == 0

print("Test: single character")
assert longest_unique_substring("a") == 1

print("Test: all unique")
assert longest_unique_substring("abcdef") == 6

print("Test: all same characters")
assert longest_unique_substring("aaaaaa") == 1

print("Test: simple repeat")
assert longest_unique_substring("abcabcbb") == 3  # "abc"

print("Test: repeat at start")
assert longest_unique_substring("aab") == 2  # "ab"

print("Test: repeat at end")
assert longest_unique_substring("abcc") == 3  # "abc"

print("Test: overlapping repeats")
assert longest_unique_substring("pwwkew") == 3  # "wke"

print("Test: immediate duplicate")
assert longest_unique_substring("abba") == 2  # "ab" or "ba"

print("Test: duplicate forces multiple L moves")
assert longest_unique_substring("dvdf") == 3  # "vdf"

print("Test: mixed letters and numbers")
assert longest_unique_substring("a1b2c3a4") == 7  # "1b2c3a4" or similar

print("Test: spaces included")
assert longest_unique_substring("a b c a b") == 3  # "a b", "b c", etc.

print("Test: unicode characters")
assert longest_unique_substring("åß∂ƒå") == 4  # "ß∂ƒå"

print("Test: long repeating pattern")
assert longest_unique_substring("abcdeabcdeabcde") == 5

print("All tests passed ✅")
