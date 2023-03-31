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
        4,1,32,260,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,4,0,51,8,0,11,0,12,0,52,
        1,0,1,0,1,0,4,0,58,8,0,11,0,12,0,59,1,0,1,0,1,0,4,0,65,8,0,11,0,
        12,0,66,1,0,1,0,3,0,71,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,88,8,2,10,2,12,2,91,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,99,8,3,10,3,12,3,102,9,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,125,8,4,10,4,12,4,128,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,139,8,5,10,5,12,5,142,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,156,8,6,10,6,12,6,159,9,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,168,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,179,
        8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,202,8,11,1,12,1,12,
        1,12,3,12,207,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,216,8,
        13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,224,8,15,1,16,1,16,1,17,1,
        17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,239,8,19,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,1,22,4,22,249,8,22,11,22,12,22,
        250,1,22,4,22,254,8,22,11,22,12,22,255,3,22,258,8,22,1,22,0,5,4,
        6,8,10,12,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,0,1,1,0,19,21,279,0,70,1,0,0,0,2,79,1,0,0,0,4,81,1,0,
        0,0,6,92,1,0,0,0,8,103,1,0,0,0,10,129,1,0,0,0,12,143,1,0,0,0,14,
        167,1,0,0,0,16,178,1,0,0,0,18,180,1,0,0,0,20,184,1,0,0,0,22,201,
        1,0,0,0,24,206,1,0,0,0,26,215,1,0,0,0,28,217,1,0,0,0,30,223,1,0,
        0,0,32,225,1,0,0,0,34,227,1,0,0,0,36,229,1,0,0,0,38,238,1,0,0,0,
        40,240,1,0,0,0,42,242,1,0,0,0,44,257,1,0,0,0,46,47,3,44,22,0,47,
        48,3,2,1,0,48,49,3,44,22,0,49,51,1,0,0,0,50,46,1,0,0,0,51,52,1,0,
        0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,71,1,0,0,0,54,55,3,44,22,0,55,
        56,3,2,1,0,56,58,1,0,0,0,57,54,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,
        0,59,60,1,0,0,0,60,71,1,0,0,0,61,62,3,2,1,0,62,63,3,44,22,0,63,65,
        1,0,0,0,64,61,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,
        67,71,1,0,0,0,68,71,3,2,1,0,69,71,3,44,22,0,70,50,1,0,0,0,70,57,
        1,0,0,0,70,64,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,1,1,0,0,0,72,
        73,3,4,2,0,73,74,5,1,0,0,74,80,1,0,0,0,75,76,3,4,2,0,76,77,5,1,0,
        0,77,78,3,2,1,0,78,80,1,0,0,0,79,72,1,0,0,0,79,75,1,0,0,0,80,3,1,
        0,0,0,81,82,6,2,-1,0,82,83,3,6,3,0,83,89,1,0,0,0,84,85,10,2,0,0,
        85,86,5,2,0,0,86,88,3,6,3,0,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,
        0,0,0,89,90,1,0,0,0,90,5,1,0,0,0,91,89,1,0,0,0,92,93,6,3,-1,0,93,
        94,3,8,4,0,94,100,1,0,0,0,95,96,10,2,0,0,96,97,5,3,0,0,97,99,3,8,
        4,0,98,95,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,7,1,0,0,0,102,100,1,0,0,0,103,104,6,4,-1,0,104,105,3,10,5,0,
        105,126,1,0,0,0,106,107,10,7,0,0,107,108,5,4,0,0,108,125,3,10,5,
        0,109,110,10,6,0,0,110,111,5,5,0,0,111,125,3,10,5,0,112,113,10,5,
        0,0,113,114,5,6,0,0,114,125,3,10,5,0,115,116,10,4,0,0,116,117,5,
        7,0,0,117,125,3,10,5,0,118,119,10,3,0,0,119,120,5,8,0,0,120,125,
        3,10,5,0,121,122,10,2,0,0,122,123,5,9,0,0,123,125,3,10,5,0,124,106,
        1,0,0,0,124,109,1,0,0,0,124,112,1,0,0,0,124,115,1,0,0,0,124,118,
        1,0,0,0,124,121,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,
        1,0,0,0,127,9,1,0,0,0,128,126,1,0,0,0,129,130,6,5,-1,0,130,131,3,
        12,6,0,131,140,1,0,0,0,132,133,10,3,0,0,133,134,5,10,0,0,134,139,
        3,12,6,0,135,136,10,2,0,0,136,137,5,11,0,0,137,139,3,12,6,0,138,
        132,1,0,0,0,138,135,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,11,1,0,0,0,142,140,1,0,0,0,143,144,6,6,-1,0,144,
        145,3,14,7,0,145,157,1,0,0,0,146,147,10,4,0,0,147,148,5,24,0,0,148,
        156,3,14,7,0,149,150,10,3,0,0,150,151,5,12,0,0,151,156,3,14,7,0,
        152,153,10,2,0,0,153,154,5,13,0,0,154,156,3,14,7,0,155,146,1,0,0,
        0,155,149,1,0,0,0,155,152,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,
        0,157,158,1,0,0,0,158,13,1,0,0,0,159,157,1,0,0,0,160,161,5,10,0,
        0,161,168,3,16,8,0,162,163,5,11,0,0,163,168,3,16,8,0,164,165,5,14,
        0,0,165,168,3,16,8,0,166,168,3,16,8,0,167,160,1,0,0,0,167,162,1,
        0,0,0,167,164,1,0,0,0,167,166,1,0,0,0,168,15,1,0,0,0,169,170,5,15,
        0,0,170,171,3,4,2,0,171,172,5,16,0,0,172,179,1,0,0,0,173,179,3,18,
        9,0,174,179,3,20,10,0,175,179,3,22,11,0,176,179,3,30,15,0,177,179,
        3,42,21,0,178,169,1,0,0,0,178,173,1,0,0,0,178,174,1,0,0,0,178,175,
        1,0,0,0,178,176,1,0,0,0,178,177,1,0,0,0,179,17,1,0,0,0,180,181,3,
        20,10,0,181,182,5,17,0,0,182,183,3,4,2,0,183,19,1,0,0,0,184,185,
        3,24,12,0,185,186,3,38,19,0,186,21,1,0,0,0,187,188,3,38,19,0,188,
        189,5,17,0,0,189,190,3,10,5,0,190,202,1,0,0,0,191,192,3,30,15,0,
        192,193,5,17,0,0,193,194,3,10,5,0,194,202,1,0,0,0,195,196,5,15,0,
        0,196,197,3,4,2,0,197,198,5,16,0,0,198,199,5,17,0,0,199,200,3,4,
        2,0,200,202,1,0,0,0,201,187,1,0,0,0,201,191,1,0,0,0,201,195,1,0,
        0,0,202,23,1,0,0,0,203,204,5,18,0,0,204,207,3,26,13,0,205,207,3,
        26,13,0,206,203,1,0,0,0,206,205,1,0,0,0,207,25,1,0,0,0,208,209,3,
        28,14,0,209,210,5,24,0,0,210,216,1,0,0,0,211,212,3,28,14,0,212,213,
        5,25,0,0,213,216,1,0,0,0,214,216,3,28,14,0,215,208,1,0,0,0,215,211,
        1,0,0,0,215,214,1,0,0,0,216,27,1,0,0,0,217,218,7,0,0,0,218,29,1,
        0,0,0,219,224,3,32,16,0,220,224,3,34,17,0,221,224,3,36,18,0,222,
        224,3,38,19,0,223,219,1,0,0,0,223,220,1,0,0,0,223,221,1,0,0,0,223,
        222,1,0,0,0,224,31,1,0,0,0,225,226,5,28,0,0,226,33,1,0,0,0,227,228,
        5,29,0,0,228,35,1,0,0,0,229,230,5,27,0,0,230,37,1,0,0,0,231,232,
        5,22,0,0,232,239,3,40,20,0,233,234,5,24,0,0,234,239,3,40,20,0,235,
        236,5,25,0,0,236,239,3,40,20,0,237,239,3,40,20,0,238,231,1,0,0,0,
        238,233,1,0,0,0,238,235,1,0,0,0,238,237,1,0,0,0,239,39,1,0,0,0,240,
        241,5,26,0,0,241,41,1,0,0,0,242,243,5,23,0,0,243,244,5,15,0,0,244,
        245,3,4,2,0,245,246,5,16,0,0,246,43,1,0,0,0,247,249,5,31,0,0,248,
        247,1,0,0,0,249,250,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,
        258,1,0,0,0,252,254,5,30,0,0,253,252,1,0,0,0,254,255,1,0,0,0,255,
        253,1,0,0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,248,1,0,0,0,257,
        253,1,0,0,0,258,45,1,0,0,0,23,52,59,66,70,79,89,100,124,126,138,
        140,155,157,167,178,201,206,215,223,238,250,255,257
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

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.CommentContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.CommentContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)


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
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 46
                    self.comment()
                    self.state = 47
                    self.expr()
                    self.state = 48
                    self.comment()
                    self.state = 52 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30 or _la==31):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 54
                    self.comment()
                    self.state = 55
                    self.expr()
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30 or _la==31):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 61
                    self.expr()
                    self.state = 62
                    self.comment()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073531904) != 0)):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.comment()
                pass


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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.opAnd(0)
                self.state = 73
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.opAnd(0)
                self.state = 76
                self.match(MyGrammarParser.T__0)
                self.state = 77
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
            self.state = 82
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
                    self.state = 84
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 85
                    self.match(MyGrammarParser.T__1)
                    self.state = 86
                    self.opOr(0) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 93
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
                    self.state = 95
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 96
                    self.match(MyGrammarParser.T__2)
                    self.state = 97
                    self.opCompare(0) 
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 104
            self.opAddOrSub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 106
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 107
                        self.match(MyGrammarParser.T__3)
                        self.state = 108
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 109
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 110
                        self.match(MyGrammarParser.T__4)
                        self.state = 111
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 112
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 113
                        self.match(MyGrammarParser.T__5)
                        self.state = 114
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 115
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 116
                        self.match(MyGrammarParser.T__6)
                        self.state = 117
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 118
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 119
                        self.match(MyGrammarParser.T__7)
                        self.state = 120
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 121
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 122
                        self.match(MyGrammarParser.T__8)
                        self.state = 123
                        self.opAddOrSub(0)
                        pass

             
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 130
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 138
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 132
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 133
                        self.match(MyGrammarParser.T__9)
                        self.state = 134
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 135
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 136
                        self.match(MyGrammarParser.T__10)
                        self.state = 137
                        self.opMultOrDiv(0)
                        pass

             
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 144
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 146
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 147
                        self.match(MyGrammarParser.POINTER)
                        self.state = 148
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 149
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 150
                        self.match(MyGrammarParser.T__11)
                        self.state = 151
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 152
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 153
                        self.match(MyGrammarParser.T__12)
                        self.state = 154
                        self.opUnary()
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(MyGrammarParser.T__9)
                self.state = 161
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(MyGrammarParser.T__10)
                self.state = 163
                self.brackets()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(MyGrammarParser.T__13)
                self.state = 165
                self.brackets()
                pass
            elif token in [15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
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
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(MyGrammarParser.T__14)
                self.state = 170
                self.opAnd(0)
                self.state = 171
                self.match(MyGrammarParser.T__15)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.variableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.dataTypes()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
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
            self.state = 180
            self.variableDeclaration()
            self.state = 181
            self.match(MyGrammarParser.T__16)
            self.state = 182
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
            self.state = 184
            self.constWord()
            self.state = 185
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.referenceID()
                self.state = 188
                self.match(MyGrammarParser.T__16)
                self.state = 189
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.dataTypes()
                self.state = 192
                self.match(MyGrammarParser.T__16)
                self.state = 193
                self.opAddOrSub(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(MyGrammarParser.T__14)
                self.state = 196
                self.opAnd(0)
                self.state = 197
                self.match(MyGrammarParser.T__15)
                self.state = 198
                self.match(MyGrammarParser.T__16)
                self.state = 199
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
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(MyGrammarParser.T__17)
                self.state = 204
                self.pointerWord()
                pass
            elif token in [19, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.reservedWord()
                self.state = 209
                self.match(MyGrammarParser.POINTER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.reservedWord()
                self.state = 212
                self.match(MyGrammarParser.POINTERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
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
            self.state = 217
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
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.int_()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.float_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.char()
                pass
            elif token in [22, 24, 25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
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
            self.state = 225
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
            self.state = 227
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
            self.state = 229
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
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(MyGrammarParser.T__21)
                self.state = 232
                self.nameIdentifier()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(MyGrammarParser.POINTER)
                self.state = 234
                self.nameIdentifier()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(MyGrammarParser.POINTERS)
                self.state = 236
                self.nameIdentifier()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
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
            self.state = 240
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
            self.state = 242
            self.match(MyGrammarParser.T__22)
            self.state = 243
            self.match(MyGrammarParser.T__14)
            self.state = 244
            self.opAnd(0)
            self.state = 245
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
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 247
                        self.match(MyGrammarParser.BLOCK_COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 250 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 252
                        self.match(MyGrammarParser.COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 255 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
         




