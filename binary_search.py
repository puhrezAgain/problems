def binary_search(xs: list[int], target: int) -> int:
    """
    xs is sorted in ascending order.
    Return the index of target if present, else -1.
    """
    # invariant: if the list is populated, 
    # values above index U > target; values below index L < target
    # if target exists is within U and L, which shrinks between iteration
    U = len(xs) - 1
    L = 0
    if not xs:
        return -1
    
    while L <= U:
        partition = L + (U - L) // 2

        if target == xs[partition]:
            return partition
    
        if target < xs[partition]:
            U = partition - 1
        else:
            L = partition + 1


    return -1


assert binary_search([], 5) == -1
assert binary_search([1], 1) == 0
assert binary_search([1], 2) == -1
assert binary_search([1, 2], 2) == 1
assert binary_search([1, 3, 5, 7], 5) == 2
assert binary_search([1, 3, 5, 7], 1) == 0
assert binary_search([1, 3, 5, 7], 7) == 3
assert binary_search([1, 3, 5, 7], 4) == -1
