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


    # Enter a parse tree produced by MyGrammarParser#string.
    def enterString(self, ctx:MyGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#string.
    def exitString(self, ctx:MyGrammarParser.StringContext):
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


    # Enter a parse tree produced by MyGrammarParser#conditionStatement.
    def enterConditionStatement(self, ctx:MyGrammarParser.ConditionStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#conditionStatement.
    def exitConditionStatement(self, ctx:MyGrammarParser.ConditionStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printFunction.
    def enterPrintFunction(self, ctx:MyGrammarParser.PrintFunctionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printFunction.
    def exitPrintFunction(self, ctx:MyGrammarParser.PrintFunctionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#scanFunction.
    def enterScanFunction(self, ctx:MyGrammarParser.ScanFunctionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#scanFunction.
    def exitScanFunction(self, ctx:MyGrammarParser.ScanFunctionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#scanArg.
    def enterScanArg(self, ctx:MyGrammarParser.ScanArgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#scanArg.
    def exitScanArg(self, ctx:MyGrammarParser.ScanArgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#printArg.
    def enterPrintArg(self, ctx:MyGrammarParser.PrintArgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#printArg.
    def exitPrintArg(self, ctx:MyGrammarParser.PrintArgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:MyGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:MyGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#elifStatement.
    def enterElifStatement(self, ctx:MyGrammarParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#elifStatement.
    def exitElifStatement(self, ctx:MyGrammarParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#elseStatement.
    def enterElseStatement(self, ctx:MyGrammarParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#elseStatement.
    def exitElseStatement(self, ctx:MyGrammarParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:MyGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:MyGrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#forLoop.
    def enterForLoop(self, ctx:MyGrammarParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#forLoop.
    def exitForLoop(self, ctx:MyGrammarParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#unNamedScope.
    def enterUnNamedScope(self, ctx:MyGrammarParser.UnNamedScopeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#unNamedScope.
    def exitUnNamedScope(self, ctx:MyGrammarParser.UnNamedScopeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#comment.
    def enterComment(self, ctx:MyGrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#comment.
    def exitComment(self, ctx:MyGrammarParser.CommentContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#argument.
    def enterArgument(self, ctx:MyGrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#argument.
    def exitArgument(self, ctx:MyGrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#funcDefinition.
    def enterFuncDefinition(self, ctx:MyGrammarParser.FuncDefinitionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#funcDefinition.
    def exitFuncDefinition(self, ctx:MyGrammarParser.FuncDefinitionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#funcDeclaration.
    def enterFuncDeclaration(self, ctx:MyGrammarParser.FuncDeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#funcDeclaration.
    def exitFuncDeclaration(self, ctx:MyGrammarParser.FuncDeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#argumentCall.
    def enterArgumentCall(self, ctx:MyGrammarParser.ArgumentCallContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#argumentCall.
    def exitArgumentCall(self, ctx:MyGrammarParser.ArgumentCallContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#functionCall.
    def enterFunctionCall(self, ctx:MyGrammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#functionCall.
    def exitFunctionCall(self, ctx:MyGrammarParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#arrDecl.
    def enterArrDecl(self, ctx:MyGrammarParser.ArrDeclContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrDecl.
    def exitArrDecl(self, ctx:MyGrammarParser.ArrDeclContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#arrDef.
    def enterArrDef(self, ctx:MyGrammarParser.ArrDefContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrDef.
    def exitArrDef(self, ctx:MyGrammarParser.ArrDefContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#arrCall.
    def enterArrCall(self, ctx:MyGrammarParser.ArrCallContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrCall.
    def exitArrCall(self, ctx:MyGrammarParser.ArrCallContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#arrArg.
    def enterArrArg(self, ctx:MyGrammarParser.ArrArgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrArg.
    def exitArrArg(self, ctx:MyGrammarParser.ArrArgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#arrAssign.
    def enterArrAssign(self, ctx:MyGrammarParser.ArrAssignContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#arrAssign.
    def exitArrAssign(self, ctx:MyGrammarParser.ArrAssignContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#lib.
    def enterLib(self, ctx:MyGrammarParser.LibContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#lib.
    def exitLib(self, ctx:MyGrammarParser.LibContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#body.
    def enterBody(self, ctx:MyGrammarParser.BodyContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#body.
    def exitBody(self, ctx:MyGrammarParser.BodyContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#returnStatement.
    def enterReturnStatement(self, ctx:MyGrammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#returnStatement.
    def exitReturnStatement(self, ctx:MyGrammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#increment.
    def enterIncrement(self, ctx:MyGrammarParser.IncrementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#increment.
    def exitIncrement(self, ctx:MyGrammarParser.IncrementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#decrement.
    def enterDecrement(self, ctx:MyGrammarParser.DecrementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#decrement.
    def exitDecrement(self, ctx:MyGrammarParser.DecrementContext):
        pass



del MyGrammarParser