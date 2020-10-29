from ply import lex

from lexer import instructions
from lexer.iterator import LexerIterator


class Lexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Tokens
    tokens = ('INSTR', 'LABEL', 'REGISTER', 'COMMA',
              'IMMEDIATE', 'NEWLINE', 'COLON',)

    # Rules
    t_COMMA = r','
    t_COLON = r':'
    t_IMMEDIATE = r'[-+]?\d+'
    # Ignore white spaces
    t_ignore = ' \t\r'

    # Register should appear before INSTR and LABEL since
    # x1...32 are valid labels too.
    def t_REGISTER(self, t):
        r'x\d\d?'
        return t

    def t_INSTR(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        if instructions.is_instr(t.value):
            t.type = 'INSTR'
            return t
        return self.t_LABEL(t)

    def t_LABEL(self, t):
        r'[a-zA-Z\.][a-zA-Z0-9]*'
        if instructions.is_instr(t.value):
            return self.t_INSTR(t)
        t.type = 'LABEL'
        return t

    # https://ply.readthedocs.io/en/latest/ply.html#line-numbers-and-positional-information
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    # https://ply.readthedocs.io/en/latest/ply.html#error-handling
    def t_error(self, t):
        raise Exception(
            f'Illegal character: {t.value} in line {t.lexer.lineno}')

    def input_string(self, str):
        self.lexer.input(str)

    def input(self, stream):
        self.input_string(stream.read())

    def __iter__(self):
        return LexerIterator(self)
