print("Test: empty list")
xs = []
partition_even_odd(xs)
assert xs == []

print("Test: single even")
xs = [2]
partition_even_odd(xs)
assert xs == [2]

print("Test: single odd")
xs = [3]
partition_even_odd(xs)
assert xs == [3]

print("Test: all evens")
xs = [2, 4, 6]
partition_even_odd(xs)
assert all(x % 2 == 0 for x in xs)

print("Test: all odds")
xs = [1, 3, 5]
partition_even_odd(xs)
assert all(x % 2 == 1 for x in xs)

print("Test: mixed simple")
xs = [3, 1, 2, 4]
partition_even_odd(xs)
k = 0
while k < len(xs) and xs[k] % 2 == 0:
    k += 1
assert all(xs[i] % 2 == 0 for i in range(k))
assert all(xs[i] % 2 == 1 for i in range(k, len(xs)))

print("Test: mixed already partitioned")
xs = [2, 4, 6, 1, 3, 5]
partition_even_odd(xs)
k = 0
while k < len(xs) and xs[k] % 2 == 0:
    k += 1
assert all(xs[i] % 2 == 0 for i in range(k))
assert all(xs[i] % 2 == 1 for i in range(k, len(xs)))

print("Test: alternating")
xs = [1, 2, 1, 2, 1, 2]
partition_even_odd(xs)
k = 0
while k < len(xs) and xs[k] % 2 == 0:
    k += 1
assert all(xs[i] % 2 == 0 for i in range(k))
assert all(xs[i] % 2 == 1 for i in range(k, len(xs)))

print("Test: repeated values")
xs = [2, 1, 2, 1, 2, 1]
partition_even_odd(xs)
k = 0
while k < len(xs) and xs[k] % 2 == 0:
    k += 1
assert all(xs[i] % 2 == 0 for i in range(k))
assert all(xs[i] % 2 == 1 for i in range(k, len(xs)))

print("All tests passed ✅")
