from OpcodeVM_part2 import OpcodeVM
import numpy as np
import matplotlib.pyplot as plt
import collections


def render(tiles):
    mat = np.array(list(tiles.values())).reshape((25, 42))
    plt.matshow(mat)
    plt.show()


# setup
memory = [int(x) for x in open("day13_input_hack.txt").read().split(",")]
ram = [0] * 1000
memory = memory + ram
memory[0] = 2
m = OpcodeVM(memory)
tiles = collections.defaultdict()

score = 0
while not m.finished:
    m.set_input(0)
    for [tile_id, x_pos, y_pos] in m.exec_next():
        if y_pos == -1 and x_pos == 0:
            score = tile_id
        else:
            tiles[(x_pos, y_pos)] = tile_id
        # try:
        #     render(tiles)
        # except:
        #     pass

print(score)
