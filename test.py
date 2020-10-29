from lexer.lexer import Lexer

l = Lexer()
code = '''
addi x1, x4, 5
beq x5, x1, -8
addi x2, x3, 4
slli x1, x2, 2
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
