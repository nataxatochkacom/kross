# decoder.py

from ir import InstructionIR


def decode_instruction(data: bytes) -> InstructionIR:
    """
    Декодирует 10 байт little-endian в InstructionIR
    """
    word = int.from_bytes(data, byteorder="little")

    A = (word >> 0) & 0b111111
    B = (word >> 6) & ((1 << 23) - 1)

    # Определяем тип по opcode
    if A == 23:  # LOAD_CONST
        C = (word >> 29) & ((1 << 26) - 1)
        return InstructionIR("LOAD_CONST", A, B=B, C=C)

    if A == 46:  # READ_MEM
        C = (word >> 29) & ((1 << 23) - 1)
        D = (word >> 52) & 0xFF
        return InstructionIR("READ_MEM", A, B=B, C=C, D=D)

    if A == 2:  # WRITE_MEM
        C = (word >> 29) & ((1 << 23) - 1)
        return InstructionIR("WRITE_MEM", A, B=B, C=C)

    if A == 56:  # SHR (не исполняем, но декодируем)
        C = (word >> 29) & ((1 << 23) - 1)
        D = (word >> 52) & ((1 << 23) - 1)
        return InstructionIR("SHR", A, B=B, C=C, D=D)

    raise ValueError(f"Неизвестный opcode: {A}")
