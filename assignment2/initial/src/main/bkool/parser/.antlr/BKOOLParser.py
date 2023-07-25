# Generated from d:\HDD\Documents\Uni\hk223\PPL\assignment\code\PrincipleProgrammingLangueHCMUT\assignment2\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u024c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0092\n\3\3\4")
        buf.write("\3\4\3\4\3\4\5\4\u0098\n\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5")
        buf.write("\u00a0\n\5\3\6\3\6\3\6\3\6\5\6\u00a6\n\6\3\7\3\7\3\7\5")
        buf.write("\7\u00ab\n\7\3\b\3\b\5\b\u00af\n\b\3\b\3\b\3\t\5\t\u00b4")
        buf.write("\n\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00be\n\n\3\13")
        buf.write("\3\13\3\13\5\13\u00c3\n\13\3\f\3\f\5\f\u00c7\n\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00cd\n\f\3\f\3\f\3\f\3\f\5\f\u00d3\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\r\u00da\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\5\17\u00e1\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\5\20\u00ec\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00f3\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00fc\n\23\3\24\5\24\u00ff\n\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u010f\n\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3")
        buf.write("\30\5\30\u011a\n\30\3\31\3\31\3\31\3\31\5\31\u0120\n\31")
        buf.write("\3\32\3\32\5\32\u0124\n\32\3\33\3\33\3\33\3\33\5\33\u012a")
        buf.write("\n\33\3\34\3\34\3\34\3\35\5\35\u0130\n\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u013e\n\37\3 \3 \3 \3 \3 \3 \5 \u0146\n \3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3")
        buf.write("%\5%\u015d\n%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u0172\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\5\'\u017d\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u0188\n(\f(\16(\u018b\13(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\7)\u0196\n)\f)\16)\u0199\13)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\7*\u01aa\n*\f*\16*\u01ad\13*\3")
        buf.write("+\3+\3+\3+\3+\3+\7+\u01b5\n+\f+\16+\u01b8\13+\3,\3,\3")
        buf.write(",\5,\u01bd\n,\3-\3-\3-\3-\3-\5-\u01c4\n-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01ce\n.\3/\3/\3/\3/\3/\3/\3/\5/\u01d7\n")
        buf.write("/\7/\u01d9\n/\f/\16/\u01dc\13/\3\60\3\60\5\60\u01e0\n")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01e9\n\61")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u01ef\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\58\u020e\n8\39\39\39\39\39\59\u0215\n")
        buf.write("9\3:\3:\3:\3:\3:\5:\u021c\n:\3;\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0232\n>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3D\3D\3D\3D\3D\5D\u0245\n")
        buf.write("D\3E\3E\3E\3E\3E\3E\2\7NPRT\\F\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\b")
        buf.write("\3\2%&\4\2\t\n)*\5\2+,./\619\6\2./\61\62\64\65\679\5\2")
        buf.write("+-\60\60::\4\2\4\7((\2\u0256\2\u008a\3\2\2\2\4\u0091\3")
        buf.write("\2\2\2\6\u0093\3\2\2\2\b\u009f\3\2\2\2\n\u00a5\3\2\2\2")
        buf.write("\f\u00aa\3\2\2\2\16\u00ae\3\2\2\2\20\u00b3\3\2\2\2\22")
        buf.write("\u00bd\3\2\2\2\24\u00bf\3\2\2\2\26\u00d2\3\2\2\2\30\u00d9")
        buf.write("\3\2\2\2\32\u00db\3\2\2\2\34\u00e0\3\2\2\2\36\u00eb\3")
        buf.write("\2\2\2 \u00f2\3\2\2\2\"\u00f4\3\2\2\2$\u00fb\3\2\2\2&")
        buf.write("\u00fe\3\2\2\2(\u010e\3\2\2\2*\u0110\3\2\2\2,\u0114\3")
        buf.write("\2\2\2.\u0119\3\2\2\2\60\u011f\3\2\2\2\62\u0123\3\2\2")
        buf.write("\2\64\u0129\3\2\2\2\66\u012b\3\2\2\28\u012f\3\2\2\2:\u0134")
        buf.write("\3\2\2\2<\u013d\3\2\2\2>\u013f\3\2\2\2@\u0147\3\2\2\2")
        buf.write("B\u0150\3\2\2\2D\u0153\3\2\2\2F\u0156\3\2\2\2H\u015c\3")
        buf.write("\2\2\2J\u0171\3\2\2\2L\u017c\3\2\2\2N\u017e\3\2\2\2P\u018c")
        buf.write("\3\2\2\2R\u019a\3\2\2\2T\u01ae\3\2\2\2V\u01bc\3\2\2\2")
        buf.write("X\u01c3\3\2\2\2Z\u01cd\3\2\2\2\\\u01cf\3\2\2\2^\u01df")
        buf.write("\3\2\2\2`\u01e8\3\2\2\2b\u01ee\3\2\2\2d\u01f0\3\2\2\2")
        buf.write("f\u01f4\3\2\2\2h\u01f8\3\2\2\2j\u01ff\3\2\2\2l\u0206\3")
        buf.write("\2\2\2n\u020d\3\2\2\2p\u0214\3\2\2\2r\u021b\3\2\2\2t\u021d")
        buf.write("\3\2\2\2v\u0222\3\2\2\2x\u0228\3\2\2\2z\u0231\3\2\2\2")
        buf.write("|\u0233\3\2\2\2~\u0235\3\2\2\2\u0080\u0237\3\2\2\2\u0082")
        buf.write("\u0239\3\2\2\2\u0084\u023b\3\2\2\2\u0086\u0244\3\2\2\2")
        buf.write("\u0088\u0246\3\2\2\2\u008a\u008b\5\4\3\2\u008b\u008c\7")
        buf.write("\2\2\3\u008c\3\3\2\2\2\u008d\u008e\5\6\4\2\u008e\u008f")
        buf.write("\5\4\3\2\u008f\u0092\3\2\2\2\u0090\u0092\5\6\4\2\u0091")
        buf.write("\u008d\3\2\2\2\u0091\u0090\3\2\2\2\u0092\5\3\2\2\2\u0093")
        buf.write("\u0094\7\26\2\2\u0094\u0097\7(\2\2\u0095\u0096\7\35\2")
        buf.write("\2\u0096\u0098\7(\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7\r\2\2\u009a")
        buf.write("\u009b\5\b\5\2\u009b\u009c\7\16\2\2\u009c\7\3\2\2\2\u009d")
        buf.write("\u00a0\5\n\6\2\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u009e\3\2\2\2\u00a0\t\3\2\2\2\u00a1\u00a2\5\f\7")
        buf.write("\2\u00a2\u00a3\5\n\6\2\u00a3\u00a6\3\2\2\2\u00a4\u00a6")
        buf.write("\5\f\7\2\u00a5\u00a1\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6")
        buf.write("\13\3\2\2\2\u00a7\u00ab\5\16\b\2\u00a8\u00ab\5\34\17\2")
        buf.write("\u00a9\u00ab\5&\24\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\r\3\2\2\2\u00ac\u00af")
        buf.write("\5\20\t\2\u00ad\u00af\5\26\f\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7\22\2")
        buf.write("\2\u00b1\17\3\2\2\2\u00b2\u00b4\7\27\2\2\u00b3\u00b2\3")
        buf.write("\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\5\u0086D\2\u00b6\u00b7\5\22\n\2\u00b7\21\3\2\2\2\u00b8")
        buf.write("\u00b9\5\24\13\2\u00b9\u00ba\7\23\2\2\u00ba\u00bb\5\22")
        buf.write("\n\2\u00bb\u00be\3\2\2\2\u00bc\u00be\5\24\13\2\u00bd\u00b8")
        buf.write("\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\23\3\2\2\2\u00bf\u00c2")
        buf.write("\7(\2\2\u00c0\u00c1\7\67\2\2\u00c1\u00c3\5J&\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\25\3\2\2\2\u00c4\u00c6")
        buf.write("\7\30\2\2\u00c5\u00c7\7\27\2\2\u00c6\u00c5\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5\u0086")
        buf.write("D\2\u00c9\u00ca\5\30\r\2\u00ca\u00d3\3\2\2\2\u00cb\u00cd")
        buf.write("\7\27\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00cf\7\30\2\2\u00cf\u00d0\5\u0086")
        buf.write("D\2\u00d0\u00d1\5\30\r\2\u00d1\u00d3\3\2\2\2\u00d2\u00c4")
        buf.write("\3\2\2\2\u00d2\u00cc\3\2\2\2\u00d3\27\3\2\2\2\u00d4\u00d5")
        buf.write("\5\32\16\2\u00d5\u00d6\7\23\2\2\u00d6\u00d7\5\30\r\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00da\5\32\16\2\u00d9\u00d4\3\2\2")
        buf.write("\2\u00d9\u00d8\3\2\2\2\u00da\31\3\2\2\2\u00db\u00dc\7")
        buf.write("(\2\2\u00dc\u00dd\7\67\2\2\u00dd\u00de\5J&\2\u00de\33")
        buf.write("\3\2\2\2\u00df\u00e1\7\27\2\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\5\u0086")
        buf.write("D\2\u00e3\u00e4\7(\2\2\u00e4\u00e5\7\13\2\2\u00e5\u00e6")
        buf.write("\5\36\20\2\u00e6\u00e7\7\f\2\2\u00e7\u00e8\5*\26\2\u00e8")
        buf.write("\35\3\2\2\2\u00e9\u00ec\5 \21\2\u00ea\u00ec\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\37\3\2\2\2\u00ed")
        buf.write("\u00ee\5\"\22\2\u00ee\u00ef\7\22\2\2\u00ef\u00f0\5 \21")
        buf.write("\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3\5\"\22\2\u00f2\u00ed")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3!\3\2\2\2\u00f4\u00f5")
        buf.write("\5\u0086D\2\u00f5\u00f6\5$\23\2\u00f6#\3\2\2\2\u00f7\u00f8")
        buf.write("\7(\2\2\u00f8\u00f9\7\23\2\2\u00f9\u00fc\5$\23\2\u00fa")
        buf.write("\u00fc\7(\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2")
        buf.write("\u00fc%\3\2\2\2\u00fd\u00ff\7\27\2\2\u00fe\u00fd\3\2\2")
        buf.write("\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\7(\2\2\u0101\u0102\7\13\2\2\u0102\u0103\5\36\20\2\u0103")
        buf.write("\u0104\7\f\2\2\u0104\u0105\5*\26\2\u0105\'\3\2\2\2\u0106")
        buf.write("\u010f\5*\26\2\u0107\u010f\5:\36\2\u0108\u010f\5> \2\u0109")
        buf.write("\u010f\5@!\2\u010a\u010f\5B\"\2\u010b\u010f\5D#\2\u010c")
        buf.write("\u010f\5F$\2\u010d\u010f\5H%\2\u010e\u0106\3\2\2\2\u010e")
        buf.write("\u0107\3\2\2\2\u010e\u0108\3\2\2\2\u010e\u0109\3\2\2\2")
        buf.write("\u010e\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010d\3\2\2\2\u010f)\3\2\2\2\u0110\u0111")
        buf.write("\7\r\2\2\u0111\u0112\5,\27\2\u0112\u0113\7\16\2\2\u0113")
        buf.write("+\3\2\2\2\u0114\u0115\5.\30\2\u0115\u0116\5\62\32\2\u0116")
        buf.write("-\3\2\2\2\u0117\u011a\5\60\31\2\u0118\u011a\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a/\3\2\2\2\u011b")
        buf.write("\u011c\5\66\34\2\u011c\u011d\5\60\31\2\u011d\u0120\3\2")
        buf.write("\2\2\u011e\u0120\5\66\34\2\u011f\u011b\3\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\61\3\2\2\2\u0121\u0124\5\64\33\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2")
        buf.write("\u0124\63\3\2\2\2\u0125\u0126\5(\25\2\u0126\u0127\5\64")
        buf.write("\33\2\u0127\u012a\3\2\2\2\u0128\u012a\5(\25\2\u0129\u0125")
        buf.write("\3\2\2\2\u0129\u0128\3\2\2\2\u012a\65\3\2\2\2\u012b\u012c")
        buf.write("\58\35\2\u012c\u012d\7\22\2\2\u012d\67\3\2\2\2\u012e\u0130")
        buf.write("\7\30\2\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\5\u0086D\2\u0132\u0133\5\30")
        buf.write("\r\2\u01339\3\2\2\2\u0134\u0135\5<\37\2\u0135\u0136\7")
        buf.write("\21\2\2\u0136\u0137\5J&\2\u0137\u0138\7\22\2\2\u0138;")
        buf.write("\3\2\2\2\u0139\u013e\5t;\2\u013a\u013e\7(\2\2\u013b\u013e")
        buf.write("\5d\63\2\u013c\u013e\5f\64\2\u013d\u0139\3\2\2\2\u013d")
        buf.write("\u013a\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e=\3\2\2\2\u013f\u0140\7\36\2\2\u0140\u0141\5J&\2")
        buf.write("\u0141\u0142\7 \2\2\u0142\u0145\5(\25\2\u0143\u0144\7")
        buf.write("\34\2\2\u0144\u0146\5(\25\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146?\3\2\2\2\u0147\u0148\7!\2\2\u0148")
        buf.write("\u0149\7(\2\2\u0149\u014a\7\21\2\2\u014a\u014b\5J&\2\u014b")
        buf.write("\u014c\t\2\2\2\u014c\u014d\5J&\2\u014d\u014e\7\33\2\2")
        buf.write("\u014e\u014f\5(\25\2\u014fA\3\2\2\2\u0150\u0151\7\31\2")
        buf.write("\2\u0151\u0152\7\22\2\2\u0152C\3\2\2\2\u0153\u0154\7\32")
        buf.write("\2\2\u0154\u0155\7\22\2\2\u0155E\3\2\2\2\u0156\u0157\7")
        buf.write("\"\2\2\u0157\u0158\5J&\2\u0158\u0159\7\22\2\2\u0159G\3")
        buf.write("\2\2\2\u015a\u015d\5h\65\2\u015b\u015d\5j\66\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\7\22\2\2\u015fI\3\2\2\2\u0160\u0161\5L\'\2\u0161")
        buf.write("\u0162\78\2\2\u0162\u0163\5L\'\2\u0163\u0172\3\2\2\2\u0164")
        buf.write("\u0165\5L\'\2\u0165\u0166\79\2\2\u0166\u0167\5L\'\2\u0167")
        buf.write("\u0172\3\2\2\2\u0168\u0169\5L\'\2\u0169\u016a\7.\2\2\u016a")
        buf.write("\u016b\5L\'\2\u016b\u0172\3\2\2\2\u016c\u016d\5L\'\2\u016d")
        buf.write("\u016e\7/\2\2\u016e\u016f\5L\'\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u0172\5L\'\2\u0171\u0160\3\2\2\2\u0171\u0164\3\2\2\2")
        buf.write("\u0171\u0168\3\2\2\2\u0171\u016c\3\2\2\2\u0171\u0170\3")
        buf.write("\2\2\2\u0172K\3\2\2\2\u0173\u0174\5N(\2\u0174\u0175\7")
        buf.write("+\2\2\u0175\u0176\5N(\2\u0176\u017d\3\2\2\2\u0177\u0178")
        buf.write("\5N(\2\u0178\u0179\7,\2\2\u0179\u017a\5N(\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u017d\5N(\2\u017c\u0173\3\2\2\2\u017c\u0177")
        buf.write("\3\2\2\2\u017c\u017b\3\2\2\2\u017dM\3\2\2\2\u017e\u017f")
        buf.write("\b(\1\2\u017f\u0180\5P)\2\u0180\u0189\3\2\2\2\u0181\u0182")
        buf.write("\f\5\2\2\u0182\u0183\7-\2\2\u0183\u0188\5P)\2\u0184\u0185")
        buf.write("\f\4\2\2\u0185\u0186\7\60\2\2\u0186\u0188\5P)\2\u0187")
        buf.write("\u0181\3\2\2\2\u0187\u0184\3\2\2\2\u0188\u018b\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018aO\3\2\2")
        buf.write("\2\u018b\u0189\3\2\2\2\u018c\u018d\b)\1\2\u018d\u018e")
        buf.write("\5R*\2\u018e\u0197\3\2\2\2\u018f\u0190\f\5\2\2\u0190\u0191")
        buf.write("\7\61\2\2\u0191\u0196\5R*\2\u0192\u0193\f\4\2\2\u0193")
        buf.write("\u0194\7\62\2\2\u0194\u0196\5R*\2\u0195\u018f\3\2\2\2")
        buf.write("\u0195\u0192\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0197\u0198\3\2\2\2\u0198Q\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019b\b*\1\2\u019b\u019c\5T+\2\u019c\u01ab")
        buf.write("\3\2\2\2\u019d\u019e\f\7\2\2\u019e\u019f\7\64\2\2\u019f")
        buf.write("\u01aa\5T+\2\u01a0\u01a1\f\6\2\2\u01a1\u01a2\7\65\2\2")
        buf.write("\u01a2\u01aa\5T+\2\u01a3\u01a4\f\5\2\2\u01a4\u01a5\7\66")
        buf.write("\2\2\u01a5\u01aa\5T+\2\u01a6\u01a7\f\4\2\2\u01a7\u01a8")
        buf.write("\7\63\2\2\u01a8\u01aa\5T+\2\u01a9\u019d\3\2\2\2\u01a9")
        buf.write("\u01a0\3\2\2\2\u01a9\u01a3\3\2\2\2\u01a9\u01a6\3\2\2\2")
        buf.write("\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01acS\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af")
        buf.write("\b+\1\2\u01af\u01b0\5V,\2\u01b0\u01b6\3\2\2\2\u01b1\u01b2")
        buf.write("\f\4\2\2\u01b2\u01b3\7;\2\2\u01b3\u01b5\5V,\2\u01b4\u01b1")
        buf.write("\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7U\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9")
        buf.write("\u01ba\7:\2\2\u01ba\u01bd\5V,\2\u01bb\u01bd\5X-\2\u01bc")
        buf.write("\u01b9\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bdW\3\2\2\2\u01be")
        buf.write("\u01bf\7\61\2\2\u01bf\u01c4\5X-\2\u01c0\u01c1\7\62\2\2")
        buf.write("\u01c1\u01c4\5X-\2\u01c2\u01c4\5Z.\2\u01c3\u01be\3\2\2")
        buf.write("\2\u01c3\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4Y\3\2")
        buf.write("\2\2\u01c5\u01c6\5\\/\2\u01c6\u01c7\7\17\2\2\u01c7\u01c8")
        buf.write("\5J&\2\u01c8\u01c9\7\20\2\2\u01c9\u01ce\3\2\2\2\u01ca")
        buf.write("\u01ce\5\\/\2\u01cb\u01ce\5r:\2\u01cc\u01ce\7#\2\2\u01cd")
        buf.write("\u01c5\3\2\2\2\u01cd\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01cc\3\2\2\2\u01ce[\3\2\2\2\u01cf\u01d0\b/\1\2")
        buf.write("\u01d0\u01d1\5^\60\2\u01d1\u01da\3\2\2\2\u01d2\u01d3\f")
        buf.write("\4\2\2\u01d3\u01d6\7\24\2\2\u01d4\u01d7\7(\2\2\u01d5\u01d7")
        buf.write("\5l\67\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d9\3\2\2\2\u01d8\u01d2\3\2\2\2\u01d9\u01dc\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db]\3\2\2")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dd\u01e0\5v<\2\u01de\u01e0\5")
        buf.write("`\61\2\u01df\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0_")
        buf.write("\3\2\2\2\u01e1\u01e2\7\13\2\2\u01e2\u01e3\5J&\2\u01e3")
        buf.write("\u01e4\7\f\2\2\u01e4\u01e9\3\2\2\2\u01e5\u01e9\7(\2\2")
        buf.write("\u01e6\u01e9\7$\2\2\u01e7\u01e9\7\'\2\2\u01e8\u01e1\3")
        buf.write("\2\2\2\u01e8\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7")
        buf.write("\3\2\2\2\u01e9a\3\2\2\2\u01ea\u01ef\5d\63\2\u01eb\u01ef")
        buf.write("\5f\64\2\u01ec\u01ef\5h\65\2\u01ed\u01ef\5j\66\2\u01ee")
        buf.write("\u01ea\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ed\3\2\2\2\u01efc\3\2\2\2\u01f0\u01f1\5\\/\2")
        buf.write("\u01f1\u01f2\7\24\2\2\u01f2\u01f3\7(\2\2\u01f3e\3\2\2")
        buf.write("\2\u01f4\u01f5\7(\2\2\u01f5\u01f6\7\24\2\2\u01f6\u01f7")
        buf.write("\7(\2\2\u01f7g\3\2\2\2\u01f8\u01f9\5\\/\2\u01f9\u01fa")
        buf.write("\7\24\2\2\u01fa\u01fb\7(\2\2\u01fb\u01fc\7\13\2\2\u01fc")
        buf.write("\u01fd\5n8\2\u01fd\u01fe\7\f\2\2\u01fei\3\2\2\2\u01ff")
        buf.write("\u0200\7(\2\2\u0200\u0201\7\24\2\2\u0201\u0202\7(\2\2")
        buf.write("\u0202\u0203\7\13\2\2\u0203\u0204\5n8\2\u0204\u0205\7")
        buf.write("\f\2\2\u0205k\3\2\2\2\u0206\u0207\7(\2\2\u0207\u0208\7")
        buf.write("\13\2\2\u0208\u0209\5n8\2\u0209\u020a\7\f\2\2\u020am\3")
        buf.write("\2\2\2\u020b\u020e\5p9\2\u020c\u020e\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020d\u020c\3\2\2\2\u020eo\3\2\2\2\u020f\u0210")
        buf.write("\5J&\2\u0210\u0211\7\23\2\2\u0211\u0212\5p9\2\u0212\u0215")
        buf.write("\3\2\2\2\u0213\u0215\5J&\2\u0214\u020f\3\2\2\2\u0214\u0213")
        buf.write("\3\2\2\2\u0215q\3\2\2\2\u0216\u021c\7*\2\2\u0217\u021c")
        buf.write("\7)\2\2\u0218\u021c\7\t\2\2\u0219\u021c\7\n\2\2\u021a")
        buf.write("\u021c\5x=\2\u021b\u0216\3\2\2\2\u021b\u0217\3\2\2\2\u021b")
        buf.write("\u0218\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021a\3\2\2\2")
        buf.write("\u021cs\3\2\2\2\u021d\u021e\5\\/\2\u021e\u021f\7\17\2")
        buf.write("\2\u021f\u0220\5J&\2\u0220\u0221\7\20\2\2\u0221u\3\2\2")
        buf.write("\2\u0222\u0223\7\37\2\2\u0223\u0224\7(\2\2\u0224\u0225")
        buf.write("\7\13\2\2\u0225\u0226\5n8\2\u0226\u0227\7\f\2\2\u0227")
        buf.write("w\3\2\2\2\u0228\u0229\7\r\2\2\u0229\u022a\5z>\2\u022a")
        buf.write("\u022b\7\16\2\2\u022by\3\2\2\2\u022c\u022d\5|?\2\u022d")
        buf.write("\u022e\7\23\2\2\u022e\u022f\5z>\2\u022f\u0232\3\2\2\2")
        buf.write("\u0230\u0232\5|?\2\u0231\u022c\3\2\2\2\u0231\u0230\3\2")
        buf.write("\2\2\u0232{\3\2\2\2\u0233\u0234\t\3\2\2\u0234}\3\2\2\2")
        buf.write("\u0235\u0236\t\4\2\2\u0236\177\3\2\2\2\u0237\u0238\t\5")
        buf.write("\2\2\u0238\u0081\3\2\2\2\u0239\u023a\t\6\2\2\u023a\u0083")
        buf.write("\3\2\2\2\u023b\u023c\7;\2\2\u023c\u0085\3\2\2\2\u023d")
        buf.write("\u0245\7\4\2\2\u023e\u0245\7\5\2\2\u023f\u0245\7\6\2\2")
        buf.write("\u0240\u0245\7\7\2\2\u0241\u0245\7\b\2\2\u0242\u0245\7")
        buf.write("(\2\2\u0243\u0245\5\u0088E\2\u0244\u023d\3\2\2\2\u0244")
        buf.write("\u023e\3\2\2\2\u0244\u023f\3\2\2\2\u0244\u0240\3\2\2\2")
        buf.write("\u0244\u0241\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0243\3")
        buf.write("\2\2\2\u0245\u0087\3\2\2\2\u0246\u0247\t\7\2\2\u0247\u0248")
        buf.write("\7\17\2\2\u0248\u0249\7*\2\2\u0249\u024a\7\20\2\2\u024a")
        buf.write("\u0089\3\2\2\2\63\u0091\u0097\u009f\u00a5\u00aa\u00ae")
        buf.write("\u00b3\u00bd\u00c2\u00c6\u00cc\u00d2\u00d9\u00e0\u00eb")
        buf.write("\u00f2\u00fb\u00fe\u010e\u0119\u011f\u0123\u0129\u012f")
        buf.write("\u013d\u0145\u015c\u0171\u017c\u0187\u0189\u0195\u0197")
        buf.write("\u01a9\u01ab\u01b6\u01bc\u01c3\u01cd\u01d6\u01da\u01df")
        buf.write("\u01e8\u01ee\u020d\u0214\u021b\u0231\u0244")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'int'", "'float'", "'boolean'", 
                     "'string'", "'void'", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "':='", "';'", "','", 
                     "'.'", "':'", "'class'", "'static'", "'final'", "'break'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'if'", 
                     "'new'", "'then'", "'for'", "'return'", "'nil'", "'this'", 
                     "'to'", "'downto'", "'io'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'!='", "'&&'", "'<='", "'>='", 
                     "'||'", "'+'", "'-'", "'%'", "'*'", "'/'", "'\\'", 
                     "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                      "STRINGTYPE", "VOIDTYPE", "BOOLIT", "STRINGLIT", "LB", 
                      "RB", "LP", "RP", "LSB", "RSB", "ASSIGN", "SEMI", 
                      "COMMA", "DOT", "COLON", "CLASS", "STATIC", "FINAL", 
                      "BREAK", "CONTINUTE", "DO", "ELSE", "EXTENDS", "IF", 
                      "NEW", "THEN", "FOR", "RETURN", "NIL", "THIS", "TO", 
                      "DOWNTO", "IO", "ID", "FLOATLIT", "INTLIT", "EQE", 
                      "NEQ", "AND", "LET", "GET", "OR", "ADD", "SUB", "MOD", 
                      "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", "CONCATE", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_bkool = 1
    RULE_classdecl = 2
    RULE_listmember = 3
    RULE_listmemberprime = 4
    RULE_member = 5
    RULE_attribute = 6
    RULE_mutableatt = 7
    RULE_listattmu = 8
    RULE_attributenamemu = 9
    RULE_immutableatt = 10
    RULE_listatt = 11
    RULE_attributename = 12
    RULE_method = 13
    RULE_listparameter = 14
    RULE_listparameterprime = 15
    RULE_paradecl = 16
    RULE_idlist = 17
    RULE_constructor = 18
    RULE_statement = 19
    RULE_blockstatement = 20
    RULE_listblock = 21
    RULE_blockdecllist = 22
    RULE_blockdeclprime = 23
    RULE_blockbodylist = 24
    RULE_blockbodyprime = 25
    RULE_blockdecl = 26
    RULE_vardecl = 27
    RULE_assignmentstatement = 28
    RULE_lhs = 29
    RULE_ifstatement = 30
    RULE_forstatement = 31
    RULE_breakstatment = 32
    RULE_continuestatement = 33
    RULE_returnstatement = 34
    RULE_methodinvocationstatement = 35
    RULE_expression = 36
    RULE_exp1 = 37
    RULE_exp2 = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_exp7 = 43
    RULE_exp8 = 44
    RULE_exp9 = 45
    RULE_exp10 = 46
    RULE_exp11 = 47
    RULE_memberaccess = 48
    RULE_instanceattributeaccess = 49
    RULE_staticattributeaccess = 50
    RULE_instancemethodinvocation = 51
    RULE_staticmethodinvocation = 52
    RULE_methodinvocation = 53
    RULE_listexpression = 54
    RULE_expressionprime = 55
    RULE_literal = 56
    RULE_indexexpression = 57
    RULE_classcreate = 58
    RULE_arraylit = 59
    RULE_array = 60
    RULE_arrayelement = 61
    RULE_intoperator = 62
    RULE_floatoperator = 63
    RULE_booloperator = 64
    RULE_stringoperator = 65
    RULE_typ = 66
    RULE_arraytyp = 67

    ruleNames =  [ "program", "bkool", "classdecl", "listmember", "listmemberprime", 
                   "member", "attribute", "mutableatt", "listattmu", "attributenamemu", 
                   "immutableatt", "listatt", "attributename", "method", 
                   "listparameter", "listparameterprime", "paradecl", "idlist", 
                   "constructor", "statement", "blockstatement", "listblock", 
                   "blockdecllist", "blockdeclprime", "blockbodylist", "blockbodyprime", 
                   "blockdecl", "vardecl", "assignmentstatement", "lhs", 
                   "ifstatement", "forstatement", "breakstatment", "continuestatement", 
                   "returnstatement", "methodinvocationstatement", "expression", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "memberaccess", "instanceattributeaccess", 
                   "staticattributeaccess", "instancemethodinvocation", 
                   "staticmethodinvocation", "methodinvocation", "listexpression", 
                   "expressionprime", "literal", "indexexpression", "classcreate", 
                   "arraylit", "array", "arrayelement", "intoperator", "floatoperator", 
                   "booloperator", "stringoperator", "typ", "arraytyp" ]

    EOF = Token.EOF
    COMMENT=1
    INTTYPE=2
    FLOATYPE=3
    BOOLEANTYPE=4
    STRINGTYPE=5
    VOIDTYPE=6
    BOOLIT=7
    STRINGLIT=8
    LB=9
    RB=10
    LP=11
    RP=12
    LSB=13
    RSB=14
    ASSIGN=15
    SEMI=16
    COMMA=17
    DOT=18
    COLON=19
    CLASS=20
    STATIC=21
    FINAL=22
    BREAK=23
    CONTINUTE=24
    DO=25
    ELSE=26
    EXTENDS=27
    IF=28
    NEW=29
    THEN=30
    FOR=31
    RETURN=32
    NIL=33
    THIS=34
    TO=35
    DOWNTO=36
    IO=37
    ID=38
    FLOATLIT=39
    INTLIT=40
    EQE=41
    NEQ=42
    AND=43
    LET=44
    GET=45
    OR=46
    ADD=47
    SUB=48
    MOD=49
    MUL=50
    FDIV=51
    IDIV=52
    EQ=53
    LT=54
    GT=55
    NOT=56
    CONCATE=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

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

        def bkool(self):
            return self.getTypedRuleContext(BKOOLParser.BkoolContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.bkool()
            self.state = 137
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BkoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdeclContext,0)


        def bkool(self):
            return self.getTypedRuleContext(BKOOLParser.BkoolContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_bkool




    def bkool(self):

        localctx = BKOOLParser.BkoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bkool)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.classdecl()
                self.state = 140
                self.bkool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def listmember(self):
            return self.getTypedRuleContext(BKOOLParser.ListmemberContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classdecl




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKOOLParser.CLASS)
            self.state = 146
            self.match(BKOOLParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 147
                self.match(BKOOLParser.EXTENDS)
                self.state = 148
                self.match(BKOOLParser.ID)


            self.state = 151
            self.match(BKOOLParser.LP)
            self.state = 152
            self.listmember()
            self.state = 153
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListmemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listmemberprime(self):
            return self.getTypedRuleContext(BKOOLParser.ListmemberprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listmember




    def listmember(self):

        localctx = BKOOLParser.ListmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listmember)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.STATIC, BKOOLParser.FINAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.listmemberprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ListmemberprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def listmemberprime(self):
            return self.getTypedRuleContext(BKOOLParser.ListmemberprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listmemberprime




    def listmemberprime(self):

        localctx = BKOOLParser.ListmemberprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listmemberprime)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.member()
                self.state = 160
                self.listmemberprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(BKOOLParser.MethodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def mutableatt(self):
            return self.getTypedRuleContext(BKOOLParser.MutableattContext,0)


        def immutableatt(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableattContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 170
                self.mutableatt()
                pass

            elif la_ == 2:
                self.state = 171
                self.immutableatt()
                pass


            self.state = 174
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableattContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listattmu(self):
            return self.getTypedRuleContext(BKOOLParser.ListattmuContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableatt




    def mutableatt(self):

        localctx = BKOOLParser.MutableattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutableatt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 176
                self.match(BKOOLParser.STATIC)


            self.state = 179
            self.typ()
            self.state = 180
            self.listattmu()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListattmuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributenamemu(self):
            return self.getTypedRuleContext(BKOOLParser.AttributenamemuContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def listattmu(self):
            return self.getTypedRuleContext(BKOOLParser.ListattmuContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listattmu




    def listattmu(self):

        localctx = BKOOLParser.ListattmuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listattmu)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.attributenamemu()
                self.state = 183
                self.match(BKOOLParser.COMMA)
                self.state = 184
                self.listattmu()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.attributenamemu()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributenamemuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributenamemu




    def attributenamemu(self):

        localctx = BKOOLParser.AttributenamemuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributenamemu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BKOOLParser.ID)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQ:
                self.state = 190
                self.match(BKOOLParser.EQ)
                self.state = 191
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableattContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listatt(self):
            return self.getTypedRuleContext(BKOOLParser.ListattContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutableatt




    def immutableatt(self):

        localctx = BKOOLParser.ImmutableattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_immutableatt)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(BKOOLParser.FINAL)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 195
                    self.match(BKOOLParser.STATIC)


                self.state = 198
                self.typ()
                self.state = 199
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 201
                    self.match(BKOOLParser.STATIC)


                self.state = 204
                self.match(BKOOLParser.FINAL)
                self.state = 205
                self.typ()
                self.state = 206
                self.listatt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListattContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributename(self):
            return self.getTypedRuleContext(BKOOLParser.AttributenameContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def listatt(self):
            return self.getTypedRuleContext(BKOOLParser.ListattContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listatt




    def listatt(self):

        localctx = BKOOLParser.ListattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listatt)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.attributename()
                self.state = 211
                self.match(BKOOLParser.COMMA)
                self.state = 212
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.attributename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributename




    def attributename(self):

        localctx = BKOOLParser.AttributenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attributename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BKOOLParser.ID)
            self.state = 218
            self.match(BKOOLParser.EQ)
            self.state = 219
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listparameter(self):
            return self.getTypedRuleContext(BKOOLParser.ListparameterContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 221
                self.match(BKOOLParser.STATIC)


            self.state = 224
            self.typ()
            self.state = 225
            self.match(BKOOLParser.ID)
            self.state = 226
            self.match(BKOOLParser.LB)
            self.state = 227
            self.listparameter()
            self.state = 228
            self.match(BKOOLParser.RB)
            self.state = 229
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listparameterprime(self):
            return self.getTypedRuleContext(BKOOLParser.ListparameterprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listparameter




    def listparameter(self):

        localctx = BKOOLParser.ListparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listparameter)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.listparameterprime()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ListparameterprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParadeclContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def listparameterprime(self):
            return self.getTypedRuleContext(BKOOLParser.ListparameterprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listparameterprime




    def listparameterprime(self):

        localctx = BKOOLParser.ListparameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listparameterprime)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.paradecl()
                self.state = 236
                self.match(BKOOLParser.SEMI)
                self.state = 237
                self.listparameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.paradecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paradecl




    def paradecl(self):

        localctx = BKOOLParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.typ()
            self.state = 243
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idlist)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(BKOOLParser.ID)
                self.state = 246
                self.match(BKOOLParser.COMMA)
                self.state = 247
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listparameter(self):
            return self.getTypedRuleContext(BKOOLParser.ListparameterContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 251
                self.match(BKOOLParser.STATIC)


            self.state = 254
            self.match(BKOOLParser.ID)
            self.state = 255
            self.match(BKOOLParser.LB)
            self.state = 256
            self.listparameter()
            self.state = 257
            self.match(BKOOLParser.RB)
            self.state = 258
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def assignmentstatement(self):
            return self.getTypedRuleContext(BKOOLParser.AssignmentstatementContext,0)


        def ifstatement(self):
            return self.getTypedRuleContext(BKOOLParser.IfstatementContext,0)


        def forstatement(self):
            return self.getTypedRuleContext(BKOOLParser.ForstatementContext,0)


        def breakstatment(self):
            return self.getTypedRuleContext(BKOOLParser.BreakstatmentContext,0)


        def continuestatement(self):
            return self.getTypedRuleContext(BKOOLParser.ContinuestatementContext,0)


        def returnstatement(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstatementContext,0)


        def methodinvocationstatement(self):
            return self.getTypedRuleContext(BKOOLParser.MethodinvocationstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.blockstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.assignmentstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.ifstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.forstatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.breakstatment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.continuestatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.returnstatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 267
                self.methodinvocationstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def listblock(self):
            return self.getTypedRuleContext(BKOOLParser.ListblockContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstatement




    def blockstatement(self):

        localctx = BKOOLParser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BKOOLParser.LP)
            self.state = 271
            self.listblock()
            self.state = 272
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdecllist(self):
            return self.getTypedRuleContext(BKOOLParser.BlockdecllistContext,0)


        def blockbodylist(self):
            return self.getTypedRuleContext(BKOOLParser.BlockbodylistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listblock




    def listblock(self):

        localctx = BKOOLParser.ListblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_listblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.blockdecllist()
            self.state = 275
            self.blockbodylist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockdecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdeclprime(self):
            return self.getTypedRuleContext(BKOOLParser.BlockdeclprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockdecllist




    def blockdecllist(self):

        localctx = BKOOLParser.BlockdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockdecllist)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.blockdeclprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockdeclprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdecl(self):
            return self.getTypedRuleContext(BKOOLParser.BlockdeclContext,0)


        def blockdeclprime(self):
            return self.getTypedRuleContext(BKOOLParser.BlockdeclprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockdeclprime




    def blockdeclprime(self):

        localctx = BKOOLParser.BlockdeclprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_blockdeclprime)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.blockdecl()
                self.state = 282
                self.blockdeclprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.blockdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockbodylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockbodyprime(self):
            return self.getTypedRuleContext(BKOOLParser.BlockbodyprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockbodylist




    def blockbodylist(self):

        localctx = BKOOLParser.BlockbodylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_blockbodylist)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.BREAK, BKOOLParser.CONTINUTE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.blockbodyprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class BlockbodyprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def blockbodyprime(self):
            return self.getTypedRuleContext(BKOOLParser.BlockbodyprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockbodyprime




    def blockbodyprime(self):

        localctx = BKOOLParser.BlockbodyprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_blockbodyprime)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.statement()
                self.state = 292
                self.blockbodyprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockdecl




    def blockdecl(self):

        localctx = BKOOLParser.BlockdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_blockdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.vardecl()
            self.state = 298
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listatt(self):
            return self.getTypedRuleContext(BKOOLParser.ListattContext,0)


        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 300
                self.match(BKOOLParser.FINAL)


            self.state = 303
            self.typ()
            self.state = 304
            self.listatt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignmentstatement




    def assignmentstatement(self):

        localctx = BKOOLParser.AssignmentstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignmentstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.lhs()
            self.state = 307
            self.match(BKOOLParser.ASSIGN)
            self.state = 308
            self.expression()
            self.state = 309
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexexpression(self):
            return self.getTypedRuleContext(BKOOLParser.IndexexpressionContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def instanceattributeaccess(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceattributeaccessContext,0)


        def staticattributeaccess(self):
            return self.getTypedRuleContext(BKOOLParser.StaticattributeaccessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.indexexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.instanceattributeaccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.staticattributeaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstatement




    def ifstatement(self):

        localctx = BKOOLParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(BKOOLParser.IF)
            self.state = 318
            self.expression()
            self.state = 319
            self.match(BKOOLParser.THEN)
            self.state = 320
            self.statement()
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 321
                self.match(BKOOLParser.ELSE)
                self.state = 322
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpressionContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forstatement




    def forstatement(self):

        localctx = BKOOLParser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKOOLParser.FOR)
            self.state = 326
            self.match(BKOOLParser.ID)
            self.state = 327
            self.match(BKOOLParser.ASSIGN)
            self.state = 328
            self.expression()
            self.state = 329
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 330
            self.expression()
            self.state = 331
            self.match(BKOOLParser.DO)
            self.state = 332
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakstatment




    def breakstatment(self):

        localctx = BKOOLParser.BreakstatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_breakstatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BKOOLParser.BREAK)
            self.state = 335
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUTE(self):
            return self.getToken(BKOOLParser.CONTINUTE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continuestatement




    def continuestatement(self):

        localctx = BKOOLParser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKOOLParser.CONTINUTE)
            self.state = 338
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstatement




    def returnstatement(self):

        localctx = BKOOLParser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_returnstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(BKOOLParser.RETURN)
            self.state = 341
            self.expression()
            self.state = 342
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvocationstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def instancemethodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.InstancemethodinvocationContext,0)


        def staticmethodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.StaticmethodinvocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodinvocationstatement




    def methodinvocationstatement(self):

        localctx = BKOOLParser.MethodinvocationstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_methodinvocationstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 344
                self.instancemethodinvocation()
                pass

            elif la_ == 2:
                self.state = 345
                self.staticmethodinvocation()
                pass


            self.state = 348
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LET(self):
            return self.getToken(BKOOLParser.LET, 0)

        def GET(self):
            return self.getToken(BKOOLParser.GET, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression




    def expression(self):

        localctx = BKOOLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.exp1()
                self.state = 351
                self.match(BKOOLParser.LT)
                self.state = 352
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.exp1()
                self.state = 355
                self.match(BKOOLParser.GT)
                self.state = 356
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.exp1()
                self.state = 359
                self.match(BKOOLParser.LET)
                self.state = 360
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.exp1()
                self.state = 363
                self.match(BKOOLParser.GET)
                self.state = 364
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 366
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def EQE(self):
            return self.getToken(BKOOLParser.EQE, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp1)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.exp2(0)
                self.state = 370
                self.match(BKOOLParser.EQE)
                self.state = 371
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.exp2(0)
                self.state = 374
                self.match(BKOOLParser.NEQ)
                self.state = 375
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 389
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 383
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 384
                        self.match(BKOOLParser.AND)
                        self.state = 385
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 386
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 387
                        self.match(BKOOLParser.OR)
                        self.state = 388
                        self.exp3(0)
                        pass

             
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 403
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 397
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 398
                        self.match(BKOOLParser.ADD)
                        self.state = 399
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 400
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 401
                        self.match(BKOOLParser.SUB)
                        self.state = 402
                        self.exp4(0)
                        pass

             
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 423
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 411
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 412
                        self.match(BKOOLParser.MUL)
                        self.state = 413
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 414
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 415
                        self.match(BKOOLParser.FDIV)
                        self.state = 416
                        self.exp5(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 417
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 418
                        self.match(BKOOLParser.IDIV)
                        self.state = 419
                        self.exp5(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 420
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 421
                        self.match(BKOOLParser.MOD)
                        self.state = 422
                        self.exp5(0)
                        pass

             
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCATE(self):
            return self.getToken(BKOOLParser.CONCATE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    self.match(BKOOLParser.CONCATE)
                    self.state = 433
                    self.exp6() 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp6)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(BKOOLParser.NOT)
                self.state = 440
                self.exp6()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp7)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(BKOOLParser.ADD)
                self.state = 445
                self.exp7()
                pass
            elif token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(BKOOLParser.SUB)
                self.state = 447
                self.exp7()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.exp8()
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


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp8)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.exp9(0)
                self.state = 452
                self.match(BKOOLParser.LSB)
                self.state = 453
                self.expression()
                self.state = 454
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.exp9(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(BKOOLParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def methodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.MethodinvocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 465
                    self.match(BKOOLParser.DOT)
                    self.state = 468
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 467
                        self.methodinvocation()
                        pass

             
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classcreate(self):
            return self.getTypedRuleContext(BKOOLParser.ClasscreateContext,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp10)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.classcreate()
                pass
            elif token in [BKOOLParser.LB, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.exp11()
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


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def IO(self):
            return self.getToken(BKOOLParser.IO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exp11)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(BKOOLParser.LB)
                self.state = 480
                self.expression()
                self.state = 481
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.IO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.match(BKOOLParser.IO)
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


    class MemberaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceattributeaccess(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceattributeaccessContext,0)


        def staticattributeaccess(self):
            return self.getTypedRuleContext(BKOOLParser.StaticattributeaccessContext,0)


        def instancemethodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.InstancemethodinvocationContext,0)


        def staticmethodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.StaticmethodinvocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberaccess




    def memberaccess(self):

        localctx = BKOOLParser.MemberaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_memberaccess)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.instanceattributeaccess()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.staticattributeaccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.instancemethodinvocation()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 491
                self.staticmethodinvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceattributeaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instanceattributeaccess




    def instanceattributeaccess(self):

        localctx = BKOOLParser.InstanceattributeaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instanceattributeaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.exp9(0)
            self.state = 495
            self.match(BKOOLParser.DOT)
            self.state = 496
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticattributeaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_staticattributeaccess




    def staticattributeaccess(self):

        localctx = BKOOLParser.StaticattributeaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_staticattributeaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BKOOLParser.ID)
            self.state = 499
            self.match(BKOOLParser.DOT)
            self.state = 500
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstancemethodinvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listexpression(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instancemethodinvocation




    def instancemethodinvocation(self):

        localctx = BKOOLParser.InstancemethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_instancemethodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.exp9(0)
            self.state = 503
            self.match(BKOOLParser.DOT)
            self.state = 504
            self.match(BKOOLParser.ID)
            self.state = 505
            self.match(BKOOLParser.LB)
            self.state = 506
            self.listexpression()
            self.state = 507
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticmethodinvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listexpression(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_staticmethodinvocation




    def staticmethodinvocation(self):

        localctx = BKOOLParser.StaticmethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_staticmethodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(BKOOLParser.ID)
            self.state = 510
            self.match(BKOOLParser.DOT)
            self.state = 511
            self.match(BKOOLParser.ID)
            self.state = 512
            self.match(BKOOLParser.LB)
            self.state = 513
            self.listexpression()
            self.state = 514
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listexpression(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodinvocation




    def methodinvocation(self):

        localctx = BKOOLParser.MethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_methodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(BKOOLParser.ID)
            self.state = 517
            self.match(BKOOLParser.LB)
            self.state = 518
            self.listexpression()
            self.state = 519
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listexpression




    def listexpression(self):

        localctx = BKOOLParser.ListexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_listexpression)
        try:
            self.state = 523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.expressionprime()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ExpressionprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expressionprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expressionprime




    def expressionprime(self):

        localctx = BKOOLParser.ExpressionprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expressionprime)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.expression()
                self.state = 526
                self.match(BKOOLParser.COMMA)
                self.state = 527
                self.expressionprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(BKOOLParser.ArraylitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_literal)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 534
                self.match(BKOOLParser.BOOLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 535
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 536
                self.arraylit()
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


    class IndexexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexexpression




    def indexexpression(self):

        localctx = BKOOLParser.IndexexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.exp9(0)
            self.state = 540
            self.match(BKOOLParser.LSB)
            self.state = 541
            self.expression()
            self.state = 542
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasscreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listexpression(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classcreate




    def classcreate(self):

        localctx = BKOOLParser.ClasscreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_classcreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(BKOOLParser.NEW)
            self.state = 545
            self.match(BKOOLParser.ID)
            self.state = 546
            self.match(BKOOLParser.LB)
            self.state = 547
            self.listexpression()
            self.state = 548
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
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
            return BKOOLParser.RULE_arraylit




    def arraylit(self):

        localctx = BKOOLParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(BKOOLParser.LP)
            self.state = 551
            self.array()
            self.state = 552
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




    def array(self):

        localctx = BKOOLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.arrayelement()
                self.state = 555
                self.match(BKOOLParser.COMMA)
                self.state = 556
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
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

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayelement




    def arrayelement(self):

        localctx = BKOOLParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_arrayelement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT))) != 0)):
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


    class IntoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def LET(self):
            return self.getToken(BKOOLParser.LET, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def GET(self):
            return self.getToken(BKOOLParser.GET, 0)

        def EQE(self):
            return self.getToken(BKOOLParser.EQE, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_intoperator




    def intoperator(self):

        localctx = BKOOLParser.IntoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_intoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.EQE) | (1 << BKOOLParser.NEQ) | (1 << BKOOLParser.LET) | (1 << BKOOLParser.GET) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.MOD) | (1 << BKOOLParser.MUL) | (1 << BKOOLParser.FDIV) | (1 << BKOOLParser.IDIV) | (1 << BKOOLParser.EQ) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.GT))) != 0)):
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


    class FloatoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def LET(self):
            return self.getToken(BKOOLParser.LET, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def GET(self):
            return self.getToken(BKOOLParser.GET, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_floatoperator




    def floatoperator(self):

        localctx = BKOOLParser.FloatoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_floatoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LET) | (1 << BKOOLParser.GET) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.MUL) | (1 << BKOOLParser.FDIV) | (1 << BKOOLParser.EQ) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.GT))) != 0)):
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


    class BooloperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQE(self):
            return self.getToken(BKOOLParser.EQE, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booloperator




    def booloperator(self):

        localctx = BKOOLParser.BooloperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_booloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.EQE) | (1 << BKOOLParser.NEQ) | (1 << BKOOLParser.AND) | (1 << BKOOLParser.OR) | (1 << BKOOLParser.NOT))) != 0)):
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


    class StringoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCATE(self):
            return self.getToken(BKOOLParser.CONCATE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_stringoperator




    def stringoperator(self):

        localctx = BKOOLParser.StringoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_stringoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(BKOOLParser.CONCATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATYPE(self):
            return self.getToken(BKOOLParser.FLOATYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(BKOOLParser.BOOLEANTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(BKOOLParser.STRINGTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arraytyp(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_typ)
        try:
            self.state = 578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.match(BKOOLParser.INTTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.match(BKOOLParser.FLOATYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 573
                self.match(BKOOLParser.BOOLEANTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 574
                self.match(BKOOLParser.STRINGTYPE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 575
                self.match(BKOOLParser.VOIDTYPE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 576
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 577
                self.arraytyp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATYPE(self):
            return self.getToken(BKOOLParser.FLOATYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(BKOOLParser.BOOLEANTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(BKOOLParser.STRINGTYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytyp




    def arraytyp(self):

        localctx = BKOOLParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_arraytyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.FLOATYPE) | (1 << BKOOLParser.BOOLEANTYPE) | (1 << BKOOLParser.STRINGTYPE) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 581
            self.match(BKOOLParser.LSB)
            self.state = 582
            self.match(BKOOLParser.INTLIT)
            self.state = 583
            self.match(BKOOLParser.RSB)
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
        self._predicates[38] = self.exp2_sempred
        self._predicates[39] = self.exp3_sempred
        self._predicates[40] = self.exp4_sempred
        self._predicates[41] = self.exp5_sempred
        self._predicates[45] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




