from OpcodeVM import OpcodeVM
import numpy as np
import matplotlib.pyplot as plt
import collections


# setup
memory = [int(x) for x in open("day13_input_hack.txt").read().split(",")]
ram = [0] * 1000
memory = memory + ram
m = OpcodeVM(memory)
tiles = collections.defaultdict()

block_cnt = 0
while not m.finished:
    for [tile_id, x_pos, y_pos] in m.exec_next():
        tiles[(x_pos, y_pos)] = tile_id
        if tile_id == 2:
            block_cnt = block_cnt + 1


# visualisation
max_x = max([abs(x) for (x, _) in tiles.keys()])
max_y = max([abs(y) for (_, y) in tiles.keys()])
mat = np.array(list(tiles.values())).reshape((max_x + 1, max_y + 1))

print(block_cnt)
plt.matshow(mat)
plt.show()
