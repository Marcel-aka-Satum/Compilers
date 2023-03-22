from MyGrammarLexer import MyGrammarLexer
from AST import *
from ASTVisitor import *
from ErrorListener import *

def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    parser.removeErrorListeners()
    ##CREATE ERROR LISTENER AND ADD TO THE PARSER
    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)
    ##check for syntax errors
    try:
        syntaxTree = parser.prog()
    except ValueError as e:
        print(str(e))

    ##CREATE AST
    ast = AST(syntaxTree)
    ##OPTIMIZE AST
    ast.optimize()
    
    ##PROPAGATION + FOLDING
    ast.constantPropagation(dict())
    ast.constantFolding()
    ##PRINT DOT
    ast.printInDot()

    ##VISIT
    visitor = ASTVisitor()
    visitor.visit_AST(ast)

if __name__ == '__main__':
    main("/home/hatepainsad/Desktop/compilers/Compilers/test.txt")