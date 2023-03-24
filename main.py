from MyGrammarLexer import MyGrammarLexer
from AST import *
from SemanticAnalysisVisitor import *

def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)

    # Create syntax tree
    syntaxTree = parser.prog()
    # Create AST
    ast = AST(syntaxTree)
    # Optimize the AST
    ast.optimize()
    # Constant propagation and constant folding
    ast.constantPropagation(dict(), dict())
    ast.constantFolding()
    # Print the AST in dot
    ast.printInDot()
    # Create the symbol table
    symbolTable = SemanticAnalysisVisitor()
    # Visit the AST and look for errors
    symbolTable.visit(ast)

    print(symbolTable.symbol_table.symbol_tables)

if __name__ == '__main__':
    main("test.txt")