# Generated from MyGrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,223,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,3,1,3,1,3,1,
        3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,4,1,4,1,4,3,4,81,8,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,100,8,4,10,4,12,4,103,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,114,8,5,10,5,12,5,117,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,131,8,6,10,6,12,6,134,9,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,143,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,154,
        8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,177,8,11,1,12,1,12,
        1,12,3,12,182,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,191,8,
        13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,199,8,15,1,16,1,16,1,17,1,
        17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,214,8,19,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,0,5,4,6,8,10,12,22,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,1,0,19,
        21,234,0,44,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,66,1,0,0,0,8,80,
        1,0,0,0,10,104,1,0,0,0,12,118,1,0,0,0,14,142,1,0,0,0,16,153,1,0,
        0,0,18,155,1,0,0,0,20,159,1,0,0,0,22,176,1,0,0,0,24,181,1,0,0,0,
        26,190,1,0,0,0,28,192,1,0,0,0,30,198,1,0,0,0,32,200,1,0,0,0,34,202,
        1,0,0,0,36,204,1,0,0,0,38,213,1,0,0,0,40,215,1,0,0,0,42,217,1,0,
        0,0,44,45,3,2,1,0,45,1,1,0,0,0,46,47,3,4,2,0,47,48,5,1,0,0,48,54,
        1,0,0,0,49,50,3,4,2,0,50,51,5,1,0,0,51,52,3,2,1,0,52,54,1,0,0,0,
        53,46,1,0,0,0,53,49,1,0,0,0,54,3,1,0,0,0,55,56,6,2,-1,0,56,57,3,
        6,3,0,57,63,1,0,0,0,58,59,10,2,0,0,59,60,5,2,0,0,60,62,3,6,3,0,61,
        58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,
        0,65,63,1,0,0,0,66,67,6,3,-1,0,67,68,3,8,4,0,68,74,1,0,0,0,69,70,
        10,2,0,0,70,71,5,3,0,0,71,73,3,8,4,0,72,69,1,0,0,0,73,76,1,0,0,0,
        74,72,1,0,0,0,74,75,1,0,0,0,75,7,1,0,0,0,76,74,1,0,0,0,77,78,6,4,
        -1,0,78,81,3,10,5,0,79,81,3,10,5,0,80,77,1,0,0,0,80,79,1,0,0,0,81,
        101,1,0,0,0,82,83,10,8,0,0,83,84,5,4,0,0,84,100,3,10,5,0,85,86,10,
        7,0,0,86,87,5,5,0,0,87,100,3,10,5,0,88,89,10,6,0,0,89,90,5,6,0,0,
        90,100,3,10,5,0,91,92,10,5,0,0,92,93,5,7,0,0,93,100,3,10,5,0,94,
        95,10,4,0,0,95,96,5,8,0,0,96,100,3,10,5,0,97,98,10,3,0,0,98,100,
        5,9,0,0,99,82,1,0,0,0,99,85,1,0,0,0,99,88,1,0,0,0,99,91,1,0,0,0,
        99,94,1,0,0,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,
        1,0,0,0,102,9,1,0,0,0,103,101,1,0,0,0,104,105,6,5,-1,0,105,106,3,
        12,6,0,106,115,1,0,0,0,107,108,10,3,0,0,108,109,5,10,0,0,109,114,
        3,12,6,0,110,111,10,2,0,0,111,112,5,11,0,0,112,114,3,12,6,0,113,
        107,1,0,0,0,113,110,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,11,1,0,0,0,117,115,1,0,0,0,118,119,6,6,-1,0,119,
        120,3,14,7,0,120,132,1,0,0,0,121,122,10,4,0,0,122,123,5,24,0,0,123,
        131,3,14,7,0,124,125,10,3,0,0,125,126,5,12,0,0,126,131,3,14,7,0,
        127,128,10,2,0,0,128,129,5,13,0,0,129,131,3,14,7,0,130,121,1,0,0,
        0,130,124,1,0,0,0,130,127,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,
        0,132,133,1,0,0,0,133,13,1,0,0,0,134,132,1,0,0,0,135,136,5,10,0,
        0,136,143,3,16,8,0,137,138,5,11,0,0,138,143,3,16,8,0,139,140,5,14,
        0,0,140,143,3,16,8,0,141,143,3,16,8,0,142,135,1,0,0,0,142,137,1,
        0,0,0,142,139,1,0,0,0,142,141,1,0,0,0,143,15,1,0,0,0,144,145,5,15,
        0,0,145,146,3,4,2,0,146,147,5,16,0,0,147,154,1,0,0,0,148,154,3,18,
        9,0,149,154,3,20,10,0,150,154,3,22,11,0,151,154,3,30,15,0,152,154,
        3,42,21,0,153,144,1,0,0,0,153,148,1,0,0,0,153,149,1,0,0,0,153,150,
        1,0,0,0,153,151,1,0,0,0,153,152,1,0,0,0,154,17,1,0,0,0,155,156,3,
        20,10,0,156,157,5,17,0,0,157,158,3,10,5,0,158,19,1,0,0,0,159,160,
        3,24,12,0,160,161,3,38,19,0,161,21,1,0,0,0,162,163,3,38,19,0,163,
        164,5,17,0,0,164,165,3,10,5,0,165,177,1,0,0,0,166,167,3,30,15,0,
        167,168,5,17,0,0,168,169,3,10,5,0,169,177,1,0,0,0,170,171,5,15,0,
        0,171,172,3,4,2,0,172,173,5,16,0,0,173,174,5,17,0,0,174,175,3,10,
        5,0,175,177,1,0,0,0,176,162,1,0,0,0,176,166,1,0,0,0,176,170,1,0,
        0,0,177,23,1,0,0,0,178,179,5,18,0,0,179,182,3,26,13,0,180,182,3,
        26,13,0,181,178,1,0,0,0,181,180,1,0,0,0,182,25,1,0,0,0,183,184,3,
        28,14,0,184,185,5,24,0,0,185,191,1,0,0,0,186,187,3,28,14,0,187,188,
        5,25,0,0,188,191,1,0,0,0,189,191,3,28,14,0,190,183,1,0,0,0,190,186,
        1,0,0,0,190,189,1,0,0,0,191,27,1,0,0,0,192,193,7,0,0,0,193,29,1,
        0,0,0,194,199,3,32,16,0,195,199,3,34,17,0,196,199,3,36,18,0,197,
        199,3,38,19,0,198,194,1,0,0,0,198,195,1,0,0,0,198,196,1,0,0,0,198,
        197,1,0,0,0,199,31,1,0,0,0,200,201,5,28,0,0,201,33,1,0,0,0,202,203,
        5,29,0,0,203,35,1,0,0,0,204,205,5,27,0,0,205,37,1,0,0,0,206,207,
        5,22,0,0,207,214,3,40,20,0,208,209,5,24,0,0,209,214,3,40,20,0,210,
        211,5,25,0,0,211,214,3,40,20,0,212,214,3,40,20,0,213,206,1,0,0,0,
        213,208,1,0,0,0,213,210,1,0,0,0,213,212,1,0,0,0,214,39,1,0,0,0,215,
        216,5,26,0,0,216,41,1,0,0,0,217,218,5,23,0,0,218,219,5,15,0,0,219,
        220,3,4,2,0,220,221,5,16,0,0,221,43,1,0,0,0,17,53,63,74,80,99,101,
        113,115,130,132,142,153,176,181,190,198,213
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'&&'", "'||'", "'=='", "'<='", 
                     "'>='", "'!='", "'<'", "'>'", "'+'", "'-'", "'/'", 
                     "'%'", "'!'", "'('", "')'", "'='", "'const'", "'int'", 
                     "'float'", "'char'", "'&'", "'printf'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "POINTER", "POINTERS", "ID", "CHAR", "INT", "FLOAT", 
                      "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_opAnd = 2
    RULE_opOr = 3
    RULE_opCompare = 4
    RULE_opAddOrSub = 5
    RULE_opMultOrDiv = 6
    RULE_opUnary = 7
    RULE_brackets = 8
    RULE_variableDefinition = 9
    RULE_variableDeclaration = 10
    RULE_assignmentStatement = 11
    RULE_constWord = 12
    RULE_pointerWord = 13
    RULE_reservedWord = 14
    RULE_dataTypes = 15
    RULE_int = 16
    RULE_float = 17
    RULE_char = 18
    RULE_referenceID = 19
    RULE_nameIdentifier = 20
    RULE_printFunction = 21

    ruleNames =  [ "prog", "expr", "opAnd", "opOr", "opCompare", "opAddOrSub", 
                   "opMultOrDiv", "opUnary", "brackets", "variableDefinition", 
                   "variableDeclaration", "assignmentStatement", "constWord", 
                   "pointerWord", "reservedWord", "dataTypes", "int", "float", 
                   "char", "referenceID", "nameIdentifier", "printFunction" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    POINTER=24
    POINTERS=25
    ID=26
    CHAR=27
    INT=28
    FLOAT=29
    WS=30
    COMMENT=31
    BLOCK_COMMENT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MyGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.opAnd(0)
                self.state = 47
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.opAnd(0)
                self.state = 50
                self.match(MyGrammarParser.T__0)
                self.state = 51
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opOr(self):
            return self.getTypedRuleContext(MyGrammarParser.OpOrContext,0)


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAnd" ):
                listener.enterOpAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAnd" ):
                listener.exitOpAnd(self)



    def opAnd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpAndContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_opAnd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    self.match(MyGrammarParser.T__1)
                    self.state = 60
                    self.opOr(0) 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opCompare(self):
            return self.getTypedRuleContext(MyGrammarParser.OpCompareContext,0)


        def opOr(self):
            return self.getTypedRuleContext(MyGrammarParser.OpOrContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpOr" ):
                listener.enterOpOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpOr" ):
                listener.exitOpOr(self)



    def opOr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpOrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_opOr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
                    self.state = 69
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 70
                    self.match(MyGrammarParser.T__2)
                    self.state = 71
                    self.opCompare(0) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpCompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def opCompare(self):
            return self.getTypedRuleContext(MyGrammarParser.OpCompareContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opCompare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpCompare" ):
                listener.enterOpCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpCompare" ):
                listener.exitOpCompare(self)



    def opCompare(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpCompareContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_opCompare, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 78
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.state = 79
                self.opAddOrSub(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 82
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 83
                        self.match(MyGrammarParser.T__3)
                        self.state = 84
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 85
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 86
                        self.match(MyGrammarParser.T__4)
                        self.state = 87
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 88
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 89
                        self.match(MyGrammarParser.T__5)
                        self.state = 90
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 91
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 92
                        self.match(MyGrammarParser.T__6)
                        self.state = 93
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.match(MyGrammarParser.T__7)
                        self.state = 96
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 97
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 98
                        self.match(MyGrammarParser.T__8)
                        pass

             
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpAddOrSubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opMultOrDiv(self):
            return self.getTypedRuleContext(MyGrammarParser.OpMultOrDivContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opAddOrSub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAddOrSub" ):
                listener.enterOpAddOrSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAddOrSub" ):
                listener.exitOpAddOrSub(self)



    def opAddOrSub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpAddOrSubContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_opAddOrSub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 107
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 108
                        self.match(MyGrammarParser.T__9)
                        self.state = 109
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 110
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 111
                        self.match(MyGrammarParser.T__10)
                        self.state = 112
                        self.opMultOrDiv(0)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpMultOrDivContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opUnary(self):
            return self.getTypedRuleContext(MyGrammarParser.OpUnaryContext,0)


        def opMultOrDiv(self):
            return self.getTypedRuleContext(MyGrammarParser.OpMultOrDivContext,0)


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_opMultOrDiv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMultOrDiv" ):
                listener.enterOpMultOrDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMultOrDiv" ):
                listener.exitOpMultOrDiv(self)



    def opMultOrDiv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpMultOrDivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_opMultOrDiv, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 130
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 121
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 122
                        self.match(MyGrammarParser.POINTER)
                        self.state = 123
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 124
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 125
                        self.match(MyGrammarParser.T__11)
                        self.state = 126
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 127
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 128
                        self.match(MyGrammarParser.T__12)
                        self.state = 129
                        self.opUnary()
                        pass

             
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpUnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brackets(self):
            return self.getTypedRuleContext(MyGrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opUnary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpUnary" ):
                listener.enterOpUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpUnary" ):
                listener.exitOpUnary(self)




    def opUnary(self):

        localctx = MyGrammarParser.OpUnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opUnary)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(MyGrammarParser.T__9)
                self.state = 136
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MyGrammarParser.T__10)
                self.state = 138
                self.brackets()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(MyGrammarParser.T__13)
                self.state = 140
                self.brackets()
                pass
            elif token in [15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.brackets()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDefinitionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentStatementContext,0)


        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def printFunction(self):
            return self.getTypedRuleContext(MyGrammarParser.PrintFunctionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_brackets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)




    def brackets(self):

        localctx = MyGrammarParser.BracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_brackets)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(MyGrammarParser.T__14)
                self.state = 145
                self.opAnd(0)
                self.state = 146
                self.match(MyGrammarParser.T__15)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.variableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.dataTypes()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.printFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)




    def variableDefinition(self):

        localctx = MyGrammarParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.variableDeclaration()
            self.state = 156
            self.match(MyGrammarParser.T__16)
            self.state = 157
            self.opAddOrSub(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = MyGrammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.constWord()
            self.state = 160
            self.referenceID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = MyGrammarParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignmentStatement)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.referenceID()
                self.state = 163
                self.match(MyGrammarParser.T__16)
                self.state = 164
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.dataTypes()
                self.state = 167
                self.match(MyGrammarParser.T__16)
                self.state = 168
                self.opAddOrSub(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(MyGrammarParser.T__14)
                self.state = 171
                self.opAnd(0)
                self.state = 172
                self.match(MyGrammarParser.T__15)
                self.state = 173
                self.match(MyGrammarParser.T__16)
                self.state = 174
                self.opAddOrSub(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointerWord(self):
            return self.getTypedRuleContext(MyGrammarParser.PointerWordContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_constWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstWord" ):
                listener.enterConstWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstWord" ):
                listener.exitConstWord(self)




    def constWord(self):

        localctx = MyGrammarParser.ConstWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constWord)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(MyGrammarParser.T__17)
                self.state = 179
                self.pointerWord()
                pass
            elif token in [19, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.pointerWord()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reservedWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ReservedWordContext,0)


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

        def POINTERS(self):
            return self.getToken(MyGrammarParser.POINTERS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_pointerWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerWord" ):
                listener.enterPointerWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerWord" ):
                listener.exitPointerWord(self)




    def pointerWord(self):

        localctx = MyGrammarParser.PointerWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pointerWord)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.reservedWord()
                self.state = 184
                self.match(MyGrammarParser.POINTER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.reservedWord()
                self.state = 187
                self.match(MyGrammarParser.POINTERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.reservedWord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReservedWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedWord" ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedWord" ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = MyGrammarParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(MyGrammarParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(MyGrammarParser.FloatContext,0)


        def char(self):
            return self.getTypedRuleContext(MyGrammarParser.CharContext,0)


        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_dataTypes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataTypes" ):
                listener.enterDataTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataTypes" ):
                listener.exitDataTypes(self)




    def dataTypes(self):

        localctx = MyGrammarParser.DataTypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dataTypes)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.int_()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.float_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.char()
                pass
            elif token in [22, 24, 25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.referenceID()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = MyGrammarParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MyGrammarParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MyGrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = MyGrammarParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MyGrammarParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(MyGrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = MyGrammarParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MyGrammarParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameIdentifier(self):
            return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,0)


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

        def POINTERS(self):
            return self.getToken(MyGrammarParser.POINTERS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_referenceID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceID" ):
                listener.enterReferenceID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceID" ):
                listener.exitReferenceID(self)




    def referenceID(self):

        localctx = MyGrammarParser.ReferenceIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_referenceID)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MyGrammarParser.T__21)
                self.state = 207
                self.nameIdentifier()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(MyGrammarParser.POINTER)
                self.state = 209
                self.nameIdentifier()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(MyGrammarParser.POINTERS)
                self.state = 211
                self.nameIdentifier()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_nameIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameIdentifier" ):
                listener.enterNameIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameIdentifier" ):
                listener.exitNameIdentifier(self)




    def nameIdentifier(self):

        localctx = MyGrammarParser.NameIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_nameIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_printFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunction" ):
                listener.enterPrintFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunction" ):
                listener.exitPrintFunction(self)




    def printFunction(self):

        localctx = MyGrammarParser.PrintFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_printFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MyGrammarParser.T__22)
            self.state = 218
            self.match(MyGrammarParser.T__14)
            self.state = 219
            self.opAnd(0)
            self.state = 220
            self.match(MyGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.opAnd_sempred
        self._predicates[3] = self.opOr_sempred
        self._predicates[4] = self.opCompare_sempred
        self._predicates[5] = self.opAddOrSub_sempred
        self._predicates[6] = self.opMultOrDiv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def opAnd_sempred(self, localctx:OpAndContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def opOr_sempred(self, localctx:OpOrContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def opCompare_sempred(self, localctx:OpCompareContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

    def opAddOrSub_sempred(self, localctx:OpAddOrSubContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def opMultOrDiv_sempred(self, localctx:OpMultOrDivContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




