# rv32i-assembler

_*Work in progress*_

An assembler for a small subset of rv32i instructions in Python. Uses [Python Lex-Yacc](https://ply.readthedocs.io/en/latest/ply.html#) for grammar definition and parsing.

Originally implemented as an assignment in the Computer Organization and Architecture course at NIT Srinagar.

- Number of instructions implemented: 38. (work in progress)

```bash
pip install -r requirements.txt
python3 assembler.py <input> -o <output>
```

## Pending

- ~~CLI~~ -> partially done.
- Error reporting
- ~~Load/Store instructions~~ -> implemented.
- JALR
- ~~SLT/SLTU/SLTI/SLTIU~~ -> implemented.
- Comments

## Resources

- [COA Course, NIT Srinagar](https://www.youtube.com/playlist?list=PLUbapHgKkROlrwsMXiROFL6T2ftXxe_5C)
- [RISC-V cheatsheet](https://metalcode.eu/2019-12-06-rv32i.html)
- [RISC-V reference](https://github.com/jameslzhu/riscv-card/blob/master/riscv-card.pdf)
- [PLY Docs](https://ply.readthedocs.io/en/latest/ply.html#)
