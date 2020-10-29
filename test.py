from lexer.lexer import Lexer

l = Lexer()
code = '''
addi x1, x2, 1
addi x2, x3, 2
add x2, x5, x2
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
for ln in code.split('\n'):
    print(p.parse_line(ln + '\n'))
