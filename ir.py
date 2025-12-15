# ir.py

from dataclasses import dataclass, asdict


@dataclass
class InstructionIR:
    name: str
    A: int
    B: int | None = None
    C: int | None = None
    D: int | None = None

    def to_dict(self):
        """Для тестового режима"""
        return {k: v for k, v in asdict(self).items() if v is not None}
