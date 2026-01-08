def dutch_national_flag(xs: list[int]) -> None:
    L, M, R = 0, 0, len(xs) - 1

    while M <= R:
        if xs[M] == 1:
            M += 1
        elif xs[M] == 0:
            xs[L], xs[M] = xs[M], xs[L]
            L += 1
            M += 1
        elif xs[M] == 2:
            xs[R], xs[M] = xs[M], xs[R]
            R -= 1

print("Test: empty list")
xs = []
dutch_national_flag(xs)
assert xs == []

print("Test: single element 0")
xs = [0]
dutch_national_flag(xs)
assert xs == [0]

print("Test: single element 1")
xs = [1]
dutch_national_flag(xs)
assert xs == [1]

print("Test: single element 2")
xs = [2]
dutch_national_flag(xs)
assert xs == [2]

print("Test: already sorted")
xs = [0, 0, 1, 1, 2, 2]
dutch_national_flag(xs)
assert xs == [0, 0, 1, 1, 2, 2]

print("Test: reverse order")
xs = [2, 2, 1, 1, 0, 0]
dutch_national_flag(xs)
# verify partition
i = 0
while i < len(xs) and xs[i] == 0:
    i += 1
while i < len(xs) and xs[i] == 1:
    i += 1
while i < len(xs) and xs[i] == 2:
    i += 1
assert i == len(xs)

print("Test: mixed simple")
xs = [2, 0, 2, 1, 1, 0]
dutch_national_flag(xs)
i = 0
while i < len(xs) and xs[i] == 0:
    i += 1
while i < len(xs) and xs[i] == 1:
    i += 1
while i < len(xs) and xs[i] == 2:
    i += 1
assert i == len(xs)

print("Test: alternating values")
xs = [0, 1, 2, 0, 1, 2]
dutch_national_flag(xs)
i = 0
while i < len(xs) and xs[i] == 0:
    i += 1
while i < len(xs) and xs[i] == 1:
    i += 1
while i < len(xs) and xs[i] == 2:
    i += 1
assert i == len(xs)

print("Test: all zeros")
xs = [0, 0, 0, 0]
dutch_national_flag(xs)
assert xs == [0, 0, 0, 0]

print("Test: all ones")
xs = [1, 1, 1, 1]
dutch_national_flag(xs)
assert xs == [1, 1, 1, 1]

print("Test: all twos")
xs = [2, 2, 2, 2]
dutch_national_flag(xs)
assert xs == [2, 2, 2, 2]

print("Test: random distribution")
xs = [1, 2, 0, 1, 2, 0, 1, 2, 0]
dutch_national_flag(xs)
i = 0
while i < len(xs) and xs[i] == 0:
    i += 1
while i < len(xs) and xs[i] == 1:
    i += 1
while i < len(xs) and xs[i] == 2:
    i += 1
assert i == len(xs)

print("All tests passed ✅")
