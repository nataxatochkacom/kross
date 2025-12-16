# gui_runner.py

from parser import AssemblyParser
from encoder import encode_instruction
from interpreter import UVMInterpreter


def run_program(source_text: str):
    parser = AssemblyParser()
    ir_program = parser.parse(source_text)

    binary = bytearray()
    for instr in ir_program:
        binary += encode_instruction(instr)

    vm = UVMInterpreter()
    vm.load_program(binary)
    vm.run()

    return vm.memory
