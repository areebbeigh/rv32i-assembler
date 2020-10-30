from lexer.lexer import Lexer

l = Lexer()
code = '''
slt x1, x2, x3
START:
	addi x3,x0,2047
	addi x30,x0,20
	jal  x31,PUSH
	addi x3, x0, 1
	jal x31,POP
HALT:
	jal x31, HALT

PUSH:
	addi x30, x30, 4
	sw x30, x3, 0

POP:
	lw x4, x30, 0
	addi x30,x30,-4

SWAP:
	add x3,x0,x1
	add x1,x0,x2
	add x2,x0,x3
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
