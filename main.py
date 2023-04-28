from MyGrammarLexer import MyGrammarLexer
from AST import *
from ASTVisitor import *
from SemanticAnalysisVisitor import *

def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    ##check for syntax errors
    try:
        syntaxTree = parser.prog()
    except ValueError as e:
        print(str(e))

    ##CREATE AST
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
    if symbolTable.error:
        exit()
    # Constant propagation and constant folding
    # ast.constantPropagation(dict(), [], symbolTable.symbol_table, None)
    ast.constantFolding(symbolTable.symbol_table, None)
    # Initialise the symbol table after the constant folding
    ast.initialiseSymbolTable(symbolTable.symbol_table, None)
    # Print the AST in dot
    ast.printInDot(argv)
    ast.generate_LLVM(ast)
    ast.print_ll(argv)

    # print symbol table
    print(symbolTable.symbol_table.symbol_tables)
if __name__ == '__main__':
    main("/home/hatepainsad/Desktop/compilers/Compilers/test.txt")