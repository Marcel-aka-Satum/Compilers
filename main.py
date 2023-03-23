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

    ##OPTIMIZE AST
    ast.optimize()

    ##PROPAGATION + FOLDING
    ast.constantPropagation(dict(), dict())
    ast.constantFolding()
    ##PRINT DOT
    ast.printInDot()


    ##check for semantic errors
    print("LOOKING FOR SEMANTIC ERRORS ------")
    semanticAnalyser = SemanticAnalysisVisitor()
    semanticAnalyser.visit(ast)

    ##VISIT
    # print("VISITOR AFTER OPITMIZING-----------")
    # visitor = ASTVisitor()
    # visitor.visit_AST(ast)

if __name__ == '__main__':
    main("/home/hatepainsad/Desktop/compilers/Compilers/test.txt")