class OpcodeVM:
    def __init__(self, memory):
        self.memory = memory
        self.pointer = 0
        self.finished = False
        self.inputValues = []
        self.outputValues = []
        self.base = 0

    def print_state(self):
        print("Memory: " + str(self.memory))
        print("Pointer: " + str(self.pointer))
        print("Opcode: " + str(self.memory[self.pointer])[-2:])
        print("Rel. base:" + str(self.base))

        print("\n")

    def set_input(self, value):
        self.inputValues.append(value)

    def exec_next(self):
        instruction = str(self.memory[self.pointer])
        opcode = int(instruction[-2:])
        modes = instruction[:-2][::-1]
        i = self.pointer
        length = 4

        if opcode == 99:
            self.finished = True
            return 0

        try:
            if modes[0] == "1":
                par1 = i+1
            elif modes[0] == "2":
                par1 = self.memory[i+1] + self.base
            else:
                par1 = self.memory[i+1]
        except IndexError:
            par1 = self.memory[i+1]

        try:
            if modes[1] == "1":
                par2 = i+2
            elif modes[1] == "2":
                par2 = self.memory[i+2] + self.base
            else:
                par2 = self.memory[i+2]
        except IndexError:
            par2 = self.memory[i+2]

        try:
            if modes[2] == "2":
                dest = self.memory[i+3] + self.base
            else:
                dest = self.memory[i+3]
        except IndexError:
            dest = self.memory[i+3]

        if opcode == 1:
            self.memory[dest] = self.memory[par1] + self.memory[par2]

        elif opcode == 2:
            self.memory[dest] = self.memory[par1] * self.memory[par2]

        elif opcode == 3:
            length = 2
            try:
                self.memory[par1] = self.inputValues.pop(0)
            except IndexError:
                length = 0

        elif opcode == 4:
            length = 2
            self.outputValues.append(self.memory[par1])
            if len(self.outputValues) == 3:
                color = self.outputValues.pop()
                turn = self.outputValues.pop()
                val3 = self.outputValues.pop()  # only for day 13
                yield [color, turn, val3]

        elif opcode == 5:
            if self.memory[par1] != 0:
                length = 0
                self.pointer = self.memory[par2]
            else:
                length = 3

        elif opcode == 6:
            if self.memory[par1] == 0:
                length = 0
                self.pointer = self.memory[par2]
            else:
                length = 3

        elif opcode == 7:
            if self.memory[par1] < self.memory[par2]:
                self.memory[dest] = 1
            else:
                self.memory[dest] = 0

        elif opcode == 8:
            if self.memory[par1] == self.memory[par2]:
                self.memory[dest] = 1
            else:
                self.memory[dest] = 0

        elif opcode == 9:
            length = 2
            self.base = self.base + self.memory[par1]

        else:
            print("Unknown opcode: " + str(opcode))
            raise RuntimeError

        self.pointer = self.pointer + length
