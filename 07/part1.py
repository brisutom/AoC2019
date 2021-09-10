import itertools


def opcodeMachine(val1, val2):
    sample = [int(x) for x in open("input.txt").read().split(",")]
    vals = [val1, val2]
    i = 0
    outputs = []
    opcodes = []

    while i < len(sample):
        instruction = str(sample[i])
        opcode = int(instruction[-2:])
        modes = instruction[:-2][::-1]
        opcodes.append(opcode)

        if opcode == 99:
            break

        if opcode in [1, 2, 4, 5, 6, 7, 8]:
            length = 4
            try:
                if modes[0] == "1":
                    par1 = sample[i+1]
                else:
                    par1 = sample[sample[i+1]]
            except Exception:
                par1 = sample[sample[i+1]]

            if opcode not in [3, 4]:
                try:
                    if modes[1] == "1":
                        par2 = sample[i+2]
                    else:
                        par2 = sample[sample[i+2]]
                except Exception:
                    par2 = sample[sample[i+2]]

            dest = sample[i+3]

        if opcode == 1:
            sample[dest] = par1 + par2

        elif opcode == 2:
            sample[dest] = par1 * par2

        elif opcode == 3:
            length = 2
            par1 = sample[i+1]
            sample[par1] = vals.pop(0)

        elif opcode == 4:
            length = 2
            outputs.append(par1)

        elif opcode == 5:
            if par1 != 0:
                length = 0
                i = par2
            else:
                length = 3

        elif opcode == 6:
            if par1 == 0:
                length = 0
                i = par2
            else:
                length = 3

        elif opcode == 7:
            if par1 < par2:
                sample[dest] = 1
            else:
                sample[dest] = 0

        elif opcode == 8:
            if par1 == par2:
                sample[dest] = 1
            else:
                sample[dest] = 0

        i += length

    return outputs[-1]


def trySequence(seq):
    val2 = 0
    for val1 in seq:
        val2 = opcodeMachine(val1, val2)

    return val2


results = []
sequences = itertools.permutations(range(5))
for seq in sequences:
    results.append(trySequence(seq))

print(max(results))
