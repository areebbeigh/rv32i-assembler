from ply import yacc

from helpers import imm_converter
from lexer import instructions
from generator import CodeGenerator


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self)
        self.generator = CodeGenerator()

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
        assert instr in instructions.TYPE_I or instr in instructions.TYPE_SB

        res = {
            'instr': instr,
            'lineno': p.lineno(1),
        }

        if instr in instructions.TYPE_I:
            res.update({
                'type': 'i',
                'rd': p[2],
                'rs1': p[4],
                'imm': imm_converter.imm_12(int(p[6])),
            })
        else:  # Type SB
            res.update({
                'type': 'sb',
                'rs1': p[2],
                'rs2': p[4],
                'imm': imm_converter.imm_13_effective(int(p[6])),
            })
        p[0] = res

    def p_stmt_type_ui_uj(self, p):
        'stmt : INSTR register COMMA IMMEDIATE NEWLINE'
        instr = p[1]
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

    def p_stmt_type_uj_label(self, p):
        'stmt : INSTR register COMMA LABEL NEWLINE'
        instr = p[0]
        assert instr in instructions.TYPE_UJ
        p[0] = {
            'type': 'uj',
            'instr': instr,
            'lineno': p.lineno(1),
            'label': p[4],
            'rd': p[2],
        }

    def p_stmt_type_sb_label(self, p):
        'stmt : INSTR register COMMA register COMMA LABEL NEWLINE'
        instr = p[0]
        assert instr in instructions.TYPE_SB
        p[0] = {
            'type': 'sb',
            'instr': instr,
            'lineno': p.lineno(1),
            'label': p[6],
            'rs1': p[2],
            'rs2': p[4],
        }

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
        return self.parser.parse(line, debug=False, lexer=self.lexer.lexer)

    def _readlines(self, stream):
        for ln in stream.readlines():
            # Ensure line ends in \n for our parser to work
            yield f'{ln.strip()}\n'

    # First pass

    def build_symbol_table(self, stream):
        # Symbol table
        self.symbol_table = {}
        address = 0

        for ln in self._readlines(stream):
            node = self.parse_line(ln)

            if node['tokens'] is None:
                # Newline
                continue
            if node['type'] != 'label':
                # 4 bytes per instruction
                address += 4
                continue

            label = node['tokens']['label']
            assert label not in self.symbol_table, f'Label {label} already exists'
            self.symbol_table[label] = address

    # Second pass

    def generate_output(self, istream, ostream):
        address = 0
        for ln in self._readlines(istream):
            node = self.parse_line(ln)

            if node['type'] == 'label':
                continue
            if node['tokens'] is None:
                continue

            # Jump instruction
            if 'label' in node['tokens']:
                label = node['tokens']['label']
                assert label in self.symbol_table, f'Undefined label {label}'
                # We need to get the offset from current address to this label's address
                raise NotImplementedError()
            else:
                self.generator.write_binstr(node['tokens'], ostream)
                ostream.write('\n')
            address += 4

    def assemble(self, istream, ostream):
        self.build_symbol_table(istream)
        istream.seek(0)
        self.generate_output(istream, ostream)
