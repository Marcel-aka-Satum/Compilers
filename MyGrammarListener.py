# Generated from MyGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#prog.
    def enterProg(self, ctx:MyGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#prog.
    def exitProg(self, ctx:MyGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opAnd.
    def enterOpAnd(self, ctx:MyGrammarParser.OpAndContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opAnd.
    def exitOpAnd(self, ctx:MyGrammarParser.OpAndContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opOr.
    def enterOpOr(self, ctx:MyGrammarParser.OpOrContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opOr.
    def exitOpOr(self, ctx:MyGrammarParser.OpOrContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opCompare.
    def enterOpCompare(self, ctx:MyGrammarParser.OpCompareContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opCompare.
    def exitOpCompare(self, ctx:MyGrammarParser.OpCompareContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opAddOrSub.
    def enterOpAddOrSub(self, ctx:MyGrammarParser.OpAddOrSubContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opAddOrSub.
    def exitOpAddOrSub(self, ctx:MyGrammarParser.OpAddOrSubContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opMultOrDiv.
    def enterOpMultOrDiv(self, ctx:MyGrammarParser.OpMultOrDivContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opMultOrDiv.
    def exitOpMultOrDiv(self, ctx:MyGrammarParser.OpMultOrDivContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#opUnary.
    def enterOpUnary(self, ctx:MyGrammarParser.OpUnaryContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#opUnary.
    def exitOpUnary(self, ctx:MyGrammarParser.OpUnaryContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#brackets.
    def enterBrackets(self, ctx:MyGrammarParser.BracketsContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#brackets.
    def exitBrackets(self, ctx:MyGrammarParser.BracketsContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variableDefinition.
    def enterVariableDefinition(self, ctx:MyGrammarParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variableDefinition.
    def exitVariableDefinition(self, ctx:MyGrammarParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MyGrammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MyGrammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:MyGrammarParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:MyGrammarParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#constWord.
    def enterConstWord(self, ctx:MyGrammarParser.ConstWordContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#constWord.
    def exitConstWord(self, ctx:MyGrammarParser.ConstWordContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#pointerWord.
    def enterPointerWord(self, ctx:MyGrammarParser.PointerWordContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#pointerWord.
    def exitPointerWord(self, ctx:MyGrammarParser.PointerWordContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#reservedWord.
    def enterReservedWord(self, ctx:MyGrammarParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#reservedWord.
    def exitReservedWord(self, ctx:MyGrammarParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#dataTypes.
    def enterDataTypes(self, ctx:MyGrammarParser.DataTypesContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#dataTypes.
    def exitDataTypes(self, ctx:MyGrammarParser.DataTypesContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#int.
    def enterInt(self, ctx:MyGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#int.
    def exitInt(self, ctx:MyGrammarParser.IntContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#float.
    def enterFloat(self, ctx:MyGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#float.
    def exitFloat(self, ctx:MyGrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#char.
    def enterChar(self, ctx:MyGrammarParser.CharContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#char.
    def exitChar(self, ctx:MyGrammarParser.CharContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#referenceID.
    def enterReferenceID(self, ctx:MyGrammarParser.ReferenceIDContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#referenceID.
    def exitReferenceID(self, ctx:MyGrammarParser.ReferenceIDContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#nameIdentifier.
    def enterNameIdentifier(self, ctx:MyGrammarParser.NameIdentifierContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#nameIdentifier.
    def exitNameIdentifier(self, ctx:MyGrammarParser.NameIdentifierContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printFunction.
    def enterPrintFunction(self, ctx:MyGrammarParser.PrintFunctionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printFunction.
    def exitPrintFunction(self, ctx:MyGrammarParser.PrintFunctionContext):
        pass



del MyGrammarParser