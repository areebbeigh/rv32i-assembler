from lexer.lexer import Lexer

l = Lexer()
code = '''
addi x1, x2, 1
addi x2, x3, 2
add x2, x5, 1
'''
l.input_string(code)

for t in l:
    print(t)

from parser import imm_converter

print(imm_converter.imm_type_i(5))
print(imm_converter.imm_type_i(-5))

print(imm_converter.imm_type_ui(5))
print(imm_converter.imm_type_ui(-5))
