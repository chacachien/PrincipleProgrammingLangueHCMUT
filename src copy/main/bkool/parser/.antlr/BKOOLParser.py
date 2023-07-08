# Generated from d:\HDD\Documents\Uni\hk223\PPL\assignment\assignment 1\initial1\initial\pull\PrincipleProgrammingLangueHCMUT\src copy\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0234\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0090\n\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u0096\n\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\u009e")
        buf.write("\n\5\3\6\3\6\3\6\3\6\5\6\u00a4\n\6\3\7\3\7\5\7\u00a8\n")
        buf.write("\7\3\b\3\b\5\b\u00ac\n\b\3\b\3\b\3\t\5\t\u00b1\n\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\5\n\u00b8\n\n\3\n\3\n\3\n\3\n\5\n\u00be")
        buf.write("\n\n\3\n\3\n\3\n\3\n\5\n\u00c4\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00cb\n\13\3\f\3\f\3\f\5\f\u00d0\n\f\3\r\5")
        buf.write("\r\u00d3\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u00de\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00e5\n\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00ee\n\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00fd\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\26\3\26\5\26\u0108\n\26\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u010e\n\27\3\30\3\30\5\30\u0112\n\30\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0118\n\31\3\32\3\32\5\32\u011c\n\32\3\32\3\32")
        buf.write("\3\33\5\33\u0121\n\33\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\5\35\u012f\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0137\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\5#\u014e\n#\3#\3#\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0163\n$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\5%\u016e\n%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\7&\u0179\n&\f&\16&\u017c\13&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\7\'\u0187\n\'\f\'\16\'\u018a\13\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u019b\n(\f(\16")
        buf.write("(\u019e\13(\3)\3)\3)\3)\3)\3)\7)\u01a6\n)\f)\16)\u01a9")
        buf.write("\13)\3*\3*\3*\5*\u01ae\n*\3+\3+\3+\3+\3+\5+\u01b5\n+\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u01bf\n,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u01c8\n-\7-\u01ca\n-\f-\16-\u01cd\13-\3.\3.\5.\u01d1")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\3/\5/\u01da\n/\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01e0\n\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\5\66\u01ff\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u0206\n")
        buf.write("\67\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0226\n>\3")
        buf.write("?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3D\2\7JLNPXE\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\2\n\3\2+,\4\2**-.\4\2\t\n/\60\3\2\4\7\5\2\61\62")
        buf.write("\64\65\67?\6\2\64\65\678:;=?\5\2\61\63\66\66@@\3\2\4\b")
        buf.write("\2\u0233\2\u0088\3\2\2\2\4\u008f\3\2\2\2\6\u0091\3\2\2")
        buf.write("\2\b\u009d\3\2\2\2\n\u00a3\3\2\2\2\f\u00a7\3\2\2\2\16")
        buf.write("\u00ab\3\2\2\2\20\u00b0\3\2\2\2\22\u00c3\3\2\2\2\24\u00ca")
        buf.write("\3\2\2\2\26\u00cc\3\2\2\2\30\u00d2\3\2\2\2\32\u00dd\3")
        buf.write("\2\2\2\34\u00e4\3\2\2\2\36\u00e6\3\2\2\2 \u00ed\3\2\2")
        buf.write("\2\"\u00ef\3\2\2\2$\u00fc\3\2\2\2&\u00fe\3\2\2\2(\u0102")
        buf.write("\3\2\2\2*\u0107\3\2\2\2,\u010d\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u0117\3\2\2\2\62\u011b\3\2\2\2\64\u0120\3\2\2\2\66")
        buf.write("\u0125\3\2\2\28\u012e\3\2\2\2:\u0130\3\2\2\2<\u0138\3")
        buf.write("\2\2\2>\u0141\3\2\2\2@\u0144\3\2\2\2B\u0147\3\2\2\2D\u014d")
        buf.write("\3\2\2\2F\u0162\3\2\2\2H\u016d\3\2\2\2J\u016f\3\2\2\2")
        buf.write("L\u017d\3\2\2\2N\u018b\3\2\2\2P\u019f\3\2\2\2R\u01ad\3")
        buf.write("\2\2\2T\u01b4\3\2\2\2V\u01be\3\2\2\2X\u01c0\3\2\2\2Z\u01d0")
        buf.write("\3\2\2\2\\\u01d9\3\2\2\2^\u01df\3\2\2\2`\u01e1\3\2\2\2")
        buf.write("b\u01e5\3\2\2\2d\u01e9\3\2\2\2f\u01f0\3\2\2\2h\u01f7\3")
        buf.write("\2\2\2j\u01fe\3\2\2\2l\u0205\3\2\2\2n\u0207\3\2\2\2p\u0209")
        buf.write("\3\2\2\2r\u020e\3\2\2\2t\u0214\3\2\2\2v\u021a\3\2\2\2")
        buf.write("x\u021c\3\2\2\2z\u0225\3\2\2\2|\u0227\3\2\2\2~\u0229\3")
        buf.write("\2\2\2\u0080\u022b\3\2\2\2\u0082\u022d\3\2\2\2\u0084\u022f")
        buf.write("\3\2\2\2\u0086\u0231\3\2\2\2\u0088\u0089\5\4\3\2\u0089")
        buf.write("\u008a\7\2\2\3\u008a\3\3\2\2\2\u008b\u008c\5\6\4\2\u008c")
        buf.write("\u008d\5\4\3\2\u008d\u0090\3\2\2\2\u008e\u0090\5\6\4\2")
        buf.write("\u008f\u008b\3\2\2\2\u008f\u008e\3\2\2\2\u0090\5\3\2\2")
        buf.write("\2\u0091\u0092\7\33\2\2\u0092\u0095\7.\2\2\u0093\u0094")
        buf.write("\7\"\2\2\u0094\u0096\7.\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\7\r\2\2")
        buf.write("\u0098\u0099\5\b\5\2\u0099\u009a\7\16\2\2\u009a\7\3\2")
        buf.write("\2\2\u009b\u009e\5\n\6\2\u009c\u009e\3\2\2\2\u009d\u009b")
        buf.write("\3\2\2\2\u009d\u009c\3\2\2\2\u009e\t\3\2\2\2\u009f\u00a0")
        buf.write("\5\f\7\2\u00a0\u00a1\5\n\6\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a4\5\f\7\2\u00a3\u009f\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\13\3\2\2\2\u00a5\u00a8\5\16\b\2\u00a6\u00a8\5\30")
        buf.write("\r\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\r\3")
        buf.write("\2\2\2\u00a9\u00ac\5\20\t\2\u00aa\u00ac\5\22\n\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00ae\7\22\2\2\u00ae\17\3\2\2\2\u00af\u00b1\7\34")
        buf.write("\2\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\5\u0086D\2\u00b3\u00b4\5\24\13\2")
        buf.write("\u00b4\21\3\2\2\2\u00b5\u00b7\7\35\2\2\u00b6\u00b8\7\34")
        buf.write("\2\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00ba\5\u0086D\2\u00ba\u00bb\5\24\13\2")
        buf.write("\u00bb\u00c4\3\2\2\2\u00bc\u00be\7\34\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c0\7\35\2\2\u00c0\u00c1\5\u0086D\2\u00c1\u00c2\5\24")
        buf.write("\13\2\u00c2\u00c4\3\2\2\2\u00c3\u00b5\3\2\2\2\u00c3\u00bd")
        buf.write("\3\2\2\2\u00c4\23\3\2\2\2\u00c5\u00c6\5\26\f\2\u00c6\u00c7")
        buf.write("\7\23\2\2\u00c7\u00c8\5\24\13\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00cb\5\26\f\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\25\3\2\2\2\u00cc\u00cf\7.\2\2\u00cd\u00ce\7=")
        buf.write("\2\2\u00ce\u00d0\5F$\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\27\3\2\2\2\u00d1\u00d3\7\34\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\5\u0086D\2\u00d5\u00d6\7.\2\2\u00d6\u00d7\7\13")
        buf.write("\2\2\u00d7\u00d8\5\32\16\2\u00d8\u00d9\7\f\2\2\u00d9\u00da")
        buf.write("\5&\24\2\u00da\31\3\2\2\2\u00db\u00de\5\34\17\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00de\33\3\2\2\2\u00df\u00e0\5\36\20\2\u00e0\u00e1\7")
        buf.write("\22\2\2\u00e1\u00e2\5\34\17\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e5\5\36\20\2\u00e4\u00df\3\2\2\2\u00e4\u00e3\3\2\2")
        buf.write("\2\u00e5\35\3\2\2\2\u00e6\u00e7\5\u0086D\2\u00e7\u00e8")
        buf.write("\5 \21\2\u00e8\37\3\2\2\2\u00e9\u00ea\7.\2\2\u00ea\u00eb")
        buf.write("\7\23\2\2\u00eb\u00ee\5 \21\2\u00ec\u00ee\7.\2\2\u00ed")
        buf.write("\u00e9\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee!\3\2\2\2\u00ef")
        buf.write("\u00f0\7.\2\2\u00f0\u00f1\7\13\2\2\u00f1\u00f2\5\32\16")
        buf.write("\2\u00f2\u00f3\5&\24\2\u00f3#\3\2\2\2\u00f4\u00fd\5&\24")
        buf.write("\2\u00f5\u00fd\5\66\34\2\u00f6\u00fd\5:\36\2\u00f7\u00fd")
        buf.write("\5<\37\2\u00f8\u00fd\5> \2\u00f9\u00fd\5@!\2\u00fa\u00fd")
        buf.write("\5B\"\2\u00fb\u00fd\5D#\2\u00fc\u00f4\3\2\2\2\u00fc\u00f5")
        buf.write("\3\2\2\2\u00fc\u00f6\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc")
        buf.write("\u00f8\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fb\3\2\2\2\u00fd%\3\2\2\2\u00fe\u00ff\7\r\2")
        buf.write("\2\u00ff\u0100\5(\25\2\u0100\u0101\7\16\2\2\u0101\'\3")
        buf.write("\2\2\2\u0102\u0103\5*\26\2\u0103\u0104\5.\30\2\u0104)")
        buf.write("\3\2\2\2\u0105\u0108\5,\27\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108+\3\2\2\2\u0109")
        buf.write("\u010a\5\62\32\2\u010a\u010b\5,\27\2\u010b\u010e\3\2\2")
        buf.write("\2\u010c\u010e\5\62\32\2\u010d\u0109\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e-\3\2\2\2\u010f\u0112\5\60\31\2\u0110\u0112")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("/\3\2\2\2\u0113\u0114\5$\23\2\u0114\u0115\5\60\31\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0118\5$\23\2\u0117\u0113\3\2\2\2")
        buf.write("\u0117\u0116\3\2\2\2\u0118\61\3\2\2\2\u0119\u011c\5t;")
        buf.write("\2\u011a\u011c\5\64\33\2\u011b\u0119\3\2\2\2\u011b\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\7\22\2\2\u011e")
        buf.write("\63\3\2\2\2\u011f\u0121\7\35\2\2\u0120\u011f\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\5\u0086")
        buf.write("D\2\u0123\u0124\5\24\13\2\u0124\65\3\2\2\2\u0125\u0126")
        buf.write("\58\35\2\u0126\u0127\7\21\2\2\u0127\u0128\5F$\2\u0128")
        buf.write("\u0129\7\22\2\2\u0129\67\3\2\2\2\u012a\u012f\5p9\2\u012b")
        buf.write("\u012f\7.\2\2\u012c\u012f\5`\61\2\u012d\u012f\5b\62\2")
        buf.write("\u012e\u012a\3\2\2\2\u012e\u012b\3\2\2\2\u012e\u012c\3")
        buf.write("\2\2\2\u012e\u012d\3\2\2\2\u012f9\3\2\2\2\u0130\u0131")
        buf.write("\7#\2\2\u0131\u0132\5F$\2\u0132\u0133\7%\2\2\u0133\u0136")
        buf.write("\5$\23\2\u0134\u0135\7!\2\2\u0135\u0137\5$\23\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137;\3\2\2\2\u0138")
        buf.write("\u0139\7&\2\2\u0139\u013a\7.\2\2\u013a\u013b\7\21\2\2")
        buf.write("\u013b\u013c\5F$\2\u013c\u013d\t\2\2\2\u013d\u013e\5F")
        buf.write("$\2\u013e\u013f\7 \2\2\u013f\u0140\5$\23\2\u0140=\3\2")
        buf.write("\2\2\u0141\u0142\7\36\2\2\u0142\u0143\7\22\2\2\u0143?")
        buf.write("\3\2\2\2\u0144\u0145\7\37\2\2\u0145\u0146\7\22\2\2\u0146")
        buf.write("A\3\2\2\2\u0147\u0148\7\'\2\2\u0148\u0149\5F$\2\u0149")
        buf.write("\u014a\7\22\2\2\u014aC\3\2\2\2\u014b\u014e\5d\63\2\u014c")
        buf.write("\u014e\5f\64\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0150\7\22\2\2\u0150E\3\2\2")
        buf.write("\2\u0151\u0152\5H%\2\u0152\u0153\7>\2\2\u0153\u0154\5")
        buf.write("H%\2\u0154\u0163\3\2\2\2\u0155\u0156\5H%\2\u0156\u0157")
        buf.write("\7?\2\2\u0157\u0158\5H%\2\u0158\u0163\3\2\2\2\u0159\u015a")
        buf.write("\5H%\2\u015a\u015b\7\64\2\2\u015b\u015c\5H%\2\u015c\u0163")
        buf.write("\3\2\2\2\u015d\u015e\5H%\2\u015e\u015f\7\65\2\2\u015f")
        buf.write("\u0160\5H%\2\u0160\u0163\3\2\2\2\u0161\u0163\5H%\2\u0162")
        buf.write("\u0151\3\2\2\2\u0162\u0155\3\2\2\2\u0162\u0159\3\2\2\2")
        buf.write("\u0162\u015d\3\2\2\2\u0162\u0161\3\2\2\2\u0163G\3\2\2")
        buf.write("\2\u0164\u0165\5J&\2\u0165\u0166\7\61\2\2\u0166\u0167")
        buf.write("\5J&\2\u0167\u016e\3\2\2\2\u0168\u0169\5J&\2\u0169\u016a")
        buf.write("\7\62\2\2\u016a\u016b\5J&\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016e\5J&\2\u016d\u0164\3\2\2\2\u016d\u0168\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016eI\3\2\2\2\u016f\u0170\b&\1\2\u0170")
        buf.write("\u0171\5L\'\2\u0171\u017a\3\2\2\2\u0172\u0173\f\5\2\2")
        buf.write("\u0173\u0174\7\63\2\2\u0174\u0179\5L\'\2\u0175\u0176\f")
        buf.write("\4\2\2\u0176\u0177\7\66\2\2\u0177\u0179\5L\'\2\u0178\u0172")
        buf.write("\3\2\2\2\u0178\u0175\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bK\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u017e\b\'\1\2\u017e\u017f\5N(\2\u017f")
        buf.write("\u0188\3\2\2\2\u0180\u0181\f\5\2\2\u0181\u0182\7\67\2")
        buf.write("\2\u0182\u0187\5N(\2\u0183\u0184\f\4\2\2\u0184\u0185\7")
        buf.write("8\2\2\u0185\u0187\5N(\2\u0186\u0180\3\2\2\2\u0186\u0183")
        buf.write("\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189M\3\2\2\2\u018a\u0188\3\2\2\2\u018b")
        buf.write("\u018c\b(\1\2\u018c\u018d\5P)\2\u018d\u019c\3\2\2\2\u018e")
        buf.write("\u018f\f\7\2\2\u018f\u0190\7:\2\2\u0190\u019b\5P)\2\u0191")
        buf.write("\u0192\f\6\2\2\u0192\u0193\7;\2\2\u0193\u019b\5P)\2\u0194")
        buf.write("\u0195\f\5\2\2\u0195\u0196\7<\2\2\u0196\u019b\5P)\2\u0197")
        buf.write("\u0198\f\4\2\2\u0198\u0199\79\2\2\u0199\u019b\5P)\2\u019a")
        buf.write("\u018e\3\2\2\2\u019a\u0191\3\2\2\2\u019a\u0194\3\2\2\2")
        buf.write("\u019a\u0197\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019dO\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a0\b)\1\2\u01a0\u01a1\5R*\2\u01a1\u01a7")
        buf.write("\3\2\2\2\u01a2\u01a3\f\4\2\2\u01a3\u01a4\7A\2\2\u01a4")
        buf.write("\u01a6\5R*\2\u01a5\u01a2\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8Q\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ab\7@\2\2\u01ab\u01ae\5R*\2\u01ac")
        buf.write("\u01ae\5T+\2\u01ad\u01aa\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("S\3\2\2\2\u01af\u01b0\7\67\2\2\u01b0\u01b5\5T+\2\u01b1")
        buf.write("\u01b2\78\2\2\u01b2\u01b5\5T+\2\u01b3\u01b5\5V,\2\u01b4")
        buf.write("\u01af\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5U\3\2\2\2\u01b6\u01b7\5X-\2\u01b7\u01b8\7\17\2\2")
        buf.write("\u01b8\u01b9\5F$\2\u01b9\u01ba\7\20\2\2\u01ba\u01bf\3")
        buf.write("\2\2\2\u01bb\u01bf\5X-\2\u01bc\u01bf\5n8\2\u01bd\u01bf")
        buf.write("\7)\2\2\u01be\u01b6\3\2\2\2\u01be\u01bb\3\2\2\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfW\3\2\2\2\u01c0")
        buf.write("\u01c1\b-\1\2\u01c1\u01c2\5Z.\2\u01c2\u01cb\3\2\2\2\u01c3")
        buf.write("\u01c4\f\4\2\2\u01c4\u01c7\7\24\2\2\u01c5\u01c8\7.\2\2")
        buf.write("\u01c6\u01c8\5h\65\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3")
        buf.write("\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c3\3\2\2\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("Y\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d1\5r:\2\u01cf")
        buf.write("\u01d1\5\\/\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2")
        buf.write("\u01d1[\3\2\2\2\u01d2\u01d3\7\13\2\2\u01d3\u01d4\5F$\2")
        buf.write("\u01d4\u01d5\7\f\2\2\u01d5\u01da\3\2\2\2\u01d6\u01da\7")
        buf.write(".\2\2\u01d7\u01da\7*\2\2\u01d8\u01da\7-\2\2\u01d9\u01d2")
        buf.write("\3\2\2\2\u01d9\u01d6\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da]\3\2\2\2\u01db\u01e0\5`\61\2\u01dc")
        buf.write("\u01e0\5b\62\2\u01dd\u01e0\5d\63\2\u01de\u01e0\5f\64\2")
        buf.write("\u01df\u01db\3\2\2\2\u01df\u01dc\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01df\u01de\3\2\2\2\u01e0_\3\2\2\2\u01e1\u01e2")
        buf.write("\t\3\2\2\u01e2\u01e3\7\24\2\2\u01e3\u01e4\7.\2\2\u01e4")
        buf.write("a\3\2\2\2\u01e5\u01e6\7.\2\2\u01e6\u01e7\7\24\2\2\u01e7")
        buf.write("\u01e8\7.\2\2\u01e8c\3\2\2\2\u01e9\u01ea\t\3\2\2\u01ea")
        buf.write("\u01eb\7\24\2\2\u01eb\u01ec\7.\2\2\u01ec\u01ed\7\13\2")
        buf.write("\2\u01ed\u01ee\5j\66\2\u01ee\u01ef\7\f\2\2\u01efe\3\2")
        buf.write("\2\2\u01f0\u01f1\7.\2\2\u01f1\u01f2\7\24\2\2\u01f2\u01f3")
        buf.write("\7.\2\2\u01f3\u01f4\7\13\2\2\u01f4\u01f5\5j\66\2\u01f5")
        buf.write("\u01f6\7\f\2\2\u01f6g\3\2\2\2\u01f7\u01f8\7.\2\2\u01f8")
        buf.write("\u01f9\7\13\2\2\u01f9\u01fa\5j\66\2\u01fa\u01fb\7\f\2")
        buf.write("\2\u01fbi\3\2\2\2\u01fc\u01ff\5l\67\2\u01fd\u01ff\3\2")
        buf.write("\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffk\3")
        buf.write("\2\2\2\u0200\u0201\5F$\2\u0201\u0202\7\23\2\2\u0202\u0203")
        buf.write("\5l\67\2\u0203\u0206\3\2\2\2\u0204\u0206\5F$\2\u0205\u0200")
        buf.write("\3\2\2\2\u0205\u0204\3\2\2\2\u0206m\3\2\2\2\u0207\u0208")
        buf.write("\t\4\2\2\u0208o\3\2\2\2\u0209\u020a\5X-\2\u020a\u020b")
        buf.write("\7\17\2\2\u020b\u020c\5F$\2\u020c\u020d\7\20\2\2\u020d")
        buf.write("q\3\2\2\2\u020e\u020f\7$\2\2\u020f\u0210\7.\2\2\u0210")
        buf.write("\u0211\7\13\2\2\u0211\u0212\5j\66\2\u0212\u0213\7\f\2")
        buf.write("\2\u0213s\3\2\2\2\u0214\u0215\5v<\2\u0215\u0216\7\17\2")
        buf.write("\2\u0216\u0217\7\60\2\2\u0217\u0218\7\20\2\2\u0218\u0219")
        buf.write("\5 \21\2\u0219u\3\2\2\2\u021a\u021b\t\5\2\2\u021bw\3\2")
        buf.write("\2\2\u021c\u021d\7\r\2\2\u021d\u021e\5z>\2\u021e\u021f")
        buf.write("\7\16\2\2\u021fy\3\2\2\2\u0220\u0221\5|?\2\u0221\u0222")
        buf.write("\7\23\2\2\u0222\u0223\5z>\2\u0223\u0226\3\2\2\2\u0224")
        buf.write("\u0226\5|?\2\u0225\u0220\3\2\2\2\u0225\u0224\3\2\2\2\u0226")
        buf.write("{\3\2\2\2\u0227\u0228\t\4\2\2\u0228}\3\2\2\2\u0229\u022a")
        buf.write("\t\6\2\2\u022a\177\3\2\2\2\u022b\u022c\t\7\2\2\u022c\u0081")
        buf.write("\3\2\2\2\u022d\u022e\t\b\2\2\u022e\u0083\3\2\2\2\u022f")
        buf.write("\u0230\7A\2\2\u0230\u0085\3\2\2\2\u0231\u0232\t\t\2\2")
        buf.write("\u0232\u0087\3\2\2\2\60\u008f\u0095\u009d\u00a3\u00a7")
        buf.write("\u00ab\u00b0\u00b7\u00bd\u00c3\u00ca\u00cf\u00d2\u00dd")
        buf.write("\u00e4\u00ed\u00fc\u0107\u010d\u0111\u0117\u011b\u0120")
        buf.write("\u012e\u0136\u014d\u0162\u016d\u0178\u017a\u0186\u0188")
        buf.write("\u019a\u019c\u01a7\u01ad\u01b4\u01be\u01c7\u01cb\u01d0")
        buf.write("\u01d9\u01df\u01fe\u0205\u0225")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'int'", "'float'", "'boolean'", 
                     "'string'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "':='", "';'", 
                     "','", "'.'", "':'", "'\t'", "'\f'", "'\r'", "'\n'", 
                     "'\b'", "'class'", "'static'", "'final'", "'break'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'if'", 
                     "'new'", "'then'", "'for'", "'return'", "<INVALID>", 
                     "'nil'", "'this'", "'to'", "'downto'", "'io'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'=='", "'!='", "'&&'", "'<='", 
                     "'>='", "'||'", "'+'", "'-'", "'%'", "'*'", "'/'", 
                     "'\\'", "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                      "STRINGTYPE", "VOIDTYPE", "BOOLIT", "STRINGLIT", "LB", 
                      "RB", "LP", "RP", "LSB", "RSB", "ASSIGN", "SEMI", 
                      "COMMA", "DOT", "COLON", "TAB", "FF", "CR", "LR", 
                      "BS", "CLASS", "STATIC", "FINAL", "BREAK", "CONTINUTE", 
                      "DO", "ELSE", "EXTENDS", "IF", "NEW", "THEN", "FOR", 
                      "RETURN", "VOID", "NIL", "THIS", "TO", "DOWNTO", "IO", 
                      "ID", "FLOATLIT", "INTLIT", "EQE", "NEQ", "AND", "LET", 
                      "GET", "OR", "ADD", "SUB", "MOD", "MUL", "FDIV", "IDIV", 
                      "EQ", "LT", "GT", "NOT", "CONCATE", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_bkool = 1
    RULE_classdecl = 2
    RULE_listmember = 3
    RULE_listmemberprime = 4
    RULE_member = 5
    RULE_attribute = 6
    RULE_mutableatt = 7
    RULE_immutableatt = 8
    RULE_listatt = 9
    RULE_attributename = 10
    RULE_method = 11
    RULE_listparameter = 12
    RULE_listparameterprime = 13
    RULE_paradecl = 14
    RULE_idlist = 15
    RULE_constructor = 16
    RULE_statement = 17
    RULE_blockstatement = 18
    RULE_listblock = 19
    RULE_blockdecllist = 20
    RULE_blockdeclprime = 21
    RULE_blockbodylist = 22
    RULE_blockbodyprime = 23
    RULE_blockdecl = 24
    RULE_vardecl = 25
    RULE_assignmentstatement = 26
    RULE_lhs = 27
    RULE_ifstatement = 28
    RULE_forstatement = 29
    RULE_breakstatment = 30
    RULE_continuestatement = 31
    RULE_returnstatement = 32
    RULE_methodinvocationstatement = 33
    RULE_expression = 34
    RULE_exp1 = 35
    RULE_exp2 = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_exp7 = 41
    RULE_exp8 = 42
    RULE_exp9 = 43
    RULE_exp10 = 44
    RULE_exp11 = 45
    RULE_memberaccess = 46
    RULE_instanceattributeaccess = 47
    RULE_staticattributeaccess = 48
    RULE_instancemethodinvocation = 49
    RULE_staticmethodinvocation = 50
    RULE_methodinvocation = 51
    RULE_listexpression = 52
    RULE_expressionprime = 53
    RULE_literal = 54
    RULE_indexexpression = 55
    RULE_classcreate = 56
    RULE_arraydecl = 57
    RULE_arraytype = 58
    RULE_arraylist = 59
    RULE_array = 60
    RULE_arrayelement = 61
    RULE_intoperator = 62
    RULE_floatoperator = 63
    RULE_booloperator = 64
    RULE_stringoperator = 65
    RULE_typ = 66

    ruleNames =  [ "program", "bkool", "classdecl", "listmember", "listmemberprime", 
                   "member", "attribute", "mutableatt", "immutableatt", 
                   "listatt", "attributename", "method", "listparameter", 
                   "listparameterprime", "paradecl", "idlist", "constructor", 
                   "statement", "blockstatement", "listblock", "blockdecllist", 
                   "blockdeclprime", "blockbodylist", "blockbodyprime", 
                   "blockdecl", "vardecl", "assignmentstatement", "lhs", 
                   "ifstatement", "forstatement", "breakstatment", "continuestatement", 
                   "returnstatement", "methodinvocationstatement", "expression", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "memberaccess", "instanceattributeaccess", 
                   "staticattributeaccess", "instancemethodinvocation", 
                   "staticmethodinvocation", "methodinvocation", "listexpression", 
                   "expressionprime", "literal", "indexexpression", "classcreate", 
                   "arraydecl", "arraytype", "arraylist", "array", "arrayelement", 
                   "intoperator", "floatoperator", "booloperator", "stringoperator", 
                   "typ" ]

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
    TAB=20
    FF=21
    CR=22
    LR=23
    BS=24
    CLASS=25
    STATIC=26
    FINAL=27
    BREAK=28
    CONTINUTE=29
    DO=30
    ELSE=31
    EXTENDS=32
    IF=33
    NEW=34
    THEN=35
    FOR=36
    RETURN=37
    VOID=38
    NIL=39
    THIS=40
    TO=41
    DOWNTO=42
    IO=43
    ID=44
    FLOATLIT=45
    INTLIT=46
    EQE=47
    NEQ=48
    AND=49
    LET=50
    GET=51
    OR=52
    ADD=53
    SUB=54
    MOD=55
    MUL=56
    FDIV=57
    IDIV=58
    EQ=59
    LT=60
    GT=61
    NOT=62
    CONCATE=63
    WS=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    ERROR_CHAR=67

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
            self.state = 134
            self.bkool()
            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.classdecl()
                self.state = 138
                self.bkool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 143
            self.match(BKOOLParser.CLASS)
            self.state = 144
            self.match(BKOOLParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 145
                self.match(BKOOLParser.EXTENDS)
                self.state = 146
                self.match(BKOOLParser.ID)


            self.state = 149
            self.match(BKOOLParser.LP)
            self.state = 150
            self.listmember()
            self.state = 151
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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.STATIC, BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
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
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.member()
                self.state = 158
                self.listmemberprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_member




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.method()
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 167
                self.mutableatt()
                pass

            elif la_ == 2:
                self.state = 168
                self.immutableatt()
                pass


            self.state = 171
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


        def listatt(self):
            return self.getTypedRuleContext(BKOOLParser.ListattContext,0)


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
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 173
                self.match(BKOOLParser.STATIC)


            self.state = 176
            self.typ()
            self.state = 177
            self.listatt()
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
        self.enterRule(localctx, 16, self.RULE_immutableatt)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(BKOOLParser.FINAL)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 180
                    self.match(BKOOLParser.STATIC)


                self.state = 183
                self.typ()
                self.state = 184
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 186
                    self.match(BKOOLParser.STATIC)


                self.state = 189
                self.match(BKOOLParser.FINAL)
                self.state = 190
                self.typ()
                self.state = 191
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
        self.enterRule(localctx, 18, self.RULE_listatt)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.attributename()
                self.state = 196
                self.match(BKOOLParser.COMMA)
                self.state = 197
                self.listatt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        self.enterRule(localctx, 20, self.RULE_attributename)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BKOOLParser.ID)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQ:
                self.state = 203
                self.match(BKOOLParser.EQ)
                self.state = 204
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
        self.enterRule(localctx, 22, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 207
                self.match(BKOOLParser.STATIC)


            self.state = 210
            self.typ()
            self.state = 211
            self.match(BKOOLParser.ID)
            self.state = 212
            self.match(BKOOLParser.LB)
            self.state = 213
            self.listparameter()
            self.state = 214
            self.match(BKOOLParser.RB)
            self.state = 215
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
        self.enterRule(localctx, 24, self.RULE_listparameter)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.listparameterprime()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.LP]:
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
        self.enterRule(localctx, 26, self.RULE_listparameterprime)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.paradecl()
                self.state = 222
                self.match(BKOOLParser.SEMI)
                self.state = 223
                self.listparameterprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
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
        self.enterRule(localctx, 28, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.typ()
            self.state = 229
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
        self.enterRule(localctx, 30, self.RULE_idlist)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(BKOOLParser.ID)
                self.state = 232
                self.match(BKOOLParser.COMMA)
                self.state = 233
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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


        def blockstatement(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(BKOOLParser.ID)
            self.state = 238
            self.match(BKOOLParser.LB)
            self.state = 239
            self.listparameter()
            self.state = 240
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
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.blockstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.assignmentstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.ifstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.forstatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.breakstatment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                self.continuestatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 248
                self.returnstatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 249
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
        self.enterRule(localctx, 36, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BKOOLParser.LP)
            self.state = 253
            self.listblock()
            self.state = 254
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
        self.enterRule(localctx, 38, self.RULE_listblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.blockdecllist()
            self.state = 257
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
        self.enterRule(localctx, 40, self.RULE_blockdecllist)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.FLOATYPE, BKOOLParser.BOOLEANTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.blockdeclprime()
                pass
            elif token in [BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.RP, BKOOLParser.BREAK, BKOOLParser.CONTINUTE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID]:
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
        self.enterRule(localctx, 42, self.RULE_blockdeclprime)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.blockdecl()
                self.state = 264
                self.blockdeclprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 44, self.RULE_blockbodylist)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.BREAK, BKOOLParser.CONTINUTE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
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
        self.enterRule(localctx, 46, self.RULE_blockbodyprime)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.statement()
                self.state = 274
                self.blockbodyprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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

        def arraydecl(self):
            return self.getTypedRuleContext(BKOOLParser.ArraydeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockdecl




    def blockdecl(self):

        localctx = BKOOLParser.BlockdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_blockdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 279
                self.arraydecl()
                pass

            elif la_ == 2:
                self.state = 280
                self.vardecl()
                pass


            self.state = 283
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
        self.enterRule(localctx, 50, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 285
                self.match(BKOOLParser.FINAL)


            self.state = 288
            self.typ()
            self.state = 289
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
        self.enterRule(localctx, 52, self.RULE_assignmentstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.lhs()
            self.state = 292
            self.match(BKOOLParser.ASSIGN)
            self.state = 293
            self.expression()
            self.state = 294
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
        self.enterRule(localctx, 54, self.RULE_lhs)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.indexexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.instanceattributeaccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
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
        self.enterRule(localctx, 56, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKOOLParser.IF)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(BKOOLParser.THEN)
            self.state = 305
            self.statement()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 306
                self.match(BKOOLParser.ELSE)
                self.state = 307
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
        self.enterRule(localctx, 58, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(BKOOLParser.FOR)
            self.state = 311
            self.match(BKOOLParser.ID)
            self.state = 312
            self.match(BKOOLParser.ASSIGN)
            self.state = 313
            self.expression()
            self.state = 314
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 315
            self.expression()
            self.state = 316
            self.match(BKOOLParser.DO)
            self.state = 317
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
        self.enterRule(localctx, 60, self.RULE_breakstatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKOOLParser.BREAK)
            self.state = 320
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
        self.enterRule(localctx, 62, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BKOOLParser.CONTINUTE)
            self.state = 323
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
        self.enterRule(localctx, 64, self.RULE_returnstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKOOLParser.RETURN)
            self.state = 326
            self.expression()
            self.state = 327
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
        self.enterRule(localctx, 66, self.RULE_methodinvocationstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 329
                self.instancemethodinvocation()
                pass

            elif la_ == 2:
                self.state = 330
                self.staticmethodinvocation()
                pass


            self.state = 333
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
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.exp1()
                self.state = 336
                self.match(BKOOLParser.LT)
                self.state = 337
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.exp1()
                self.state = 340
                self.match(BKOOLParser.GT)
                self.state = 341
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.exp1()
                self.state = 344
                self.match(BKOOLParser.LET)
                self.state = 345
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.exp1()
                self.state = 348
                self.match(BKOOLParser.GET)
                self.state = 349
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 351
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
        self.enterRule(localctx, 70, self.RULE_exp1)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.exp2(0)
                self.state = 355
                self.match(BKOOLParser.EQE)
                self.state = 356
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.exp2(0)
                self.state = 359
                self.match(BKOOLParser.NEQ)
                self.state = 360
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 374
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 368
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 369
                        self.match(BKOOLParser.AND)
                        self.state = 370
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 371
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 372
                        self.match(BKOOLParser.OR)
                        self.state = 373
                        self.exp3(0)
                        pass

             
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 382
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 383
                        self.match(BKOOLParser.ADD)
                        self.state = 384
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 385
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 386
                        self.match(BKOOLParser.SUB)
                        self.state = 387
                        self.exp4(0)
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 408
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 396
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 397
                        self.match(BKOOLParser.MUL)
                        self.state = 398
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 399
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 400
                        self.match(BKOOLParser.FDIV)
                        self.state = 401
                        self.exp5(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 402
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 403
                        self.match(BKOOLParser.IDIV)
                        self.state = 404
                        self.exp5(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 405
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 406
                        self.match(BKOOLParser.MOD)
                        self.state = 407
                        self.exp5(0)
                        pass

             
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 417
                    self.match(BKOOLParser.CONCATE)
                    self.state = 418
                    self.exp6() 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(BKOOLParser.NOT)
                self.state = 425
                self.exp6()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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
        self.enterRule(localctx, 82, self.RULE_exp7)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(BKOOLParser.ADD)
                self.state = 430
                self.exp7()
                pass
            elif token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(BKOOLParser.SUB)
                self.state = 432
                self.exp7()
                pass
            elif token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
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
        self.enterRule(localctx, 84, self.RULE_exp8)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.exp9(0)
                self.state = 437
                self.match(BKOOLParser.LSB)
                self.state = 438
                self.expression()
                self.state = 439
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.exp9(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 449
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self.match(BKOOLParser.DOT)
                    self.state = 453
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        self.state = 451
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 452
                        self.methodinvocation()
                        pass

             
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_exp10)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.classcreate()
                pass
            elif token in [BKOOLParser.LB, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
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
        self.enterRule(localctx, 90, self.RULE_exp11)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(BKOOLParser.LB)
                self.state = 465
                self.expression()
                self.state = 466
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.IO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
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
        self.enterRule(localctx, 92, self.RULE_memberaccess)
        try:
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.instanceattributeaccess()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.staticattributeaccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.instancemethodinvocation()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 476
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

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def IO(self):
            return self.getToken(BKOOLParser.IO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instanceattributeaccess




    def instanceattributeaccess(self):

        localctx = BKOOLParser.InstanceattributeaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_instanceattributeaccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.IO) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 480
            self.match(BKOOLParser.DOT)
            self.state = 481
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
        self.enterRule(localctx, 96, self.RULE_staticattributeaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(BKOOLParser.ID)
            self.state = 484
            self.match(BKOOLParser.DOT)
            self.state = 485
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

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def listexpression(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def IO(self):
            return self.getToken(BKOOLParser.IO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instancemethodinvocation




    def instancemethodinvocation(self):

        localctx = BKOOLParser.InstancemethodinvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instancemethodinvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.IO) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 488
            self.match(BKOOLParser.DOT)
            self.state = 489
            self.match(BKOOLParser.ID)
            self.state = 490
            self.match(BKOOLParser.LB)
            self.state = 491
            self.listexpression()
            self.state = 492
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
        self.enterRule(localctx, 100, self.RULE_staticmethodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(BKOOLParser.ID)
            self.state = 495
            self.match(BKOOLParser.DOT)
            self.state = 496
            self.match(BKOOLParser.ID)
            self.state = 497
            self.match(BKOOLParser.LB)
            self.state = 498
            self.listexpression()
            self.state = 499
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
        self.enterRule(localctx, 102, self.RULE_methodinvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(BKOOLParser.ID)
            self.state = 502
            self.match(BKOOLParser.LB)
            self.state = 503
            self.listexpression()
            self.state = 504
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
        self.enterRule(localctx, 104, self.RULE_listexpression)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.LB, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.IO, BKOOLParser.ID, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
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
        self.enterRule(localctx, 106, self.RULE_expressionprime)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.expression()
                self.state = 511
                self.match(BKOOLParser.COMMA)
                self.state = 512
                self.expressionprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
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
        self.enterRule(localctx, 110, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.exp9(0)
            self.state = 520
            self.match(BKOOLParser.LSB)
            self.state = 521
            self.expression()
            self.state = 522
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
        self.enterRule(localctx, 112, self.RULE_classcreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(BKOOLParser.NEW)
            self.state = 525
            self.match(BKOOLParser.ID)
            self.state = 526
            self.match(BKOOLParser.LB)
            self.state = 527
            self.listexpression()
            self.state = 528
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arraydecl




    def arraydecl(self):

        localctx = BKOOLParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.arraytype()
            self.state = 531
            self.match(BKOOLParser.LSB)
            self.state = 532
            self.match(BKOOLParser.INTLIT)
            self.state = 533
            self.match(BKOOLParser.RSB)
            self.state = 534
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATYPE(self):
            return self.getToken(BKOOLParser.FLOATYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(BKOOLParser.STRINGTYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(BKOOLParser.BOOLEANTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.FLOATYPE) | (1 << BKOOLParser.BOOLEANTYPE) | (1 << BKOOLParser.STRINGTYPE))) != 0)):
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




    def arraylist(self):

        localctx = BKOOLParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arraylist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(BKOOLParser.LP)
            self.state = 539
            self.array()
            self.state = 540
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
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.arrayelement()
                self.state = 543
                self.match(BKOOLParser.COMMA)
                self.state = 544
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
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
            self.state = 549
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
            self.state = 551
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
            self.state = 553
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
            self.state = 555
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
            self.state = 557
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.FLOATYPE) | (1 << BKOOLParser.BOOLEANTYPE) | (1 << BKOOLParser.STRINGTYPE) | (1 << BKOOLParser.VOIDTYPE))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.exp2_sempred
        self._predicates[37] = self.exp3_sempred
        self._predicates[38] = self.exp4_sempred
        self._predicates[39] = self.exp5_sempred
        self._predicates[43] = self.exp9_sempred
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
         




