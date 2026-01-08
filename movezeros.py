def moveZeros(xs: list):
    """Rearrange a list of ints, xs to have the 0s at the end"""
    # invariant: everything before i is final value
    i = 0
    zeros = 0

    for x in xs:
        if x == 0:
            zeros +=1 
        else:
            xs[i] = x
            i += 1

    xs[-zeros:] = ([0] * zeros)
    return xs
   
assert moveZeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert moveZeros([0, 0, 1]) == [1, 0, 0]
