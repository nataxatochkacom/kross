# encoder.py

def encode_instruction(instr) -> bytes:
    """
    Кодирует одну команду УВМ в 10 байт (little-endian)
    """
    word = 0

    # Поле A (opcode): биты 0–5
    word |= (instr.A & 0b111111) << 0

    # Поле B: биты 6–28
    if instr.B is not None:
        word |= (instr.B & ((1 << 23) - 1)) << 6

    # Поле C
    if instr.name == "LOAD_CONST":
        # биты 29–54 (26 бит)
        word |= (instr.C & ((1 << 26) - 1)) << 29
    elif instr.C is not None:
        # биты 29–51 (23 бита)
        word |= (instr.C & ((1 << 23) - 1)) << 29

    # Поле D
    if instr.name == "READ_MEM":
        # биты 52–59 (8 бит)
        word |= (instr.D & 0xFF) << 52
    elif instr.name == "SHR":
        # биты 52–74 (23 бита)
        word |= (instr.D & ((1 << 23) - 1)) << 52

    return word.to_bytes(10, byteorder="little")
