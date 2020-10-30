import argparse

from src.lexer.lexer import Lexer
from src.parser.parser import Parser


def get_parser():
    lexer = Lexer()
    return Parser(lexer=lexer)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", help="assembly source file")
arg_parser.add_argument(
    "-o", "--output", default="a.txt", help="output file name")
args = arg_parser.parse_args()

parser = get_parser()

with open(args.input, 'r') as istream, open(args.output, 'w') as ostream:
    parser.assemble(istream, ostream)
