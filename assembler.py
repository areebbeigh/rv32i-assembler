from src.lexer.lexer import Lexer
from src.parser.parser import Parser

# argparse definitions

def get_parser():
    lexer = Lexer()
    return Parser(lexer=lexer)

# get_parser() -> parser
# parser.assemble(input_stream, output_stream)
