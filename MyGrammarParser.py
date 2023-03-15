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
        4,1,20,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,2,12,2,
        43,9,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,4,1,
        4,1,4,3,4,59,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,9,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,92,8,5,10,5,12,5,95,9,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,109,8,6,10,6,12,6,112,9,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,121,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,129,8,8,1,9,1,9,1,10,1,10,1,10,0,5,4,6,8,10,12,11,0,2,4,6,8,10,
        12,14,16,18,20,0,0,143,0,22,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,
        44,1,0,0,0,8,58,1,0,0,0,10,82,1,0,0,0,12,96,1,0,0,0,14,120,1,0,0,
        0,16,128,1,0,0,0,18,130,1,0,0,0,20,132,1,0,0,0,22,23,3,2,1,0,23,
        1,1,0,0,0,24,25,3,4,2,0,25,26,5,1,0,0,26,32,1,0,0,0,27,28,3,4,2,
        0,28,29,5,1,0,0,29,30,3,2,1,0,30,32,1,0,0,0,31,24,1,0,0,0,31,27,
        1,0,0,0,32,3,1,0,0,0,33,34,6,2,-1,0,34,35,3,6,3,0,35,41,1,0,0,0,
        36,37,10,2,0,0,37,38,5,2,0,0,38,40,3,6,3,0,39,36,1,0,0,0,40,43,1,
        0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,
        45,6,3,-1,0,45,46,3,8,4,0,46,52,1,0,0,0,47,48,10,2,0,0,48,49,5,3,
        0,0,49,51,3,8,4,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,56,6,4,-1,0,56,59,3,10,5,0,
        57,59,3,10,5,0,58,55,1,0,0,0,58,57,1,0,0,0,59,79,1,0,0,0,60,61,10,
        8,0,0,61,62,5,4,0,0,62,78,3,10,5,0,63,64,10,7,0,0,64,65,5,5,0,0,
        65,78,3,10,5,0,66,67,10,6,0,0,67,68,5,6,0,0,68,78,3,10,5,0,69,70,
        10,5,0,0,70,71,5,7,0,0,71,78,3,10,5,0,72,73,10,4,0,0,73,74,5,8,0,
        0,74,78,3,10,5,0,75,76,10,3,0,0,76,78,5,9,0,0,77,60,1,0,0,0,77,63,
        1,0,0,0,77,66,1,0,0,0,77,69,1,0,0,0,77,72,1,0,0,0,77,75,1,0,0,0,
        78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,9,1,0,0,0,81,79,1,0,
        0,0,82,83,6,5,-1,0,83,84,3,12,6,0,84,93,1,0,0,0,85,86,10,3,0,0,86,
        87,5,10,0,0,87,92,3,12,6,0,88,89,10,2,0,0,89,90,5,11,0,0,90,92,3,
        12,6,0,91,85,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,
        94,1,0,0,0,94,11,1,0,0,0,95,93,1,0,0,0,96,97,6,6,-1,0,97,98,3,14,
        7,0,98,110,1,0,0,0,99,100,10,4,0,0,100,101,5,12,0,0,101,109,3,14,
        7,0,102,103,10,3,0,0,103,104,5,13,0,0,104,109,3,14,7,0,105,106,10,
        2,0,0,106,107,5,14,0,0,107,109,3,14,7,0,108,99,1,0,0,0,108,102,1,
        0,0,0,108,105,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,
        0,0,0,111,13,1,0,0,0,112,110,1,0,0,0,113,114,5,10,0,0,114,121,3,
        16,8,0,115,116,5,11,0,0,116,121,3,16,8,0,117,118,5,15,0,0,118,121,
        3,16,8,0,119,121,3,16,8,0,120,113,1,0,0,0,120,115,1,0,0,0,120,117,
        1,0,0,0,120,119,1,0,0,0,121,15,1,0,0,0,122,123,5,16,0,0,123,124,
        3,4,2,0,124,125,5,17,0,0,125,129,1,0,0,0,126,129,3,18,9,0,127,129,
        3,20,10,0,128,122,1,0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,17,
        1,0,0,0,130,131,5,18,0,0,131,19,1,0,0,0,132,133,5,19,0,0,133,21,
        1,0,0,0,12,31,41,52,58,77,79,91,93,108,110,120,128
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'&&'", "'||'", "'=='", "'<='", 
                     "'>='", "'!='", "'<'", "'>'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_opAnd = 2
    RULE_opOr = 3
    RULE_opCompare = 4
    RULE_opAddOrSub = 5
    RULE_opMultOrDiv = 6
    RULE_opUnary = 7
    RULE_brackets = 8
    RULE_int = 9
    RULE_float = 10

    ruleNames =  [ "prog", "expr", "opAnd", "opOr", "opCompare", "opAddOrSub", 
                   "opMultOrDiv", "opUnary", "brackets", "int", "float" ]

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
    INT=18
    FLOAT=19
    WS=20

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
            self.state = 22
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.opAnd(0)
                self.state = 25
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.opAnd(0)
                self.state = 28
                self.match(MyGrammarParser.T__0)
                self.state = 29
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
            self.state = 34
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
                    self.state = 36
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 37
                    self.match(MyGrammarParser.T__1)
                    self.state = 38
                    self.opOr(0) 
                self.state = 43
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
            self.state = 45
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
                    self.state = 47
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 48
                    self.match(MyGrammarParser.T__2)
                    self.state = 49
                    self.opCompare(0) 
                self.state = 54
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
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 56
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.state = 57
                self.opAddOrSub(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 60
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 61
                        self.match(MyGrammarParser.T__3)
                        self.state = 62
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 63
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 64
                        self.match(MyGrammarParser.T__4)
                        self.state = 65
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 66
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 67
                        self.match(MyGrammarParser.T__5)
                        self.state = 68
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 69
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 70
                        self.match(MyGrammarParser.T__6)
                        self.state = 71
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        self.match(MyGrammarParser.T__7)
                        self.state = 74
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        self.match(MyGrammarParser.T__8)
                        pass

             
                self.state = 81
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
            self.state = 83
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        self.match(MyGrammarParser.T__9)
                        self.state = 87
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 88
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 89
                        self.match(MyGrammarParser.T__10)
                        self.state = 90
                        self.opMultOrDiv(0)
                        pass

             
                self.state = 95
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
            self.state = 97
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 108
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 99
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 100
                        self.match(MyGrammarParser.T__11)
                        self.state = 101
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 102
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 103
                        self.match(MyGrammarParser.T__12)
                        self.state = 104
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 105
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 106
                        self.match(MyGrammarParser.T__13)
                        self.state = 107
                        self.opUnary()
                        pass

             
                self.state = 112
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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MyGrammarParser.T__9)
                self.state = 114
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(MyGrammarParser.T__10)
                self.state = 116
                self.brackets()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(MyGrammarParser.T__14)
                self.state = 118
                self.brackets()
                pass
            elif token in [16, 18, 19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
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


        def int_(self):
            return self.getTypedRuleContext(MyGrammarParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(MyGrammarParser.FloatContext,0)


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
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(MyGrammarParser.T__15)
                self.state = 123
                self.opAnd(0)
                self.state = 124
                self.match(MyGrammarParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.int_()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.float_()
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
        self.enterRule(localctx, 18, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
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
        self.enterRule(localctx, 20, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(MyGrammarParser.FLOAT)
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
         




