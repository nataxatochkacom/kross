# interpreter.py

import argparse
import csv
from decoder import decode_instruction

MEMORY_SIZE = 4096
INSTRUCTION_SIZE = 10


class UVMInterpreter:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE      # память данных
        self.program = []                    # память команд (bytes)
        self.pc = 0

    def load_program(self, binary: bytes):
        for i in range(0, len(binary), INSTRUCTION_SIZE):
            self.program.append(binary[i:i + INSTRUCTION_SIZE])

    def step(self):
        instr_bytes = self.program[self.pc]
        instr = decode_instruction(instr_bytes)

        if instr.name == "LOAD_CONST":
            self.memory[instr.B] = instr.C

        elif instr.name == "READ_MEM":
            base = self.memory[instr.B]
            self.memory[instr.C] = self.memory[base + instr.D]

        elif instr.name == "WRITE_MEM":
            target = self.memory[instr.C]
            self.memory[target] = self.memory[instr.B]

        else:
            raise RuntimeError(f"Команда {instr.name} не поддерживается")

        self.pc += 1

    def run(self):
        while self.pc < len(self.program):
            self.step()

    def dump_memory(self, start: int, end: int, path: str):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["address", "value"])
            for addr in range(start, end + 1):
                writer.writerow([addr, self.memory[addr]])


def main():
    cli = argparse.ArgumentParser(description="Интерпретатор УВМ")
    cli.add_argument("binary", help="Бинарный файл программы")
    cli.add_argument("dump", help="CSV-файл дампа памяти")
    cli.add_argument("range", help="Диапазон адресов, например 100:120")

    args = cli.parse_args()
    start, end = map(int, args.range.split(":"))

    with open(args.binary, "rb") as f:
        binary = f.read()

    vm = UVMInterpreter()
    vm.load_program(binary)
    vm.run()
    vm.dump_memory(start, end, args.dump)


if __name__ == "__main__":
    main()
