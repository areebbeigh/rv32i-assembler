from ply import yacc

from helpers import imm_converter
from lexer import instructions


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self)

    # Rules
    # https://ply.readthedocs.io/en/latest/ply.html#ast-construction

    def p_program_stmt(self, p):
        'program : stmt'
        p[0] = {
            'type': 'non_label',
            'tokens': p[1],
        }

    def p_program_label(self, p):
        'program : LABEL COLON NEWLINE'
        p[0] = {
            'type': 'label',
            'tokens': {
                'label': p[1],
                'lineno': p.lineno(1),
            }
        }

    def p_stmt_type_r(self, p):
        'stmt : INSTR register COMMA register COMMA register NEWLINE'
        assert instructions.is_instr(p[1])
        p[0] = {
            'type': 'r',
            'instr': p[1],
            'rd': p[2],
            'rs1': p[4],
            'rs2': p[6],
            'lineno': p.lineno(1),
        }

    def p_stmt_type_i_sb(self, p):
        'stmt : INSTR register COMMA register COMMA IMMEDIATE NEWLINE'
        instr = p[1]
        assert instructions.is_instr(instr)
        assert instr in instructions.TYPE_I or instr in instructions.TYPE_SB

        res = {
            'instr': instr,
            'lineno': p.lineno(1),
            'rd': p[2],
            'rs1': p[4],
        }

        if instr in instructions.TYPE_I:
            res.update({
                'type': 'i',
                'imm': imm_converter.imm_12(int(p[6])),
            })
        else:  # Type SB
            res.update({
                'type': 'sb',
                'imm': imm_converter.imm_13_effective(int(p[6])),
            })
        p[0] = res

    def p_stmt_type_ui_uj(self, p):
        'stmt : INSTR register COMMA IMMEDIATE NEWLINE'
        instr = p[1]
        assert instructions.is_instr(instr)
        assert instr in instructions.TYPE_UI or instr in instructions.TYPE_UJ

        res = {
            'instr': instr,
            'lineno': p.lineno(1),
            'rd': p[2],
        }

        if instr in instructions.TYPE_UI:
            res.update({
                'imm': imm_converter.imm_20(p[4])
            })
        else:  # Type UJ
            res.update({
                'imm': imm_converter.imm_21_effective(p[4])
            })
        p[0] = res

    # def p_stmt_type_uj_label(self, p):
    #     'stmt : INSTR register COMMA LABEL NEWLINE'
    #     pass

    # def p_stmt_type_sb_label(self, p):
    #     'stmt : INSTR register COMMA register COMMA LABEL NEWLINE'
    #     pass

    def p_register(self, p):
        'register : REGISTER'
        r = int(p[1][1:])
        assert r >= 0 and r <= 31, f'Invalid register {p[1]}'
        p[0] = p[1]

    def p_stmt_none(self, p):
        'stmt : NEWLINE'
        p[0] = None

    def p_error(self, p):
        lineno = ''
        if p:
            lineno = p.lineno
        raise Exception(f'Syntax error: {lineno} {p}')

    def parse_line(self, line):
        return self.parser.parse(line, debug=True, lexer=self.lexer.lexer)
