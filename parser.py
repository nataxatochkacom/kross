# parser.py

from instructions import INSTRUCTIONS
from ir import InstructionIR


class AssemblyParser:
    def parse_line(self, line: str) -> InstructionIR | None:
        # Удаляем комментарии и пробелы
        line = line.split(";")[0].strip()
        if not line:
            return None

        parts = line.replace(",", "").split()
        mnemonic = parts[0]

        if mnemonic not in INSTRUCTIONS:
            raise ValueError(f"Неизвестная команда: {mnemonic}")

        spec = INSTRUCTIONS[mnemonic]
        args = list(map(int, parts[1:]))

        if len(args) != len(spec["fields"]):
            raise ValueError(
                f"{mnemonic}: ожидается {len(spec['fields'])} аргументов"
            )

        kwargs = {"name": mnemonic, "A": spec["A"]}
        for field, value in zip(spec["fields"], args):
            kwargs[field] = value

        return InstructionIR(**kwargs)

    def parse(self, text: str):
        instructions = []
        for line_num, line in enumerate(text.splitlines(), start=1):
            try:
                instr = self.parse_line(line)
                if instr:
                    instructions.append(instr)
            except Exception as e:
                raise SyntaxError(f"Строка {line_num}: {e}")

        return instructions
