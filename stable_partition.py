from typing import Callable

def stable_partition(xs: list[int], f: Callable[[int], bool]) -> int:
    """
    Move all even numbers to the front, in-place, preserving order.
    Return the length of the even prefix.

    Every index before the write index satisfied the predicate in original order. 
    Each iteration advances the write index if and only if the value at the read index satisfies the predicate. 
    Iteration finished when all the possible read indexes have been evaluated, and the write index indicates where the failed remainder begins. 
    """
    w = 0

    for x in xs:
        if f(x):
            xs[w] = x
            w += 1

    return w

def stable_partition_even(xs):
    return stable_partition(xs, lambda x: not (x % 2))

print("Test: empty list")
xs = []
assert stable_partition_even(xs) == 0

print("Test: no evens")
xs = [1, 3, 5]
assert stable_partition_even(xs) == 0
assert xs[:0] == []

print("Test: all evens")
xs = [2, 4, 6]
assert stable_partition_even(xs) == 3
assert xs[:3] == [2, 4, 6]

print("Test: mixed, evens interleaved")
xs = [1, 2, 3, 4, 5, 6]
assert stable_partition_even(xs) == 3
assert xs[:3] == [2, 4, 6]

print("Test: evens already at front")
xs = [2, 4, 1, 3]
assert stable_partition_even(xs) == 2
assert xs[:2] == [2, 4]

print("Test: evens at end")
xs = [1, 3, 5, 2, 4]
assert stable_partition_even(xs) == 2
assert xs[:2] == [2, 4]

print("Test: single even")
xs = [1, 3, 4, 5]
assert stable_partition_even(xs) == 1
assert xs[:1] == [4]

print("Test: single odd")
xs = [2, 3, 5]
assert stable_partition_even(xs) == 1
assert xs[:1] == [2]

print("Test: repeated values")
xs = [2, 2, 1, 1, 4, 4]
assert stable_partition_even(xs) == 4
assert xs[:4] == [2, 2, 4, 4]

print("All tests passed ✅")
