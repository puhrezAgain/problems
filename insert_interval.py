from typing import List, Tuple

def insert_interval(intervals: List[Tuple[int, int]], input_interval: Tuple) -> List[Tuple[int, int]]:
    """
    The active interval is the unplaced insert interval. 
    Sort the input list and interate. 
    If an interval begins after our active interval ends, 
    we finalize the active_interval by returing the list until prefix, the active_interval, and the untouched suffix.
    If an interval overlaps, we finalize the prefix by setting prefix limit and merge and the result becomes out active_interval
    Otherwise we increment the prefix limit to finalize earlier intervals
    If we exahaust the list that means the tuple belongs at the end, we return the list with the interval at end
    """
    active_interval: Tuple[int, int] = input_interval
    intervals.sort(key=lambda x: x[0])
    prefix_limit = 0

    for i, interval in enumerate(intervals):
        if active_interval[1] < interval[0]:
            return intervals[:prefix_limit] + [active_interval] + intervals[i:]
        if interval[0] <= active_interval[1] and active_interval[0] <= interval[1]:
            active_interval = min(interval[0], active_interval[0]),  max(interval[1], active_interval[1])
        elif interval[1] < active_interval[0]:
            prefix_limit += 1            
 
        
    return intervals[:prefix_limit] + [active_interval]


# Insert Interval — Test Cases

print("Test 1: insert into empty list")
intervals = []
new_interval = (2, 5)
assert insert_interval(intervals, new_interval) == [(2, 5)]

print("Test 2: no overlap, insert at beginning")
intervals = [(5, 7), (8, 10)]
new_interval = (1, 3)
assert insert_interval(intervals, new_interval) == [(1, 3), (5, 7), (8, 10)]

print("Test 3: no overlap, insert at end")
intervals = [(1, 2), (3, 5)]
new_interval = (6, 8)
print(insert_interval(intervals, new_interval))
assert insert_interval(intervals, new_interval) == [(1, 2), (3, 5), (6, 8)]

print("Test 4: overlap with one interval")
intervals = [(1, 3), (6, 9)]
new_interval = (2, 5)
assert insert_interval(intervals, new_interval) == [(1, 5), (6, 9)]

print("Test 5: overlap with multiple intervals")
intervals = [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)]
new_interval = (4, 8)
assert insert_interval(intervals, new_interval) == [(1, 2), (3, 10), (12, 16)]

print("Test 6: new interval absorbs all intervals")
intervals = [(1, 3), (6, 9)]
new_interval = (0, 20)
assert insert_interval(intervals, new_interval) == [(0, 20)]

print("Test 7: new interval fully inside existing interval")
intervals = [(1, 10)]
new_interval = (3, 5)
assert insert_interval(intervals, new_interval) == [(1, 10)]

print("Test 8: touching boundaries (closed intervals)")
intervals = [(1, 2), (3, 5)]
new_interval = (2, 3)
assert insert_interval(intervals, new_interval) == [(1, 5)]

print("Test 9: new interval equals existing interval")
intervals = [(1, 3), (5, 7)]
new_interval = (1, 3)
assert insert_interval(intervals, new_interval) == [(1, 3), (5, 7)]

print("Test 10: single interval, no overlap before")
intervals = [(5, 7)]
new_interval = (1, 3)
assert insert_interval(intervals, new_interval) == [(1, 3), (5, 7)]

print("Test 11: single interval, no overlap after")
intervals = [(1, 3)]
new_interval = (5, 7)
assert insert_interval(intervals, new_interval) == [(1, 3), (5, 7)]

print("Test 12: single interval, overlap")
intervals = [(5, 7)]
new_interval = (6, 8)
assert insert_interval(intervals, new_interval) == [(5, 8)]

print("Test 13: new interval overlaps prefix only")
intervals = [(1, 4), (6, 8), (10, 12)]
new_interval = (2, 3)
assert insert_interval(intervals, new_interval) == [(1, 4), (6, 8), (10, 12)]

print("Test 14: new interval overlaps suffix only")
intervals = [(1, 2), (4, 6), (8, 10)]
new_interval = (9, 12)
assert insert_interval(intervals, new_interval) == [(1, 2), (4, 6), (8, 12)]

print("Test 15: new interval overlaps middle only")
intervals = [(1, 2), (4, 6), (8, 10)]
new_interval = (5, 5)
assert insert_interval(intervals, new_interval) == [(1, 2), (4, 6), (8, 10)]

print("Test: interval becomes problematic after active grows")

intervals = [(1, 2), (5, 6), (8, 9)]
new_interval = (3, 4)
assert insert_interval(intervals, new_interval) == [(1, 2), (3, 4), (5, 6), (8, 9)]

print("Test: active grows, creating a silent suffix interval")

intervals = [(1, 2), (4, 7), (8, 9)]
new_interval = (3, 5)
assert insert_interval(intervals, new_interval) == [(1, 2), (3, 7), (8, 9)]


print("Test passed :)")

