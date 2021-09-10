sample = [int(x) for x in open("input.txt").read().split(",")]
i = 2
sample[225] = 1
while i < len(sample):
    instruction = str(sample[i])
    opcode = int(instruction[-2:])
    modes = instruction[:-2][::-1]
    if opcode == 99:
        break

    if opcode == 1 or opcode == 2:
        length = 4
        try:
            if modes[0] == "1":
                par1 = sample[i+1]
            else:
                par1 = sample[sample[i+1]]
        except Exception:
            par1 = sample[sample[i+1]]

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
    elif opcode == 4:
        length = 2
        try:
            if modes[0] == "1":
                par = sample[i+1]
            else:
                par = sample[sample[i+1]]
        except Exception:
            par = sample[sample[i+1]]

        print(par)

    i += length
