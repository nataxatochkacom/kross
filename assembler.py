# assembler.py

import argparse
from parser import AssemblyParser


def main():
    cli = argparse.ArgumentParser(description="Ассемблер УВМ (Этап 1)")
    cli.add_argument("source", help="Файл с исходным кодом")
    cli.add_argument("output", help="Выходной бинарный файл")
    cli.add_argument("--test", action="store_true", help="Режим тестирования")

    args = cli.parse_args()

    with open(args.source, "r", encoding="utf-8") as f:
        source_code = f.read()

    parser = AssemblyParser()
    ir_program = parser.parse(source_code)

    if args.test:
        print("=== ВНУТРЕННЕЕ ПРЕДСТАВЛЕНИЕ ===\n")
        for i, instr in enumerate(ir_program, start=1):
            print(f"Команда {i}:")
            for field, value in instr.to_dict().items():
                print(f"  {field} = {value}")
            print()
    else:
        # На этапе 1 бинарник не формируем
        with open(args.output, "wb") as f:
            pass


if __name__ == "__main__":
    main()
