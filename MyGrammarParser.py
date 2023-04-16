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
        4,1,32,239,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,
        70,9,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,9,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,5,5,118,8,5,10,5,12,5,121,9,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,135,8,6,10,6,12,6,138,9,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,147,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,3,8,158,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,181,
        8,11,1,12,1,12,1,12,3,12,186,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,195,8,13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,203,8,15,1,
        16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,
        19,218,8,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,22,4,22,228,8,22,
        11,22,12,22,229,1,22,4,22,233,8,22,11,22,12,22,234,3,22,237,8,22,
        1,22,0,5,4,6,8,10,12,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,0,1,1,0,19,21,252,0,46,1,0,0,0,2,58,1,0,
        0,0,4,60,1,0,0,0,6,71,1,0,0,0,8,82,1,0,0,0,10,108,1,0,0,0,12,122,
        1,0,0,0,14,146,1,0,0,0,16,157,1,0,0,0,18,159,1,0,0,0,20,163,1,0,
        0,0,22,180,1,0,0,0,24,185,1,0,0,0,26,194,1,0,0,0,28,196,1,0,0,0,
        30,202,1,0,0,0,32,204,1,0,0,0,34,206,1,0,0,0,36,208,1,0,0,0,38,217,
        1,0,0,0,40,219,1,0,0,0,42,221,1,0,0,0,44,236,1,0,0,0,46,47,3,2,1,
        0,47,1,1,0,0,0,48,49,3,4,2,0,49,50,5,1,0,0,50,59,1,0,0,0,51,52,3,
        4,2,0,52,53,5,1,0,0,53,54,3,2,1,0,54,59,1,0,0,0,55,56,3,44,22,0,
        56,57,3,2,1,0,57,59,1,0,0,0,58,48,1,0,0,0,58,51,1,0,0,0,58,55,1,
        0,0,0,59,3,1,0,0,0,60,61,6,2,-1,0,61,62,3,6,3,0,62,68,1,0,0,0,63,
        64,10,2,0,0,64,65,5,2,0,0,65,67,3,6,3,0,66,63,1,0,0,0,67,70,1,0,
        0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,5,1,0,0,0,70,68,1,0,0,0,71,72,
        6,3,-1,0,72,73,3,8,4,0,73,79,1,0,0,0,74,75,10,2,0,0,75,76,5,3,0,
        0,76,78,3,8,4,0,77,74,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,
        1,0,0,0,80,7,1,0,0,0,81,79,1,0,0,0,82,83,6,4,-1,0,83,84,3,10,5,0,
        84,105,1,0,0,0,85,86,10,7,0,0,86,87,5,4,0,0,87,104,3,10,5,0,88,89,
        10,6,0,0,89,90,5,5,0,0,90,104,3,10,5,0,91,92,10,5,0,0,92,93,5,6,
        0,0,93,104,3,10,5,0,94,95,10,4,0,0,95,96,5,7,0,0,96,104,3,10,5,0,
        97,98,10,3,0,0,98,99,5,8,0,0,99,104,3,10,5,0,100,101,10,2,0,0,101,
        102,5,9,0,0,102,104,3,10,5,0,103,85,1,0,0,0,103,88,1,0,0,0,103,91,
        1,0,0,0,103,94,1,0,0,0,103,97,1,0,0,0,103,100,1,0,0,0,104,107,1,
        0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,9,1,0,0,0,107,105,1,0,
        0,0,108,109,6,5,-1,0,109,110,3,12,6,0,110,119,1,0,0,0,111,112,10,
        3,0,0,112,113,5,10,0,0,113,118,3,12,6,0,114,115,10,2,0,0,115,116,
        5,11,0,0,116,118,3,12,6,0,117,111,1,0,0,0,117,114,1,0,0,0,118,121,
        1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,11,1,0,0,0,121,119,1,
        0,0,0,122,123,6,6,-1,0,123,124,3,14,7,0,124,136,1,0,0,0,125,126,
        10,4,0,0,126,127,5,24,0,0,127,135,3,14,7,0,128,129,10,3,0,0,129,
        130,5,12,0,0,130,135,3,14,7,0,131,132,10,2,0,0,132,133,5,13,0,0,
        133,135,3,14,7,0,134,125,1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,0,
        135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,13,1,0,0,0,138,
        136,1,0,0,0,139,140,5,10,0,0,140,147,3,16,8,0,141,142,5,11,0,0,142,
        147,3,16,8,0,143,144,5,14,0,0,144,147,3,16,8,0,145,147,3,16,8,0,
        146,139,1,0,0,0,146,141,1,0,0,0,146,143,1,0,0,0,146,145,1,0,0,0,
        147,15,1,0,0,0,148,149,5,15,0,0,149,150,3,4,2,0,150,151,5,16,0,0,
        151,158,1,0,0,0,152,158,3,18,9,0,153,158,3,20,10,0,154,158,3,22,
        11,0,155,158,3,30,15,0,156,158,3,42,21,0,157,148,1,0,0,0,157,152,
        1,0,0,0,157,153,1,0,0,0,157,154,1,0,0,0,157,155,1,0,0,0,157,156,
        1,0,0,0,158,17,1,0,0,0,159,160,3,20,10,0,160,161,5,17,0,0,161,162,
        3,4,2,0,162,19,1,0,0,0,163,164,3,24,12,0,164,165,3,38,19,0,165,21,
        1,0,0,0,166,167,3,38,19,0,167,168,5,17,0,0,168,169,3,10,5,0,169,
        181,1,0,0,0,170,171,3,30,15,0,171,172,5,17,0,0,172,173,3,10,5,0,
        173,181,1,0,0,0,174,175,5,15,0,0,175,176,3,4,2,0,176,177,5,16,0,
        0,177,178,5,17,0,0,178,179,3,4,2,0,179,181,1,0,0,0,180,166,1,0,0,
        0,180,170,1,0,0,0,180,174,1,0,0,0,181,23,1,0,0,0,182,183,5,18,0,
        0,183,186,3,26,13,0,184,186,3,26,13,0,185,182,1,0,0,0,185,184,1,
        0,0,0,186,25,1,0,0,0,187,188,3,28,14,0,188,189,5,24,0,0,189,195,
        1,0,0,0,190,191,3,28,14,0,191,192,5,25,0,0,192,195,1,0,0,0,193,195,
        3,28,14,0,194,187,1,0,0,0,194,190,1,0,0,0,194,193,1,0,0,0,195,27,
        1,0,0,0,196,197,7,0,0,0,197,29,1,0,0,0,198,203,3,32,16,0,199,203,
        3,34,17,0,200,203,3,36,18,0,201,203,3,38,19,0,202,198,1,0,0,0,202,
        199,1,0,0,0,202,200,1,0,0,0,202,201,1,0,0,0,203,31,1,0,0,0,204,205,
        5,28,0,0,205,33,1,0,0,0,206,207,5,29,0,0,207,35,1,0,0,0,208,209,
        5,27,0,0,209,37,1,0,0,0,210,211,5,22,0,0,211,218,3,40,20,0,212,213,
        5,24,0,0,213,218,3,40,20,0,214,215,5,25,0,0,215,218,3,40,20,0,216,
        218,3,40,20,0,217,210,1,0,0,0,217,212,1,0,0,0,217,214,1,0,0,0,217,
        216,1,0,0,0,218,39,1,0,0,0,219,220,5,26,0,0,220,41,1,0,0,0,221,222,
        5,23,0,0,222,223,5,15,0,0,223,224,3,4,2,0,224,225,5,16,0,0,225,43,
        1,0,0,0,226,228,5,31,0,0,227,226,1,0,0,0,228,229,1,0,0,0,229,227,
        1,0,0,0,229,230,1,0,0,0,230,237,1,0,0,0,231,233,5,30,0,0,232,231,
        1,0,0,0,233,234,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,237,
        1,0,0,0,236,227,1,0,0,0,236,232,1,0,0,0,237,45,1,0,0,0,19,58,68,
        79,103,105,117,119,134,136,146,157,180,185,194,202,217,229,234,236
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
                      "COMMENT", "BLOCK_COMMENT", "WS" ]

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
    RULE_comment = 22

    ruleNames =  [ "prog", "expr", "opAnd", "opOr", "opCompare", "opAddOrSub", 
                   "opMultOrDiv", "opUnary", "brackets", "variableDefinition", 
                   "variableDeclaration", "assignmentStatement", "constWord", 
                   "pointerWord", "reservedWord", "dataTypes", "int", "float", 
                   "char", "referenceID", "nameIdentifier", "printFunction", 
                   "comment" ]

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
    COMMENT=30
    BLOCK_COMMENT=31
    WS=32

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
            self.state = 46
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


        def comment(self):
            return self.getTypedRuleContext(MyGrammarParser.CommentContext,0)


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
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.opAnd(0)
                self.state = 49
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.opAnd(0)
                self.state = 52
                self.match(MyGrammarParser.T__0)
                self.state = 53
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.comment()
                self.state = 56
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
            self.state = 61
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
                    self.state = 63
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 64
                    self.match(MyGrammarParser.T__1)
                    self.state = 65
                    self.opOr(0) 
                self.state = 70
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
            self.state = 72
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
                    self.state = 74
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 75
                    self.match(MyGrammarParser.T__2)
                    self.state = 76
                    self.opCompare(0) 
                self.state = 81
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
            self.state = 83
            self.opAddOrSub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 85
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 86
                        self.match(MyGrammarParser.T__3)
                        self.state = 87
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 88
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 89
                        self.match(MyGrammarParser.T__4)
                        self.state = 90
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 91
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 92
                        self.match(MyGrammarParser.T__5)
                        self.state = 93
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.match(MyGrammarParser.T__6)
                        self.state = 96
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 97
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 98
                        self.match(MyGrammarParser.T__7)
                        self.state = 99
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 100
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 101
                        self.match(MyGrammarParser.T__8)
                        self.state = 102
                        self.opAddOrSub(0)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 109
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 111
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 112
                        self.match(MyGrammarParser.T__9)
                        self.state = 113
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 114
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 115
                        self.match(MyGrammarParser.T__10)
                        self.state = 116
                        self.opMultOrDiv(0)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 123
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 125
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 126
                        self.match(MyGrammarParser.POINTER)
                        self.state = 127
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 128
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 129
                        self.match(MyGrammarParser.T__11)
                        self.state = 130
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 131
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 132
                        self.match(MyGrammarParser.T__12)
                        self.state = 133
                        self.opUnary()
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(MyGrammarParser.T__9)
                self.state = 140
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MyGrammarParser.T__10)
                self.state = 142
                self.brackets()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(MyGrammarParser.T__13)
                self.state = 144
                self.brackets()
                pass
            elif token in [15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(MyGrammarParser.T__14)
                self.state = 149
                self.opAnd(0)
                self.state = 150
                self.match(MyGrammarParser.T__15)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.variableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.dataTypes()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
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


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


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
            self.state = 159
            self.variableDeclaration()
            self.state = 160
            self.match(MyGrammarParser.T__16)
            self.state = 161
            self.opAnd(0)
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
            self.state = 163
            self.constWord()
            self.state = 164
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


        def opAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.OpAndContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.OpAndContext,i)


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
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.referenceID()
                self.state = 167
                self.match(MyGrammarParser.T__16)
                self.state = 168
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.dataTypes()
                self.state = 171
                self.match(MyGrammarParser.T__16)
                self.state = 172
                self.opAddOrSub(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(MyGrammarParser.T__14)
                self.state = 175
                self.opAnd(0)
                self.state = 176
                self.match(MyGrammarParser.T__15)
                self.state = 177
                self.match(MyGrammarParser.T__16)
                self.state = 178
                self.opAnd(0)
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
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(MyGrammarParser.T__17)
                self.state = 183
                self.pointerWord()
                pass
            elif token in [19, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.reservedWord()
                self.state = 188
                self.match(MyGrammarParser.POINTER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.reservedWord()
                self.state = 191
                self.match(MyGrammarParser.POINTERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
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
            self.state = 196
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
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.int_()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.float_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.char()
                pass
            elif token in [22, 24, 25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
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
            self.state = 204
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
            self.state = 206
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
            self.state = 208
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(MyGrammarParser.T__21)
                self.state = 211
                self.nameIdentifier()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MyGrammarParser.POINTER)
                self.state = 213
                self.nameIdentifier()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(MyGrammarParser.POINTERS)
                self.state = 215
                self.nameIdentifier()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
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
            self.state = 219
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
            self.state = 221
            self.match(MyGrammarParser.T__22)
            self.state = 222
            self.match(MyGrammarParser.T__14)
            self.state = 223
            self.opAnd(0)
            self.state = 224
            self.match(MyGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.BLOCK_COMMENT)
            else:
                return self.getToken(MyGrammarParser.BLOCK_COMMENT, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.COMMENT)
            else:
                return self.getToken(MyGrammarParser.COMMENT, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = MyGrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comment)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 226
                        self.match(MyGrammarParser.BLOCK_COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 229 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 231
                        self.match(MyGrammarParser.COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 234 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

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
         




