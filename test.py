from lexer.lexer import Lexer

l = Lexer()
code = '''
addi x5,x0, 6
addi x1,x0,1
addi x2,x0,0
addi x3,x0,0
addi x4,x0,1
FOR:
    add x3, x1, x2
    add x2, x0, x1
    add x1, x0, x3
    addi x4, x4, 1
    blt x4, x5, FOR
HALT:
    jal x31, HALT
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
ostream = StringIO()

p.assemble(istream, ostream)
# print(p.symbol_table)
ostream.seek(0)
print(ostream.read())
