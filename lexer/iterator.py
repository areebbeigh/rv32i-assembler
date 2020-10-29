class LexerIterator:
    def __init__(self, lexer):
        self.lexer = lexer

    def __next__(self):
        t = self.lexer.lexer.token()
        if t is None:
            raise StopIteration
        return t
