def remove_element(xs: list[int], v: int) -> int:
    """
    Remove all occurrences of v in-place.
    Return the new length.
    """
    # After each iteration, indexes prefixing index i in xs will not contain v, in original order.
    # Each iteration checks if the current value is not v, if so writes to the current write index w and increments it, 
    # otherwise the write index is not incremented.

    w = 0
    for x in xs: 
        if x != v:
            xs[w] = x
            w += 1

    return w


# Basic case
xs = [3, 2, 2, 3]
assert remove_element(xs, 3) == 2
assert xs[:2] == [2, 2]

# No removals
xs = [1, 2, 3, 4]
assert remove_element(xs, 5) == 4
assert xs[:4] == [1, 2, 3, 4]

# Empty list
xs = []
assert remove_element(xs, 1) == 0

# Single element kept
xs = [1]
assert remove_element(xs, 2) == 1
assert xs[:1] == [1]

# Single element removed
xs = [1]
assert remove_element(xs, 1) == 0

# All elements removed
xs = [2, 2, 2, 2]
assert remove_element(xs, 2) == 0

# No elements removed (order preserved)
xs = [1, 3, 5, 7]
assert remove_element(xs, 2) == 4
assert xs[:4] == [1, 3, 5, 7]

# Alternating values (stability check)
xs = [1, 2, 1, 2, 1, 2]
assert remove_element(xs, 2) == 3
assert xs[:3] == [1, 1, 1]

# Leading and trailing removals
xs = [0, 0, 1, 2, 3, 0]
assert remove_element(xs, 0) == 3
assert xs[:3] == [1, 2, 3]
