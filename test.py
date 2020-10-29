from lexer.lexer import Lexer

l = Lexer()
code = '''
.main:
    addi x1, x0, 5
    addi x2, x0, 4
    beq x1,x2, -8
.ret:
    addi x0, x1, 0
'''
# code = '''addi x1, x2, 1\n'''
# l.input_string(code)

# for t in l:
#     print(t)

# from helpers import imm_converter

# print(imm_converter.imm_12(5))
# print(imm_converter.imm_12(-5))

# print(imm_converter.imm_13_effective(6))
# print(imm_converter.imm_13_effective(-6))

# print(imm_converter.imm_20(5))
# print(imm_converter.imm_20(-5))

from parser.parser import Parser

p = Parser(l)
# for ln in code.split('\n'):
#     if ln:
#         print(p.parse_line(ln + '\n'))

from io import StringIO

istream = StringIO(code)
p.build_symbol_table(istream)
print(p.symbol_table)
