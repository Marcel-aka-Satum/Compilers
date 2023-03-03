import sys
from antlr4 import *
from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser
import AST
 
def main(argv):
    input_stream = FileStream("test.txt")
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.prog()
    ast = AST(tree)
 
if __name__ == '__main__':
    main(sys.argv)
