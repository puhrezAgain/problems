nums = [2, 7, 11, 15]
target = 9


def two_sum(ns, t):
    # a map of numbers needed to sum to target -> index of number needed to sum to target
    missing_sums = {}
    for i, n in enumerate(ns):
        # if we have already encountered a number need the number at hand, we done
        if n in missing_sums: 
            return (i, missing_sums[n])
        # otherwise accumulate
        missing_sums[t - n] = i

print(two_sum(nums, target))
