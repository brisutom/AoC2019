import operator
sample = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 19, 5, 23, 2, 6, 23, 27, 1, 6, 27, 31, 2, 31, 9, 35, 1, 35, 6, 39, 1, 10, 39, 43, 2, 9, 43, 47, 1, 5, 47, 51, 2, 51, 6, 55, 1, 5, 55, 59, 2, 13, 59, 63, 1, 63, 5, 67, 2, 67, 13, 71, 1, 71, 9, 75, 1, 75, 6, 79, 2, 79, 6, 83, 1, 83, 5, 87, 2, 87, 9, 91, 2, 9, 91, 95, 1, 5, 95, 99, 2, 99, 13, 103, 1, 103, 5, 107, 1, 2, 107, 111, 1, 111, 5, 0, 99, 2, 14, 0, 0]

i = 0
while i < len(sample):
    code = sample[i]
    if code == 99:
        break
    else:
        ind1 = sample[i+1]
        ind2 = sample[i+2]
        dest = sample[i+3]

        if code == 1:
            op = operator.add
        elif code == 2:
            op = operator.mul

        sample[dest] = op(sample[ind1],  sample[ind2])

    i = i+4

print(sample[0])
