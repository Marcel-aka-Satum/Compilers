from MyGrammarLexer import MyGrammarLexer
from AST import *


def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    syntaxTree = parser.prog()
    ast = AST(syntaxTree)
    ast.optimize()
    ast.constantPropagation(dict(), dict())
    ast.constantFolding()
    ast.printInDot()

if __name__ == '__main__':
    main("test.txt")
