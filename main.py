from MyGrammarLexer import MyGrammarLexer
from AST import *
from SemanticAnalysisVisitor import *
from LLVM import *
from ErrorListener import *
from mips import *


def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    # remove the default error listener and add the custom one
    parser.removeErrorListeners()
    parser.addErrorListener(errorAnalysis())
    # Create syntax tree
    syntaxTree = parser.prog()
    # Check if we have a syntax error, if so we stop.
    if parser.getNumberOfSyntaxErrors() >= 1:
        exit()
    # Create AST
    ast = AST(syntaxTree)
    # Optimize the AST
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
    ast.constantPropagation(dict(), [], symbolTable.symbol_table, None)
    ast.constantFolding(symbolTable.symbol_table, None)
    ast.removeDeadCode()
    # Initialise the symbol table after the constant folding
    ast.initialiseSymbolTable(symbolTable.symbol_table, None)
    # Print the AST in dot
    ast.printInDot(argv)
    # print symbol table
    print(symbolTable.symbol_table.symbol_tables)
    # Generate mips and print it
    mips = Mips(ast, symbolTable, argv)

import struct
if __name__ == '__main__':

    main("test.c")