# Ассемблер УВМ — Этап 1

## Поддерживаемые команды

LOAD_CONST B, C
READ_MEM   B, C, D
WRITE_MEM  B, C
SHR        B, C, D

## Запуск

```bash
python assembler.py tests.asm out.bin --test
