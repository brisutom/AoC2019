import numpy as np
import matplotlib.pyplot as plt

img_data = [int(x) for x in open("input.txt").read().strip("\n")]
w = 25
h = 6
N = w*h

img_data = np.array(img_data).reshape((-1, N))
final_img = np.zeros(N)


for layer in img_data[::-1]:
    for i, pixel in enumerate(layer):
        if pixel == 0 or pixel == 1:
            final_img[i] = pixel

print(final_img.reshape((h, w)))
plt.matshow(final_img.reshape((h, w)))
plt.show()
