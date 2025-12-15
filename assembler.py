# assembler.py

import argparse
from parser import AssemblyParser
from encoder import encode_instruction


def main():
    cli = argparse.ArgumentParser(description="Ассемблер УВМ")
    cli.add_argument("source", help="Файл с исходным кодом")
    cli.add_argument("output", help="Выходной бинарный файл")
    cli.add_argument("--test", action="store_true", help="Режим тестирования")

    args = cli.parse_args()

    with open(args.source, "r", encoding="utf-8") as f:
        source_code = f.read()

    parser = AssemblyParser()
    ir_program = parser.parse(source_code)

    binary = bytearray()

    for instr in ir_program:
        binary += encode_instruction(instr)

    if args.test:
        print("=== РЕЗУЛЬТАТ АССЕМБЛИРОВАНИЯ ===\n")
        for i in range(0, len(binary), 10):
            chunk = binary[i:i + 10]
            print(", ".join(f"0x{b:02X}" for b in chunk))
        print()

    with open(args.output, "wb") as f:
        f.write(binary)

    print(f"Размер двоичного файла: {len(binary)} байт")


if __name__ == "__main__":
    main()
