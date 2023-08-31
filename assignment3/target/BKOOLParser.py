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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0234\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\3\4\3\4\5\4\u0090\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u009e\n\6\3\7\3\7\3\7\5\7\u00a3\n\7\3\b\3\b\5\b")
        buf.write("\u00a7\n\b\3\b\3\b\3\t\5\t\u00ac\n\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00b6\n\n\3\13\3\13\3\13\5\13\u00bb")
        buf.write("\n\13\3\f\3\f\5\f\u00bf\n\f\3\f\3\f\3\f\3\f\5\f\u00c5")
        buf.write("\n\f\3\f\3\f\3\f\3\f\5\f\u00cb\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00d2\n\r\3\16\3\16\3\16\3\16\3\17\5\17\u00d9\n\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00e4")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00eb\n\21\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\5\23\u00f4\n\23\3\24\5\24")
        buf.write("\u00f7\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\5\25\u0107\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u0112\n\30\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0118\n\31\3\32\3\32\5\32\u011c")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u0122\n\33\3\34\3\34\5")
        buf.write("\34\u0126\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u013a\n")
        buf.write(" \3!\3!\3!\3!\3!\3!\5!\u0142\n!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\5&")
        buf.write("\u0159\n&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0183\n,\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u018e\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u0199")
        buf.write("\n.\f.\16.\u019c\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u01a7")
        buf.write("\n/\f/\16/\u01aa\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01bb\n")
        buf.write("\60\f\60\16\60\u01be\13\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\7\61\u01c6\n\61\f\61\16\61\u01c9\13\61\3\62\3\62\3")
        buf.write("\62\5\62\u01ce\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01d5")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01dd\n\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01e6\n\65\7\65")
        buf.write("\u01e8\n\65\f\65\16\65\u01eb\13\65\3\66\3\66\5\66\u01ef")
        buf.write("\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01fa\n\67\38\38\58\u01fe\n8\39\39\39\39\39\59\u0205")
        buf.write("\n9\3:\3:\3:\3:\3:\5:\u020c\n:\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0222\n>\3?\3")
        buf.write("?\3@\3@\3@\3@\3@\3@\3@\5@\u022d\n@\3A\3A\3A\3A\3A\3A\2")
        buf.write("\7Z\\^`hB\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~")
        buf.write("\u0080\2\5\3\2%&\4\2\t\n)*\4\2\4\7((\2\u023f\2\u0082\3")
        buf.write("\2\2\2\4\u0089\3\2\2\2\6\u008b\3\2\2\2\b\u0097\3\2\2\2")
        buf.write("\n\u009d\3\2\2\2\f\u00a2\3\2\2\2\16\u00a6\3\2\2\2\20\u00ab")
        buf.write("\3\2\2\2\22\u00b5\3\2\2\2\24\u00b7\3\2\2\2\26\u00ca\3")
        buf.write("\2\2\2\30\u00d1\3\2\2\2\32\u00d3\3\2\2\2\34\u00d8\3\2")
        buf.write("\2\2\36\u00e3\3\2\2\2 \u00ea\3\2\2\2\"\u00ec\3\2\2\2$")
        buf.write("\u00f3\3\2\2\2&\u00f6\3\2\2\2(\u0106\3\2\2\2*\u0108\3")
        buf.write("\2\2\2,\u010c\3\2\2\2.\u0111\3\2\2\2\60\u0117\3\2\2\2")
        buf.write("\62\u011b\3\2\2\2\64\u0121\3\2\2\2\66\u0125\3\2\2\28\u0129")
        buf.write("\3\2\2\2:\u012d\3\2\2\2<\u0130\3\2\2\2>\u0139\3\2\2\2")
        buf.write("@\u013b\3\2\2\2B\u0143\3\2\2\2D\u014c\3\2\2\2F\u014f\3")
        buf.write("\2\2\2H\u0152\3\2\2\2J\u0158\3\2\2\2L\u015c\3\2\2\2N\u0160")
        buf.write("\3\2\2\2P\u0164\3\2\2\2R\u0168\3\2\2\2T\u016c\3\2\2\2")
        buf.write("V\u0182\3\2\2\2X\u018d\3\2\2\2Z\u018f\3\2\2\2\\\u019d")
        buf.write("\3\2\2\2^\u01ab\3\2\2\2`\u01bf\3\2\2\2b\u01cd\3\2\2\2")
        buf.write("d\u01d4\3\2\2\2f\u01dc\3\2\2\2h\u01de\3\2\2\2j\u01ee\3")
        buf.write("\2\2\2l\u01f9\3\2\2\2n\u01fd\3\2\2\2p\u0204\3\2\2\2r\u020b")
        buf.write("\3\2\2\2t\u020d\3\2\2\2v\u0212\3\2\2\2x\u0218\3\2\2\2")
        buf.write("z\u0221\3\2\2\2|\u0223\3\2\2\2~\u022c\3\2\2\2\u0080\u022e")
        buf.write("\3\2\2\2\u0082\u0083\5\4\3\2\u0083\u0084\7\2\2\3\u0084")
        buf.write("\3\3\2\2\2\u0085\u0086\5\6\4\2\u0086\u0087\5\4\3\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u008a\5\6\4\2\u0089\u0085\3\2\2\2")
        buf.write("\u0089\u0088\3\2\2\2\u008a\5\3\2\2\2\u008b\u008c\7\26")
        buf.write("\2\2\u008c\u008f\7(\2\2\u008d\u008e\7\35\2\2\u008e\u0090")
        buf.write("\7(\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\7\r\2\2\u0092\u0093\5\b\5\2")
        buf.write("\u0093\u0094\7\16\2\2\u0094\7\3\2\2\2\u0095\u0098\5\n")
        buf.write("\6\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\t\3\2\2\2\u0099\u009a\5\f\7\2\u009a\u009b")
        buf.write("\5\n\6\2\u009b\u009e\3\2\2\2\u009c\u009e\5\f\7\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009c\3\2\2\2\u009e\13\3\2\2\2\u009f")
        buf.write("\u00a3\5\16\b\2\u00a0\u00a3\5\34\17\2\u00a1\u00a3\5&\24")
        buf.write("\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\r\3\2\2\2\u00a4\u00a7\5\20\t\2\u00a5\u00a7")
        buf.write("\5\26\f\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\7\22\2\2\u00a9\17\3\2\2\2\u00aa")
        buf.write("\u00ac\7\27\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2")
        buf.write("\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\5~@\2\u00ae\u00af\5")
        buf.write("\22\n\2\u00af\21\3\2\2\2\u00b0\u00b1\5\24\13\2\u00b1\u00b2")
        buf.write("\7\23\2\2\u00b2\u00b3\5\22\n\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b6\5\24\13\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2")
        buf.write("\2\u00b6\23\3\2\2\2\u00b7\u00ba\7(\2\2\u00b8\u00b9\7\67")
        buf.write("\2\2\u00b9\u00bb\5V,\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\25\3\2\2\2\u00bc\u00be\7\30\2\2\u00bd\u00bf")
        buf.write("\7\27\2\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c1\5~@\2\u00c1\u00c2\5\30\r\2")
        buf.write("\u00c2\u00cb\3\2\2\2\u00c3\u00c5\7\27\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\7\30\2\2\u00c7\u00c8\5~@\2\u00c8\u00c9\5\30\r\2")
        buf.write("\u00c9\u00cb\3\2\2\2\u00ca\u00bc\3\2\2\2\u00ca\u00c4\3")
        buf.write("\2\2\2\u00cb\27\3\2\2\2\u00cc\u00cd\5\32\16\2\u00cd\u00ce")
        buf.write("\7\23\2\2\u00ce\u00cf\5\30\r\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write("\u00d2\5\32\16\2\u00d1\u00cc\3\2\2\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d2\31\3\2\2\2\u00d3\u00d4\7(\2\2\u00d4\u00d5\7\67")
        buf.write("\2\2\u00d5\u00d6\5V,\2\u00d6\33\3\2\2\2\u00d7\u00d9\7")
        buf.write("\27\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00db\5~@\2\u00db\u00dc\7(\2\2\u00dc")
        buf.write("\u00dd\7\13\2\2\u00dd\u00de\5\36\20\2\u00de\u00df\7\f")
        buf.write("\2\2\u00df\u00e0\5*\26\2\u00e0\35\3\2\2\2\u00e1\u00e4")
        buf.write("\5 \21\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\37\3\2\2\2\u00e5\u00e6\5\"\22\2\u00e6")
        buf.write("\u00e7\7\22\2\2\u00e7\u00e8\5 \21\2\u00e8\u00eb\3\2\2")
        buf.write("\2\u00e9\u00eb\5\"\22\2\u00ea\u00e5\3\2\2\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb!\3\2\2\2\u00ec\u00ed\5~@\2\u00ed\u00ee")
        buf.write("\5$\23\2\u00ee#\3\2\2\2\u00ef\u00f0\7(\2\2\u00f0\u00f1")
        buf.write("\7\23\2\2\u00f1\u00f4\5$\23\2\u00f2\u00f4\7(\2\2\u00f3")
        buf.write("\u00ef\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4%\3\2\2\2\u00f5")
        buf.write("\u00f7\7\27\2\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2")
        buf.write("\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7(\2\2\u00f9\u00fa")
        buf.write("\7\13\2\2\u00fa\u00fb\5\36\20\2\u00fb\u00fc\7\f\2\2\u00fc")
        buf.write("\u00fd\5*\26\2\u00fd\'\3\2\2\2\u00fe\u0107\5*\26\2\u00ff")
        buf.write("\u0107\5<\37\2\u0100\u0107\5@!\2\u0101\u0107\5B\"\2\u0102")
        buf.write("\u0107\5D#\2\u0103\u0107\5F$\2\u0104\u0107\5H%\2\u0105")
        buf.write("\u0107\5J&\2\u0106\u00fe\3\2\2\2\u0106\u00ff\3\2\2\2\u0106")
        buf.write("\u0100\3\2\2\2\u0106\u0101\3\2\2\2\u0106\u0102\3\2\2\2")
        buf.write("\u0106\u0103\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0105\3")
        buf.write("\2\2\2\u0107)\3\2\2\2\u0108\u0109\7\r\2\2\u0109\u010a")
        buf.write("\5,\27\2\u010a\u010b\7\16\2\2\u010b+\3\2\2\2\u010c\u010d")
        buf.write("\5.\30\2\u010d\u010e\5\62\32\2\u010e-\3\2\2\2\u010f\u0112")
        buf.write("\5\60\31\2\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0110\3\2\2\2\u0112/\3\2\2\2\u0113\u0114\5\66\34\2\u0114")
        buf.write("\u0115\5\60\31\2\u0115\u0118\3\2\2\2\u0116\u0118\5\66")
        buf.write("\34\2\u0117\u0113\3\2\2\2\u0117\u0116\3\2\2\2\u0118\61")
        buf.write("\3\2\2\2\u0119\u011c\5\64\33\2\u011a\u011c\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c\63\3\2\2\2\u011d")
        buf.write("\u011e\5(\25\2\u011e\u011f\5\64\33\2\u011f\u0122\3\2\2")
        buf.write("\2\u0120\u0122\5(\25\2\u0121\u011d\3\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\65\3\2\2\2\u0123\u0126\58\35\2\u0124\u0126")
        buf.write("\5:\36\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0128\7\22\2\2\u0128\67\3\2\2\2\u0129")
        buf.write("\u012a\7\30\2\2\u012a\u012b\5~@\2\u012b\u012c\5\30\r\2")
        buf.write("\u012c9\3\2\2\2\u012d\u012e\5~@\2\u012e\u012f\5\22\n\2")
        buf.write("\u012f;\3\2\2\2\u0130\u0131\5> \2\u0131\u0132\7\21\2\2")
        buf.write("\u0132\u0133\5V,\2\u0133\u0134\7\22\2\2\u0134=\3\2\2\2")
        buf.write("\u0135\u013a\5t;\2\u0136\u013a\7(\2\2\u0137\u013a\5L\'")
        buf.write("\2\u0138\u013a\5N(\2\u0139\u0135\3\2\2\2\u0139\u0136\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a?")
        buf.write("\3\2\2\2\u013b\u013c\7\36\2\2\u013c\u013d\5V,\2\u013d")
        buf.write("\u013e\7 \2\2\u013e\u0141\5(\25\2\u013f\u0140\7\34\2\2")
        buf.write("\u0140\u0142\5(\25\2\u0141\u013f\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142A\3\2\2\2\u0143\u0144\7!\2\2\u0144\u0145\7")
        buf.write("(\2\2\u0145\u0146\7\21\2\2\u0146\u0147\5V,\2\u0147\u0148")
        buf.write("\t\2\2\2\u0148\u0149\5V,\2\u0149\u014a\7\33\2\2\u014a")
        buf.write("\u014b\5(\25\2\u014bC\3\2\2\2\u014c\u014d\7\31\2\2\u014d")
        buf.write("\u014e\7\22\2\2\u014eE\3\2\2\2\u014f\u0150\7\32\2\2\u0150")
        buf.write("\u0151\7\22\2\2\u0151G\3\2\2\2\u0152\u0153\7\"\2\2\u0153")
        buf.write("\u0154\5V,\2\u0154\u0155\7\22\2\2\u0155I\3\2\2\2\u0156")
        buf.write("\u0159\5P)\2\u0157\u0159\5R*\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\7\22\2")
        buf.write("\2\u015bK\3\2\2\2\u015c\u015d\5V,\2\u015d\u015e\7\24\2")
        buf.write("\2\u015e\u015f\7(\2\2\u015fM\3\2\2\2\u0160\u0161\7(\2")
        buf.write("\2\u0161\u0162\7\24\2\2\u0162\u0163\7(\2\2\u0163O\3\2")
        buf.write("\2\2\u0164\u0165\5V,\2\u0165\u0166\7\24\2\2\u0166\u0167")
        buf.write("\5T+\2\u0167Q\3\2\2\2\u0168\u0169\7(\2\2\u0169\u016a\7")
        buf.write("\24\2\2\u016a\u016b\5T+\2\u016bS\3\2\2\2\u016c\u016d\7")
        buf.write("(\2\2\u016d\u016e\7\13\2\2\u016e\u016f\5n8\2\u016f\u0170")
        buf.write("\7\f\2\2\u0170U\3\2\2\2\u0171\u0172\5X-\2\u0172\u0173")
        buf.write("\78\2\2\u0173\u0174\5X-\2\u0174\u0183\3\2\2\2\u0175\u0176")
        buf.write("\5X-\2\u0176\u0177\79\2\2\u0177\u0178\5X-\2\u0178\u0183")
        buf.write("\3\2\2\2\u0179\u017a\5X-\2\u017a\u017b\7.\2\2\u017b\u017c")
        buf.write("\5X-\2\u017c\u0183\3\2\2\2\u017d\u017e\5X-\2\u017e\u017f")
        buf.write("\7/\2\2\u017f\u0180\5X-\2\u0180\u0183\3\2\2\2\u0181\u0183")
        buf.write("\5X-\2\u0182\u0171\3\2\2\2\u0182\u0175\3\2\2\2\u0182\u0179")
        buf.write("\3\2\2\2\u0182\u017d\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("W\3\2\2\2\u0184\u0185\5Z.\2\u0185\u0186\7+\2\2\u0186\u0187")
        buf.write("\5Z.\2\u0187\u018e\3\2\2\2\u0188\u0189\5Z.\2\u0189\u018a")
        buf.write("\7,\2\2\u018a\u018b\5Z.\2\u018b\u018e\3\2\2\2\u018c\u018e")
        buf.write("\5Z.\2\u018d\u0184\3\2\2\2\u018d\u0188\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018eY\3\2\2\2\u018f\u0190\b.\1\2\u0190\u0191")
        buf.write("\5\\/\2\u0191\u019a\3\2\2\2\u0192\u0193\f\5\2\2\u0193")
        buf.write("\u0194\7-\2\2\u0194\u0199\5\\/\2\u0195\u0196\f\4\2\2\u0196")
        buf.write("\u0197\7\60\2\2\u0197\u0199\5\\/\2\u0198\u0192\3\2\2\2")
        buf.write("\u0198\u0195\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b[\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019d\u019e\b/\1\2\u019e\u019f\5^\60\2\u019f")
        buf.write("\u01a8\3\2\2\2\u01a0\u01a1\f\5\2\2\u01a1\u01a2\7\61\2")
        buf.write("\2\u01a2\u01a7\5^\60\2\u01a3\u01a4\f\4\2\2\u01a4\u01a5")
        buf.write("\7\62\2\2\u01a5\u01a7\5^\60\2\u01a6\u01a0\3\2\2\2\u01a6")
        buf.write("\u01a3\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9]\3\2\2\2\u01aa\u01a8\3\2\2")
        buf.write("\2\u01ab\u01ac\b\60\1\2\u01ac\u01ad\5`\61\2\u01ad\u01bc")
        buf.write("\3\2\2\2\u01ae\u01af\f\7\2\2\u01af\u01b0\7\64\2\2\u01b0")
        buf.write("\u01bb\5`\61\2\u01b1\u01b2\f\6\2\2\u01b2\u01b3\7\65\2")
        buf.write("\2\u01b3\u01bb\5`\61\2\u01b4\u01b5\f\5\2\2\u01b5\u01b6")
        buf.write("\7\66\2\2\u01b6\u01bb\5`\61\2\u01b7\u01b8\f\4\2\2\u01b8")
        buf.write("\u01b9\7\63\2\2\u01b9\u01bb\5`\61\2\u01ba\u01ae\3\2\2")
        buf.write("\2\u01ba\u01b1\3\2\2\2\u01ba\u01b4\3\2\2\2\u01ba\u01b7")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd_\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c0\b\61\1\2\u01c0\u01c1\5b\62\2\u01c1\u01c7\3\2\2")
        buf.write("\2\u01c2\u01c3\f\4\2\2\u01c3\u01c4\7;\2\2\u01c4\u01c6")
        buf.write("\5b\62\2\u01c5\u01c2\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8a\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01ca\u01cb\7:\2\2\u01cb\u01ce\5b\62\2")
        buf.write("\u01cc\u01ce\5d\63\2\u01cd\u01ca\3\2\2\2\u01cd\u01cc\3")
        buf.write("\2\2\2\u01cec\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d5")
        buf.write("\5d\63\2\u01d1\u01d2\7\62\2\2\u01d2\u01d5\5d\63\2\u01d3")
        buf.write("\u01d5\5f\64\2\u01d4\u01cf\3\2\2\2\u01d4\u01d1\3\2\2\2")
        buf.write("\u01d4\u01d3\3\2\2\2\u01d5e\3\2\2\2\u01d6\u01d7\5h\65")
        buf.write("\2\u01d7\u01d8\7\17\2\2\u01d8\u01d9\5V,\2\u01d9\u01da")
        buf.write("\7\20\2\2\u01da\u01dd\3\2\2\2\u01db\u01dd\5h\65\2\u01dc")
        buf.write("\u01d6\3\2\2\2\u01dc\u01db\3\2\2\2\u01ddg\3\2\2\2\u01de")
        buf.write("\u01df\b\65\1\2\u01df\u01e0\5j\66\2\u01e0\u01e9\3\2\2")
        buf.write("\2\u01e1\u01e2\f\4\2\2\u01e2\u01e5\7\24\2\2\u01e3\u01e6")
        buf.write("\7(\2\2\u01e4\u01e6\5T+\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e1\3\2\2\2\u01e8")
        buf.write("\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01eai\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ef\5v<\2")
        buf.write("\u01ed\u01ef\5l\67\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3")
        buf.write("\2\2\2\u01efk\3\2\2\2\u01f0\u01f1\7\13\2\2\u01f1\u01f2")
        buf.write("\5V,\2\u01f2\u01f3\7\f\2\2\u01f3\u01fa\3\2\2\2\u01f4\u01fa")
        buf.write("\7(\2\2\u01f5\u01fa\7$\2\2\u01f6\u01fa\7\'\2\2\u01f7\u01fa")
        buf.write("\5r:\2\u01f8\u01fa\7#\2\2\u01f9\u01f0\3\2\2\2\u01f9\u01f4")
        buf.write("\3\2\2\2\u01f9\u01f5\3\2\2\2\u01f9\u01f6\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fam\3\2\2\2\u01fb")
        buf.write("\u01fe\5p9\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01feo\3\2\2\2\u01ff\u0200\5V,\2\u0200")
        buf.write("\u0201\7\23\2\2\u0201\u0202\5p9\2\u0202\u0205\3\2\2\2")
        buf.write("\u0203\u0205\5V,\2\u0204\u01ff\3\2\2\2\u0204\u0203\3\2")
        buf.write("\2\2\u0205q\3\2\2\2\u0206\u020c\7*\2\2\u0207\u020c\7)")
        buf.write("\2\2\u0208\u020c\7\t\2\2\u0209\u020c\7\n\2\2\u020a\u020c")
        buf.write("\5x=\2\u020b\u0206\3\2\2\2\u020b\u0207\3\2\2\2\u020b\u0208")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("s\3\2\2\2\u020d\u020e\5h\65\2\u020e\u020f\7\17\2\2\u020f")
        buf.write("\u0210\5V,\2\u0210\u0211\7\20\2\2\u0211u\3\2\2\2\u0212")
        buf.write("\u0213\7\37\2\2\u0213\u0214\7(\2\2\u0214\u0215\7\13\2")
        buf.write("\2\u0215\u0216\5n8\2\u0216\u0217\7\f\2\2\u0217w\3\2\2")
        buf.write("\2\u0218\u0219\7\r\2\2\u0219\u021a\5z>\2\u021a\u021b\7")
        buf.write("\16\2\2\u021by\3\2\2\2\u021c\u021d\5|?\2\u021d\u021e\7")
        buf.write("\23\2\2\u021e\u021f\5z>\2\u021f\u0222\3\2\2\2\u0220\u0222")
        buf.write("\5|?\2\u0221\u021c\3\2\2\2\u0221\u0220\3\2\2\2\u0222{")
        buf.write("\3\2\2\2\u0223\u0224\t\3\2\2\u0224}\3\2\2\2\u0225\u022d")
        buf.write("\7\4\2\2\u0226\u022d\7\5\2\2\u0227\u022d\7\6\2\2\u0228")
        buf.write("\u022d\7\7\2\2\u0229\u022d\7\b\2\2\u022a\u022d\7(\2\2")
        buf.write("\u022b\u022d\5\u0080A\2\u022c\u0225\3\2\2\2\u022c\u0226")
        buf.write("\3\2\2\2\u022c\u0227\3\2\2\2\u022c\u0228\3\2\2\2\u022c")
        buf.write("\u0229\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2")
        buf.write("\u022d\177\3\2\2\2\u022e\u022f\t\4\2\2\u022f\u0230\7\17")
        buf.write("\2\2\u0230\u0231\7*\2\2\u0231\u0232\7\20\2\2\u0232\u0081")
        buf.write("\3\2\2\2\62\u0089\u008f\u0097\u009d\u00a2\u00a6\u00ab")
        buf.write("\u00b5\u00ba\u00be\u00c4\u00ca\u00d1\u00d8\u00e3\u00ea")
        buf.write("\u00f3\u00f6\u0106\u0111\u0117\u011b\u0121\u0125\u0139")
        buf.write("\u0141\u0158\u0182\u018d\u0198\u019a\u01a6\u01a8\u01ba")
        buf.write("\u01bc\u01c7\u01cd\u01d4\u01dc\u01e5\u01e9\u01ee\u01f9")
        buf.write("\u01fd\u0204\u020b\u0221\u022c")
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
    RULE_vardeclmu = 28
    RULE_assignmentstatement = 29
    RULE_lhs = 30
    RULE_ifstatement = 31
    RULE_forstatement = 32
    RULE_breakstatment = 33
    RULE_continuestatement = 34
    RULE_returnstatement = 35
    RULE_methodinvocationstatement = 36
    RULE_instanceattributeaccess = 37
    RULE_staticattributeaccess = 38
    RULE_instancemethodinvocation = 39
    RULE_staticmethodinvocation = 40
    RULE_methodinvocation = 41
    RULE_expression = 42
    RULE_exp1 = 43
    RULE_exp2 = 44
    RULE_exp3 = 45
    RULE_exp4 = 46
    RULE_exp5 = 47
    RULE_exp6 = 48
    RULE_exp7 = 49
    RULE_exp8 = 50
    RULE_exp9 = 51
    RULE_exp10 = 52
    RULE_exp11 = 53
    RULE_listexpression = 54
    RULE_expressionprime = 55
    RULE_literal = 56
    RULE_indexexpression = 57
    RULE_classcreate = 58
    RULE_arraylit = 59
    RULE_array = 60
    RULE_arrayelement = 61
    RULE_typ = 62
    RULE_arraytyp = 63

    ruleNames =  [ "program", "bkool", "classdecl", "listmember", "listmemberprime", 
                   "member", "attribute", "mutableatt", "listattmu", "attributenamemu", 
                   "immutableatt", "listatt", "attributename", "method", 
                   "listparameter", "listparameterprime", "paradecl", "idlist", 
                   "constructor", "statement", "blockstatement", "listblock", 
                   "blockdecllist", "blockdeclprime", "blockbodylist", "blockbodyprime", 
                   "blockdecl", "vardecl", "vardeclmu", "assignmentstatement", 
                   "lhs", "ifstatement", "forstatement", "breakstatment", 
                   "continuestatement", "returnstatement", "methodinvocationstatement", 
                   "instanceattributeaccess", "staticattributeaccess", "instancemethodinvocation", 
                   "staticmethodinvocation", "methodinvocation", "expression", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "listexpression", "expressionprime", 
                   "literal", "indexexpression", "classcreate", "arraylit", 
                   "array", "arrayelement", "typ", "arraytyp" ]

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
            self.state = 128
            self.bkool()
            self.state = 129
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBkool" ):
                return visitor.visitBkool(self)
            else:
                return visitor.visitChildren(self)




    def bkool(self):

        localctx = BKOOLParser.BkoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bkool)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.classdecl()
                self.state = 132
                self.bkool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKOOLParser.CLASS)
            self.state = 138
            self.match(BKOOLParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 139
                self.match(BKOOLParser.EXTENDS)
                self.state = 140
                self.match(BKOOLParser.ID)


            self.state = 143
            self.match(BKOOLParser.LP)
            self.state = 144
            self.listmember()
            self.state = 145
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListmember" ):
                return visitor.visitListmember(self)
            else:
                return visitor.visitChildren(self)




    def listmember(self):

        localctx = BKOOLParser.ListmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listmember)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.STATIC, BKOOLParser.FINAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListmemberprime" ):
                return visitor.visitListmemberprime(self)
            else:
                return visitor.visitChildren(self)




    def listmemberprime(self):

        localctx = BKOOLParser.ListmemberprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listmemberprime)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.member()
                self.state = 152
                self.listmemberprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 162
                self.mutableatt()
                pass

            elif la_ == 2:
                self.state = 163
                self.immutableatt()
                pass


            self.state = 166
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableatt" ):
                return visitor.visitMutableatt(self)
            else:
                return visitor.visitChildren(self)




    def mutableatt(self):

        localctx = BKOOLParser.MutableattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutableatt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 168
                self.match(BKOOLParser.STATIC)


            self.state = 171
            self.typ()
            self.state = 172
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListattmu" ):
                return visitor.visitListattmu(self)
            else:
                return visitor.visitChildren(self)




    def listattmu(self):

        localctx = BKOOLParser.ListattmuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listattmu)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.attributenamemu()
                self.state = 175
                self.match(BKOOLParser.COMMA)
                self.state = 176
                self.listattmu()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributenamemu" ):
                return visitor.visitAttributenamemu(self)
            else:
                return visitor.visitChildren(self)




    def attributenamemu(self):

        localctx = BKOOLParser.AttributenamemuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributenamemu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKOOLParser.ID)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQ:
                self.state = 182
                self.match(BKOOLParser.EQ)
                self.state = 183
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableatt" ):
                return visitor.visitImmutableatt(self)
            else:
                return visitor.visitChildren(self)




    def immutableatt(self):

        localctx = BKOOLParser.ImmutableattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_immutableatt)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(BKOOLParser.FINAL)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 187
                    self.match(BKOOLParser.STATIC)


                self.state = 190
                self.typ()
                self.state = 191
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 193
                    self.match(BKOOLParser.STATIC)


                self.state = 196
                self.match(BKOOLParser.FINAL)
                self.state = 197
                self.typ()
                self.state = 198
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListatt" ):
                return visitor.visitListatt(self)
            else:
                return visitor.visitChildren(self)




    def listatt(self):

        localctx = BKOOLParser.ListattContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listatt)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.attributename()
                self.state = 203
                self.match(BKOOLParser.COMMA)
                self.state = 204
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributename" ):
                return visitor.visitAttributename(self)
            else:
                return visitor.visitChildren(self)




    def attributename(self):

        localctx = BKOOLParser.AttributenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attributename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKOOLParser.ID)
            self.state = 210
            self.match(BKOOLParser.EQ)
            self.state = 211
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = BKOOLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 213
                self.match(BKOOLParser.STATIC)


            self.state = 216
            self.typ()
            self.state = 217
            self.match(BKOOLParser.ID)
            self.state = 218
            self.match(BKOOLParser.LB)
            self.state = 219
            self.listparameter()
            self.state = 220
            self.match(BKOOLParser.RB)
            self.state = 221
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListparameter" ):
                return visitor.visitListparameter(self)
            else:
                return visitor.visitChildren(self)




    def listparameter(self):

        localctx = BKOOLParser.ListparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listparameter)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListparameterprime" ):
                return visitor.visitListparameterprime(self)
            else:
                return visitor.visitChildren(self)




    def listparameterprime(self):

        localctx = BKOOLParser.ListparameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listparameterprime)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.paradecl()
                self.state = 228
                self.match(BKOOLParser.SEMI)
                self.state = 229
                self.listparameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParadecl" ):
                return visitor.visitParadecl(self)
            else:
                return visitor.visitChildren(self)




    def paradecl(self):

        localctx = BKOOLParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.typ()
            self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idlist)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(BKOOLParser.ID)
                self.state = 238
                self.match(BKOOLParser.COMMA)
                self.state = 239
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 243
                self.match(BKOOLParser.STATIC)


            self.state = 246
            self.match(BKOOLParser.ID)
            self.state = 247
            self.match(BKOOLParser.LB)
            self.state = 248
            self.listparameter()
            self.state = 249
            self.match(BKOOLParser.RB)
            self.state = 250
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.blockstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.assignmentstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.ifstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.forstatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.breakstatment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.continuestatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.returnstatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstatement" ):
                return visitor.visitBlockstatement(self)
            else:
                return visitor.visitChildren(self)




    def blockstatement(self):

        localctx = BKOOLParser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BKOOLParser.LP)
            self.state = 263
            self.listblock()
            self.state = 264
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListblock" ):
                return visitor.visitListblock(self)
            else:
                return visitor.visitChildren(self)




    def listblock(self):

        localctx = BKOOLParser.ListblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_listblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.blockdecllist()
            self.state = 267
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdecllist" ):
                return visitor.visitBlockdecllist(self)
            else:
                return visitor.visitChildren(self)




    def blockdecllist(self):

        localctx = BKOOLParser.BlockdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockdecllist)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdeclprime" ):
                return visitor.visitBlockdeclprime(self)
            else:
                return visitor.visitChildren(self)




    def blockdeclprime(self):

        localctx = BKOOLParser.BlockdeclprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_blockdeclprime)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.blockdecl()
                self.state = 274
                self.blockdeclprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockbodylist" ):
                return visitor.visitBlockbodylist(self)
            else:
                return visitor.visitChildren(self)




    def blockbodylist(self):

        localctx = BKOOLParser.BlockbodylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_blockbodylist)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.BREAK, BKOOLParser.CONTINUTE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockbodyprime" ):
                return visitor.visitBlockbodyprime(self)
            else:
                return visitor.visitChildren(self)




    def blockbodyprime(self):

        localctx = BKOOLParser.BlockbodyprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_blockbodyprime)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.statement()
                self.state = 284
                self.blockbodyprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def vardeclmu(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclmuContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdecl" ):
                return visitor.visitBlockdecl(self)
            else:
                return visitor.visitChildren(self)




    def blockdecl(self):

        localctx = BKOOLParser.BlockdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_blockdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.state = 289
                self.vardecl()
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.ID]:
                self.state = 290
                self.vardeclmu()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
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

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listatt(self):
            return self.getTypedRuleContext(BKOOLParser.ListattContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKOOLParser.FINAL)
            self.state = 296
            self.typ()
            self.state = 297
            self.listatt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclmuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listattmu(self):
            return self.getTypedRuleContext(BKOOLParser.ListattmuContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardeclmu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclmu" ):
                return visitor.visitVardeclmu(self)
            else:
                return visitor.visitChildren(self)




    def vardeclmu(self):

        localctx = BKOOLParser.VardeclmuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_vardeclmu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.typ()
            self.state = 300
            self.listattmu()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentstatement" ):
                return visitor.visitAssignmentstatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentstatement(self):

        localctx = BKOOLParser.AssignmentstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignmentstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.lhs()
            self.state = 303
            self.match(BKOOLParser.ASSIGN)
            self.state = 304
            self.expression()
            self.state = 305
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.indexexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.instanceattributeaccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstatement" ):
                return visitor.visitIfstatement(self)
            else:
                return visitor.visitChildren(self)




    def ifstatement(self):

        localctx = BKOOLParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(BKOOLParser.IF)
            self.state = 314
            self.expression()
            self.state = 315
            self.match(BKOOLParser.THEN)
            self.state = 316
            self.statement()
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 317
                self.match(BKOOLParser.ELSE)
                self.state = 318
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstatement" ):
                return visitor.visitForstatement(self)
            else:
                return visitor.visitChildren(self)




    def forstatement(self):

        localctx = BKOOLParser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(BKOOLParser.FOR)
            self.state = 322
            self.match(BKOOLParser.ID)
            self.state = 323
            self.match(BKOOLParser.ASSIGN)
            self.state = 324
            self.expression()
            self.state = 325
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 326
            self.expression()
            self.state = 327
            self.match(BKOOLParser.DO)
            self.state = 328
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstatment" ):
                return visitor.visitBreakstatment(self)
            else:
                return visitor.visitChildren(self)




    def breakstatment(self):

        localctx = BKOOLParser.BreakstatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_breakstatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(BKOOLParser.BREAK)
            self.state = 331
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestatement" ):
                return visitor.visitContinuestatement(self)
            else:
                return visitor.visitChildren(self)




    def continuestatement(self):

        localctx = BKOOLParser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(BKOOLParser.CONTINUTE)
            self.state = 334
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstatement" ):
                return visitor.visitReturnstatement(self)
            else:
                return visitor.visitChildren(self)




    def returnstatement(self):

        localctx = BKOOLParser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BKOOLParser.RETURN)
            self.state = 337
            self.expression()
            self.state = 338
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocationstatement" ):
                return visitor.visitMethodinvocationstatement(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocationstatement(self):

        localctx = BKOOLParser.MethodinvocationstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_methodinvocationstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 340
                self.instancemethodinvocation()
                pass

            elif la_ == 2:
                self.state = 341
                self.staticmethodinvocation()
                pass


            self.state = 344
            self.match(BKOOLParser.SEMI)
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

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instanceattributeaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceattributeaccess" ):
                return visitor.visitInstanceattributeaccess(self)
            else:
                return visitor.visitChildren(self)




    def instanceattributeaccess(self):

        localctx = BKOOLParser.InstanceattributeaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_instanceattributeaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expression()
            self.state = 347
            self.match(BKOOLParser.DOT)
            self.state = 348
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticattributeaccess" ):
                return visitor.visitStaticattributeaccess(self)
            else:
                return visitor.visitChildren(self)




    def staticattributeaccess(self):

        localctx = BKOOLParser.StaticattributeaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_staticattributeaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BKOOLParser.ID)
            self.state = 351
            self.match(BKOOLParser.DOT)
            self.state = 352
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

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def methodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.MethodinvocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instancemethodinvocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstancemethodinvocation" ):
                return visitor.visitInstancemethodinvocation(self)
            else:
                return visitor.visitChildren(self)




    def instancemethodinvocation(self):

        localctx = BKOOLParser.InstancemethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instancemethodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expression()
            self.state = 355
            self.match(BKOOLParser.DOT)
            self.state = 356
            self.methodinvocation()
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def methodinvocation(self):
            return self.getTypedRuleContext(BKOOLParser.MethodinvocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_staticmethodinvocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticmethodinvocation" ):
                return visitor.visitStaticmethodinvocation(self)
            else:
                return visitor.visitChildren(self)




    def staticmethodinvocation(self):

        localctx = BKOOLParser.StaticmethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_staticmethodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(BKOOLParser.ID)
            self.state = 359
            self.match(BKOOLParser.DOT)
            self.state = 360
            self.methodinvocation()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocation" ):
                return visitor.visitMethodinvocation(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocation(self):

        localctx = BKOOLParser.MethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_methodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(BKOOLParser.ID)
            self.state = 363
            self.match(BKOOLParser.LB)
            self.state = 364
            self.listexpression()
            self.state = 365
            self.match(BKOOLParser.RB)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKOOLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.exp1()
                self.state = 368
                self.match(BKOOLParser.LT)
                self.state = 369
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.exp1()
                self.state = 372
                self.match(BKOOLParser.GT)
                self.state = 373
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.exp1()
                self.state = 376
                self.match(BKOOLParser.LET)
                self.state = 377
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.exp1()
                self.state = 380
                self.match(BKOOLParser.GET)
                self.state = 381
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 383
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp1)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.exp2(0)
                self.state = 387
                self.match(BKOOLParser.EQE)
                self.state = 388
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.exp2(0)
                self.state = 391
                self.match(BKOOLParser.NEQ)
                self.state = 392
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 406
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 400
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 401
                        self.match(BKOOLParser.AND)
                        self.state = 402
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 403
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 404
                        self.match(BKOOLParser.OR)
                        self.state = 405
                        self.exp3(0)
                        pass

             
                self.state = 410
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 420
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 414
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 415
                        self.match(BKOOLParser.ADD)
                        self.state = 416
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 417
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 418
                        self.match(BKOOLParser.SUB)
                        self.state = 419
                        self.exp4(0)
                        pass

             
                self.state = 424
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 440
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 428
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 429
                        self.match(BKOOLParser.MUL)
                        self.state = 430
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 431
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 432
                        self.match(BKOOLParser.FDIV)
                        self.state = 433
                        self.exp5(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 434
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 435
                        self.match(BKOOLParser.IDIV)
                        self.state = 436
                        self.exp5(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 437
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 438
                        self.match(BKOOLParser.MOD)
                        self.state = 439
                        self.exp5(0)
                        pass

             
                self.state = 444
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 448
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 449
                    self.match(BKOOLParser.CONCATE)
                    self.state = 450
                    self.exp6() 
                self.state = 455
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp6)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(BKOOLParser.NOT)
                self.state = 457
                self.exp6()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp7)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(BKOOLParser.ADD)
                self.state = 462
                self.exp7()
                pass
            elif token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(BKOOLParser.SUB)
                self.state = 464
                self.exp7()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp8)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.exp9(0)
                self.state = 469
                self.match(BKOOLParser.LSB)
                self.state = 470
                self.expression()
                self.state = 471
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.exp9(0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 487
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 479
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 480
                    self.match(BKOOLParser.DOT)
                    self.state = 483
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 481
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 482
                        self.methodinvocation()
                        pass

             
                self.state = 489
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_exp10)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.classcreate()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
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

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_exp11)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(BKOOLParser.LB)
                self.state = 495
                self.expression()
                self.state = 496
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.IO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 500
                self.match(BKOOLParser.IO)
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 501
                self.literal()
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 502
                self.match(BKOOLParser.NIL)
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


    class ListexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListexpression" ):
                return visitor.visitListexpression(self)
            else:
                return visitor.visitChildren(self)




    def listexpression(self):

        localctx = BKOOLParser.ListexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_listexpression)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionprime" ):
                return visitor.visitExpressionprime(self)
            else:
                return visitor.visitChildren(self)




    def expressionprime(self):

        localctx = BKOOLParser.ExpressionprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expressionprime)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.expression()
                self.state = 510
                self.match(BKOOLParser.COMMA)
                self.state = 511
                self.expressionprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_literal)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(BKOOLParser.BOOLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 520
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexpression" ):
                return visitor.visitIndexexpression(self)
            else:
                return visitor.visitChildren(self)




    def indexexpression(self):

        localctx = BKOOLParser.IndexexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.exp9(0)
            self.state = 524
            self.match(BKOOLParser.LSB)
            self.state = 525
            self.expression()
            self.state = 526
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasscreate" ):
                return visitor.visitClasscreate(self)
            else:
                return visitor.visitChildren(self)




    def classcreate(self):

        localctx = BKOOLParser.ClasscreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_classcreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(BKOOLParser.NEW)
            self.state = 529
            self.match(BKOOLParser.ID)
            self.state = 530
            self.match(BKOOLParser.LB)
            self.state = 531
            self.listexpression()
            self.state = 532
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = BKOOLParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(BKOOLParser.LP)
            self.state = 535
            self.array()
            self.state = 536
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
        self.enterRule(localctx, 120, self.RULE_array)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.arrayelement()
                self.state = 539
                self.match(BKOOLParser.COMMA)
                self.state = 540
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayelement" ):
                return visitor.visitArrayelement(self)
            else:
                return visitor.visitChildren(self)




    def arrayelement(self):

        localctx = BKOOLParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_arrayelement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_typ)
        try:
            self.state = 554
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.match(BKOOLParser.INTTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.match(BKOOLParser.FLOATYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 549
                self.match(BKOOLParser.BOOLEANTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 550
                self.match(BKOOLParser.STRINGTYPE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 551
                self.match(BKOOLParser.VOIDTYPE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 552
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 553
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytyp" ):
                return visitor.visitArraytyp(self)
            else:
                return visitor.visitChildren(self)




    def arraytyp(self):

        localctx = BKOOLParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_arraytyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.FLOATYPE) | (1 << BKOOLParser.BOOLEANTYPE) | (1 << BKOOLParser.STRINGTYPE) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 557
            self.match(BKOOLParser.LSB)
            self.state = 558
            self.match(BKOOLParser.INTLIT)
            self.state = 559
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
        self._predicates[44] = self.exp2_sempred
        self._predicates[45] = self.exp3_sempred
        self._predicates[46] = self.exp4_sempred
        self._predicates[47] = self.exp5_sempred
        self._predicates[51] = self.exp9_sempred
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
         




