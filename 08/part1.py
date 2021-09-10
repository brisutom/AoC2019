import numpy as np

img_data = [int(x) for x in open("input.txt").read().strip("\n")]
w = 25
h = 6

img_data = np.array(img_data).reshape((-1, w, h))

digits = []
for layer in img_data:
    num_zero = (layer == 0).sum()
    num_one = (layer == 1).sum()
    num_two = (layer == 2).sum()
    digits.append([num_zero, num_one, num_two])

print(min(digits)[1] * min(digits)[2])
