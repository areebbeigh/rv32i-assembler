from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from io import StringIO
import argparse
def get_parser():
    lexer = Lexer()
    return Parser(lexer=lexer)
ARGS_PARSER = argparse.ArgumentParser()
ARGS_PARSER.add_argument("input", help = "source file")
ARGS_PARSER.add_argument("-o","--output",default="a.txt",help="output file name")
ARGS = ARGS_PARSER.parse_args()
Parser = get_parser()
Parser.assemble(open(ARGS.input,'r'),open(ARGS.output,'w+'))