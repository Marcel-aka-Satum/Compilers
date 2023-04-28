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
    ast.convertToWhile()
    countScopes = {"unNamedScope": 0, "ifStatement": 0, "elifStatement": 0, "elseStatement": 0, "whileStatement": 0, "forLoop": 0}
    ast.optimize(countScopes)
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
            exit()

    if symbolTable.error:
        exit()
    # Constant propagation and constant folding
    #ast.constantPropagation(dict(), [], symbolTable.symbol_table, None)
    ast.constantFolding(symbolTable.symbol_table, None)
    # Initialise the symbol table after the constant folding
    ast.initialiseSymbolTable(symbolTable.symbol_table, None)
    # Print the AST in dot
    ast.printInDot(argv)
    # print symbol table
    print(symbolTable.symbol_table.symbol_tables)
    print(symbolTable.symbol_table.funcDict)
if __name__ == '__main__':
    main("test.c")