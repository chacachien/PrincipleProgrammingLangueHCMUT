# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\31\n\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3")
        buf.write("\3\2\'(\2!\2\f\3\2\2\2\4\17\3\2\2\2\6\30\3\2\2\2\b\36")
        buf.write("\3\2\2\2\n \3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2")
        buf.write("\2\2\17\20\7\r\2\2\20\21\5\6\4\2\21\22\7\16\2\2\22\5\3")
        buf.write("\2\2\2\23\24\5\b\5\2\24\25\7\22\2\2\25\26\5\6\4\2\26\31")
        buf.write("\3\2\2\2\27\31\5\b\5\2\30\23\3\2\2\2\30\27\3\2\2\2\31")
        buf.write("\7\3\2\2\2\32\37\7\b\2\2\33\37\7\t\2\2\34\37\5\n\6\2\35")
        buf.write("\37\7\n\2\2\36\32\3\2\2\2\36\33\3\2\2\2\36\34\3\2\2\2")
        buf.write("\36\35\3\2\2\2\37\t\3\2\2\2 !\t\2\2\2!\13\3\2\2\2\4\30")
        buf.write("\36")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'int'", "'float'", "'boolean'", 
                     "'string'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "':'", "'\t'", "'\f'", "'\r'", "'\n'", "'\b'", 
                     "'class'", "'static'", "'final'", "'break'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'if'", "'new'", "'then'", 
                     "'for'", "'return'", "'true'", "'false'", "'void'", 
                     "'nil'", "'this'", "'to'", "'downto'", "'=='", "'!='", 
                     "'&&'", "'<='", "'>='", "'||'", "'+'", "'-'", "'%'", 
                     "'*'", "'/'", "'\\'", "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                      "STRINGTYPE", "INTLIT", "FLOATLIT", "STRINGLIT", "LB", 
                      "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COMMA", "DOT", 
                      "COLON", "TAB", "FF", "CR", "LR", "BS", "CLASS", "STATIC", 
                      "FINAL", "BREAK", "CONTINUTE", "DO", "ELSE", "EXTENDS", 
                      "IF", "NEW", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "TO", "DOWNTO", "EQE", "NEQ", 
                      "AND", "LET", "GET", "OR", "ADD", "SUB", "MOD", "MUL", 
                      "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", "CONCATE", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_arraylist = 1
    RULE_array = 2
    RULE_arrayelement = 3
    RULE_booleanlit = 4

    ruleNames =  [ "program", "arraylist", "array", "arrayelement", "booleanlit" ]

    EOF = Token.EOF
    COMMENT=1
    INTTYPE=2
    FLOATYPE=3
    BOOLEANTYPE=4
    STRINGTYPE=5
    INTLIT=6
    FLOATLIT=7
    STRINGLIT=8
    LB=9
    RB=10
    LP=11
    RP=12
    LSB=13
    RSB=14
    SEMI=15
    COMMA=16
    DOT=17
    COLON=18
    TAB=19
    FF=20
    CR=21
    LR=22
    BS=23
    CLASS=24
    STATIC=25
    FINAL=26
    BREAK=27
    CONTINUTE=28
    DO=29
    ELSE=30
    EXTENDS=31
    IF=32
    NEW=33
    THEN=34
    FOR=35
    RETURN=36
    TRUE=37
    FALSE=38
    VOID=39
    NIL=40
    THIS=41
    TO=42
    DOWNTO=43
    EQE=44
    NEQ=45
    AND=46
    LET=47
    GET=48
    OR=49
    ADD=50
    SUB=51
    MOD=52
    MUL=53
    FDIV=54
    IDIV=55
    EQ=56
    LT=57
    GT=58
    NOT=59
    CONCATE=60
    ID=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraylist(self):
            return self.getTypedRuleContext(BKOOLParser.ArraylistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.arraylist()
            self.state = 11
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def array(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = BKOOLParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arraylist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(BKOOLParser.LP)
            self.state = 14
            self.array()
            self.state = 15
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayelement(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayelementContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def array(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKOOLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.arrayelement()
                self.state = 18
                self.match(BKOOLParser.COMMA)
                self.state = 19
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.arrayelement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def booleanlit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanlitContext,0)


        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayelement" ):
                return visitor.visitArrayelement(self)
            else:
                return visitor.visitChildren(self)




    def arrayelement(self):

        localctx = BKOOLParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrayelement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.booleanlit()
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.match(BKOOLParser.STRINGLIT)
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


    class BooleanlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booleanlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanlit" ):
                return visitor.visitBooleanlit(self)
            else:
                return visitor.visitChildren(self)




    def booleanlit(self):

        localctx = BKOOLParser.BooleanlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_booleanlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
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





