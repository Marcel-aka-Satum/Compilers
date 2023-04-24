from MyGrammarLexer import MyGrammarLexer
from AST import *
from SemanticAnalysisVisitor import *
from LLVM import *


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
    # Create the symbol table
    symbolTable = SemanticAnalysisVisitor()
    # Visit the AST and look for errors
    try:
        symbolTable.visit(ast)
    except:
        if symbolTable.error:
            exit()
        else:
            print("ERROR")
    if symbolTable.error:
        exit()
    ast.convertToWhile()
    # Constant propagation and constant folding
    ast.constantPropagation(dict(), [], symbolTable.symbol_table, None)
    ast.constantFolding(symbolTable.symbol_table, None)
    # Initialise the symbol table after the constant folding
    ast.initialiseSymbolTable(symbolTable.symbol_table, None)
    # Print the AST in dot
    ast.printInDot(argv)
    # print symbol table
    print(symbolTable.symbol_table.symbol_tables)

if __name__ == '__main__':
    main("test.c")