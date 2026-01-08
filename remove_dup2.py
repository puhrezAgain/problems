from typing import List 
def remove_single_dup(xs):
    if len(xs) < 2:
        return len(xs)
    w = 1

    for x in xs[1:]:
        if x != xs[w - 1]:
            xs[w] = x
            w += 1

    return w

def remove_dup(xs: List[int], n=2) -> int:
    if len(xs) < n:
        return len(xs)
    
    w = n
    for x in xs[n:]:
        if all(x == xs[w - i] for i in range(1, n+1)):
            continue
        xs[w] = x   
        w += 1
    return w

print("Test: empty list")
xs = []
assert remove_dup(xs) == 0

print("Test: single element")
xs = [1]
assert remove_dup(xs) == 1
assert xs[:1] == [1]

print("Test: two same elements (allowed)")
xs = [1, 1]
assert remove_dup(xs) == 2
assert xs[:2] == [1, 1]

print("Test: three same elements (one removed)")
xs = [1, 1, 1]
assert remove_dup(xs) == 2
assert xs[:2] == [1, 1]

print("Test: multiple duplicates")
xs = [1, 1, 1, 2, 2, 3]
assert remove_dup(xs) == 5
assert xs[:5] == [1, 1, 2, 2, 3]

print("Test: long run of duplicates")
xs = [2, 2, 2, 2, 2]
assert remove_dup(xs) == 2
assert xs[:2] == [2, 2]

print("Test: alternating values")
xs = [1, 1, 2, 2, 3, 3]
assert remove_dup(xs) == 6
assert xs[:6] == [1, 1, 2, 2, 3, 3]

print("Test: mixed case (classic example)")
xs = [0,0,1,1,1,1,2,3,3]
assert remove_dup(xs) == 7
assert xs[:7] == [0,0,1,1,2,3,3]

print("Test: already valid (no removals)")
xs = [1,1,2,2,3,3]
assert remove_dup(xs) == 6
assert xs[:6] == [1,1,2,2,3,3]

print("Test: values change after rejection")
xs = [1,1,1,2,2,2,3,3,3]
assert remove_dup(xs) == 6
assert xs[:6] == [1,1,2,2,3,3]

print("All tests passed ✅")
