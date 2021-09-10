from OpcodeVM import OpcodeVM

memory = [int(x) for x in open("input.txt").read().split(",")]
ram = [0]*1000
memory = memory + ram
m = OpcodeVM(memory)
# input 1 for part1
# input 2 for part2
m.set_input(1)

while not m.finished:
    # m.printState()
    m.exec_next()

print(m.outputValues)
