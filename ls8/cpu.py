"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into ram."""

        file = sys.argv[1]
        address = 0


        with open(file) as f:
            for line in f:

                line = line.split("#")[0].strip()

                if line == "":
                    continue

                else:
                    self.ram[address] = int(line, 2)
                    address += 1

                print(line)



    def alu(self, op, reg_a, reg_b):
        """ALU / Math operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]

        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010

        running = True

        while running:
            ir = self.ram[self.pc]

            reg_a = self.ram[self.pc + 1]
            reg_b = self.ram[self.pc + 2]

            if ir == HLT:
                self.running = False
                self.pc += 1

            elif ir == LDI:
                self.reg[reg_a] = reg_b
                self.pc += 3

            elif ir == PRN:
                print(self.reg[reg_a])
                self.pc += 2

            elif ir == MUL:
                self.reg[reg_a] *= self.reg[reg_b]
                self.pc += 3


    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
