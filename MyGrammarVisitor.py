# Generated from MyGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#prog.
    def visitProg(self, ctx:MyGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expr.
    def visitExpr(self, ctx:MyGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opAnd.
    def visitOpAnd(self, ctx:MyGrammarParser.OpAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opOr.
    def visitOpOr(self, ctx:MyGrammarParser.OpOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opCompare.
    def visitOpCompare(self, ctx:MyGrammarParser.OpCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opAddOrSub.
    def visitOpAddOrSub(self, ctx:MyGrammarParser.OpAddOrSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opMultOrDiv.
    def visitOpMultOrDiv(self, ctx:MyGrammarParser.OpMultOrDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#opUnary.
    def visitOpUnary(self, ctx:MyGrammarParser.OpUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#brackets.
    def visitBrackets(self, ctx:MyGrammarParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#int.
    def visitInt(self, ctx:MyGrammarParser.IntContext):
        return self.visitChildren(ctx)



del MyGrammarParser