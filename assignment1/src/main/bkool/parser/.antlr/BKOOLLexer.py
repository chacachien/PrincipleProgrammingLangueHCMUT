# Generated from d:\HDD\Documents\Uni\hk223\PPL\assignment\code\PrincipleProgrammingLangueHCMUT\assignment1\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\5\2\u0090\n\2\3\2\3\2\3\3")
        buf.write("\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13\3\3\3\5\3\u009c\n")
        buf.write("\3\3\3\3\3\5\3\u00a0\n\3\3\4\3\4\3\4\3\4\7\4\u00a6\n\4")
        buf.write("\f\4\16\4\u00a9\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5")
        buf.write("\n\u00ce\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\7\r\u00de\n\r\f\r\16\r\u00e1\13\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\7-\u0164\n")
        buf.write("-\f-\16-\u0167\13-\3.\3.\3.\3.\3.\3.\5.\u016f\n.\3.\3")
        buf.write(".\3.\5.\u0174\n.\3.\3.\5.\u0178\n.\3/\3/\5/\u017c\n/\3")
        buf.write("/\3/\3\60\6\60\u0181\n\60\r\60\16\60\u0182\3\61\6\61\u0186")
        buf.write("\n\61\r\61\16\61\u0187\3\62\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3@\3@\3A\3A\3B\3B\3C\6C\u01b3\nC\rC\16C\u01b4\3C\3C\3")
        buf.write("D\3D\3D\7D\u01bc\nD\fD\16D\u01bf\13D\3D\5D\u01c2\nD\3")
        buf.write("D\3D\3E\3E\3E\7E\u01c9\nE\fE\16E\u01cc\13E\3E\3E\3E\3")
        buf.write("E\3F\3F\3F\4\u0097\u00a7\2G\3\3\5\2\7\2\t\4\13\5\r\6\17")
        buf.write("\7\21\b\23\t\25\2\27\2\31\n\33\2\35\2\37\13!\f#\r%\16")
        buf.write("\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31")
        buf.write("=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]\2_\2a")
        buf.write("*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\u0089>\u008b?\3\2\13\6\2\f\f\17")
        buf.write("\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4")
        buf.write("\2GGgg\4\2--//\3\2\62;\5\2\13\f\17\17\"\"\6\2\n\f\16\17")
        buf.write("$$^^\2\u01e1\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008f\3\2\2")
        buf.write("\2\5\u0093\3\2\2\2\7\u00a1\3\2\2\2\t\u00ad\3\2\2\2\13")
        buf.write("\u00b1\3\2\2\2\r\u00b7\3\2\2\2\17\u00bf\3\2\2\2\21\u00c6")
        buf.write("\3\2\2\2\23\u00cd\3\2\2\2\25\u00cf\3\2\2\2\27\u00d4\3")
        buf.write("\2\2\2\31\u00da\3\2\2\2\33\u00e5\3\2\2\2\35\u00e8\3\2")
        buf.write("\2\2\37\u00eb\3\2\2\2!\u00ed\3\2\2\2#\u00ef\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f3\3\2\2\2)\u00f5\3\2\2\2+\u00f7\3\2\2\2")
        buf.write("-\u00fa\3\2\2\2/\u00fc\3\2\2\2\61\u00fe\3\2\2\2\63\u0100")
        buf.write("\3\2\2\2\65\u0102\3\2\2\2\67\u0108\3\2\2\29\u010f\3\2")
        buf.write("\2\2;\u0115\3\2\2\2=\u011b\3\2\2\2?\u0124\3\2\2\2A\u0127")
        buf.write("\3\2\2\2C\u012c\3\2\2\2E\u0134\3\2\2\2G\u0137\3\2\2\2")
        buf.write("I\u013b\3\2\2\2K\u0140\3\2\2\2M\u0144\3\2\2\2O\u014b\3")
        buf.write("\2\2\2Q\u014f\3\2\2\2S\u0154\3\2\2\2U\u0157\3\2\2\2W\u015e")
        buf.write("\3\2\2\2Y\u0161\3\2\2\2[\u0177\3\2\2\2]\u0179\3\2\2\2")
        buf.write("_\u0180\3\2\2\2a\u0185\3\2\2\2c\u0189\3\2\2\2e\u018c\3")
        buf.write("\2\2\2g\u018f\3\2\2\2i\u0192\3\2\2\2k\u0195\3\2\2\2m\u0198")
        buf.write("\3\2\2\2o\u019b\3\2\2\2q\u019d\3\2\2\2s\u019f\3\2\2\2")
        buf.write("u\u01a1\3\2\2\2w\u01a3\3\2\2\2y\u01a5\3\2\2\2{\u01a7\3")
        buf.write("\2\2\2}\u01a9\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01ad\3")
        buf.write("\2\2\2\u0083\u01af\3\2\2\2\u0085\u01b2\3\2\2\2\u0087\u01b8")
        buf.write("\3\2\2\2\u0089\u01c5\3\2\2\2\u008b\u01d1\3\2\2\2\u008d")
        buf.write("\u0090\5\7\4\2\u008e\u0090\5\5\3\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\b")
        buf.write("\2\2\2\u0092\4\3\2\2\2\u0093\u0097\7%\2\2\u0094\u0096")
        buf.write("\13\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009f\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\u009c\7\17\2\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u00a0\7\f\2\2\u009e\u00a0\7\2\2\3\u009f\u009b\3\2\2\2")
        buf.write("\u009f\u009e\3\2\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7\61")
        buf.write("\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a7\3\2\2\2\u00a4\u00a6")
        buf.write("\13\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7,\2\2\u00ab\u00ac\7")
        buf.write("\61\2\2\u00ac\b\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\n\3\2\2\2\u00b1\u00b2")
        buf.write("\7h\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7v\2\2\u00b6\f\3\2\2\2\u00b7\u00b8")
        buf.write("\7d\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\16\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\20\3\2\2\2\u00c6\u00c7")
        buf.write("\7x\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\22\3\2\2\2\u00cb\u00ce\5\25\13\2\u00cc\u00ce")
        buf.write("\5\27\f\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\24\3\2\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write("\u00d2\7w\2\2\u00d2\u00d3\7g\2\2\u00d3\26\3\2\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7n\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8\u00d9\7g\2\2\u00d9\30\3\2\2\2\u00da")
        buf.write("\u00df\7$\2\2\u00db\u00de\5\33\16\2\u00dc\u00de\n\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7$\2\2")
        buf.write("\u00e3\u00e4\b\r\3\2\u00e4\32\3\2\2\2\u00e5\u00e6\7^\2")
        buf.write("\2\u00e6\u00e7\t\3\2\2\u00e7\34\3\2\2\2\u00e8\u00e9\7")
        buf.write("^\2\2\u00e9\u00ea\n\3\2\2\u00ea\36\3\2\2\2\u00eb\u00ec")
        buf.write("\7*\2\2\u00ec \3\2\2\2\u00ed\u00ee\7+\2\2\u00ee\"\3\2")
        buf.write("\2\2\u00ef\u00f0\7}\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7\177")
        buf.write("\2\2\u00f2&\3\2\2\2\u00f3\u00f4\7]\2\2\u00f4(\3\2\2\2")
        buf.write("\u00f5\u00f6\7_\2\2\u00f6*\3\2\2\2\u00f7\u00f8\7<\2\2")
        buf.write("\u00f8\u00f9\7?\2\2\u00f9,\3\2\2\2\u00fa\u00fb\7=\2\2")
        buf.write("\u00fb.\3\2\2\2\u00fc\u00fd\7.\2\2\u00fd\60\3\2\2\2\u00fe")
        buf.write("\u00ff\7\60\2\2\u00ff\62\3\2\2\2\u0100\u0101\7<\2\2\u0101")
        buf.write("\64\3\2\2\2\u0102\u0103\7e\2\2\u0103\u0104\7n\2\2\u0104")
        buf.write("\u0105\7c\2\2\u0105\u0106\7u\2\2\u0106\u0107\7u\2\2\u0107")
        buf.write("\66\3\2\2\2\u0108\u0109\7u\2\2\u0109\u010a\7v\2\2\u010a")
        buf.write("\u010b\7c\2\2\u010b\u010c\7v\2\2\u010c\u010d\7k\2\2\u010d")
        buf.write("\u010e\7e\2\2\u010e8\3\2\2\2\u010f\u0110\7h\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7n\2\2\u0114:\3\2\2\2\u0115\u0116\7d\2\2\u0116")
        buf.write("\u0117\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write("\u011a\7m\2\2\u011a<\3\2\2\2\u011b\u011c\7e\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f")
        buf.write("\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7w\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123>\3\2\2\2\u0124\u0125\7f\2\2\u0125")
        buf.write("\u0126\7q\2\2\u0126@\3\2\2\2\u0127\u0128\7g\2\2\u0128")
        buf.write("\u0129\7n\2\2\u0129\u012a\7u\2\2\u012a\u012b\7g\2\2\u012b")
        buf.write("B\3\2\2\2\u012c\u012d\7g\2\2\u012d\u012e\7z\2\2\u012e")
        buf.write("\u012f\7v\2\2\u012f\u0130\7g\2\2\u0130\u0131\7p\2\2\u0131")
        buf.write("\u0132\7f\2\2\u0132\u0133\7u\2\2\u0133D\3\2\2\2\u0134")
        buf.write("\u0135\7k\2\2\u0135\u0136\7h\2\2\u0136F\3\2\2\2\u0137")
        buf.write("\u0138\7p\2\2\u0138\u0139\7g\2\2\u0139\u013a\7y\2\2\u013a")
        buf.write("H\3\2\2\2\u013b\u013c\7v\2\2\u013c\u013d\7j\2\2\u013d")
        buf.write("\u013e\7g\2\2\u013e\u013f\7p\2\2\u013fJ\3\2\2\2\u0140")
        buf.write("\u0141\7h\2\2\u0141\u0142\7q\2\2\u0142\u0143\7t\2\2\u0143")
        buf.write("L\3\2\2\2\u0144\u0145\7t\2\2\u0145\u0146\7g\2\2\u0146")
        buf.write("\u0147\7v\2\2\u0147\u0148\7w\2\2\u0148\u0149\7t\2\2\u0149")
        buf.write("\u014a\7p\2\2\u014aN\3\2\2\2\u014b\u014c\7p\2\2\u014c")
        buf.write("\u014d\7k\2\2\u014d\u014e\7n\2\2\u014eP\3\2\2\2\u014f")
        buf.write("\u0150\7v\2\2\u0150\u0151\7j\2\2\u0151\u0152\7k\2\2\u0152")
        buf.write("\u0153\7u\2\2\u0153R\3\2\2\2\u0154\u0155\7v\2\2\u0155")
        buf.write("\u0156\7q\2\2\u0156T\3\2\2\2\u0157\u0158\7f\2\2\u0158")
        buf.write("\u0159\7q\2\2\u0159\u015a\7y\2\2\u015a\u015b\7p\2\2\u015b")
        buf.write("\u015c\7v\2\2\u015c\u015d\7q\2\2\u015dV\3\2\2\2\u015e")
        buf.write("\u015f\7k\2\2\u015f\u0160\7q\2\2\u0160X\3\2\2\2\u0161")
        buf.write("\u0165\t\4\2\2\u0162\u0164\t\5\2\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166Z\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169")
        buf.write("\5_\60\2\u0169\u016a\5]/\2\u016a\u0178\3\2\2\2\u016b\u016c")
        buf.write("\5_\60\2\u016c\u016e\5\61\31\2\u016d\u016f\5_\60\2\u016e")
        buf.write("\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0178\3\2\2\2")
        buf.write("\u0170\u0171\5_\60\2\u0171\u0173\5\61\31\2\u0172\u0174")
        buf.write("\5_\60\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0176\5]/\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0168\3\2\2\2\u0177\u016b\3\2\2\2\u0177\u0170\3\2\2\2")
        buf.write("\u0178\\\3\2\2\2\u0179\u017b\t\6\2\2\u017a\u017c\t\7\2")
        buf.write("\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017e\5_\60\2\u017e^\3\2\2\2\u017f\u0181")
        buf.write("\t\b\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183`\3\2\2\2\u0184")
        buf.write("\u0186\t\b\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188b\3\2\2")
        buf.write("\2\u0189\u018a\7?\2\2\u018a\u018b\7?\2\2\u018bd\3\2\2")
        buf.write("\2\u018c\u018d\7#\2\2\u018d\u018e\7?\2\2\u018ef\3\2\2")
        buf.write("\2\u018f\u0190\7(\2\2\u0190\u0191\7(\2\2\u0191h\3\2\2")
        buf.write("\2\u0192\u0193\7>\2\2\u0193\u0194\7?\2\2\u0194j\3\2\2")
        buf.write("\2\u0195\u0196\7@\2\2\u0196\u0197\7?\2\2\u0197l\3\2\2")
        buf.write("\2\u0198\u0199\7~\2\2\u0199\u019a\7~\2\2\u019an\3\2\2")
        buf.write("\2\u019b\u019c\7-\2\2\u019cp\3\2\2\2\u019d\u019e\7/\2")
        buf.write("\2\u019er\3\2\2\2\u019f\u01a0\7\'\2\2\u01a0t\3\2\2\2\u01a1")
        buf.write("\u01a2\7,\2\2\u01a2v\3\2\2\2\u01a3\u01a4\7\61\2\2\u01a4")
        buf.write("x\3\2\2\2\u01a5\u01a6\7^\2\2\u01a6z\3\2\2\2\u01a7\u01a8")
        buf.write("\7?\2\2\u01a8|\3\2\2\2\u01a9\u01aa\7>\2\2\u01aa~\3\2\2")
        buf.write("\2\u01ab\u01ac\7@\2\2\u01ac\u0080\3\2\2\2\u01ad\u01ae")
        buf.write("\7#\2\2\u01ae\u0082\3\2\2\2\u01af\u01b0\7`\2\2\u01b0\u0084")
        buf.write("\3\2\2\2\u01b1\u01b3\t\t\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b7\bC\2\2\u01b7\u0086\3")
        buf.write("\2\2\2\u01b8\u01bd\7$\2\2\u01b9\u01bc\5\33\16\2\u01ba")
        buf.write("\u01bc\n\n\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c2")
        buf.write("\7\2\2\3\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c4\bD\4\2\u01c4\u0088\3\2\2\2")
        buf.write("\u01c5\u01ca\7$\2\2\u01c6\u01c9\n\n\2\2\u01c7\u01c9\5")
        buf.write("\33\16\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\5")
        buf.write("\35\17\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\bE\5\2\u01d0")
        buf.write("\u008a\3\2\2\2\u01d1\u01d2\13\2\2\2\u01d2\u01d3\bF\6\2")
        buf.write("\u01d3\u008c\3\2\2\2\30\2\u008f\u0097\u009b\u009f\u00a7")
        buf.write("\u00cd\u00dd\u00df\u0165\u016e\u0173\u0177\u017b\u0182")
        buf.write("\u0187\u01b4\u01bb\u01bd\u01c1\u01c8\u01ca\7\b\2\2\3\r")
        buf.write("\2\3D\3\3E\4\3F\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTTYPE = 2
    FLOATYPE = 3
    BOOLEANTYPE = 4
    STRINGTYPE = 5
    VOIDTYPE = 6
    BOOLIT = 7
    STRINGLIT = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    LSB = 13
    RSB = 14
    ASSIGN = 15
    SEMI = 16
    COMMA = 17
    DOT = 18
    COLON = 19
    CLASS = 20
    STATIC = 21
    FINAL = 22
    BREAK = 23
    CONTINUTE = 24
    DO = 25
    ELSE = 26
    EXTENDS = 27
    IF = 28
    NEW = 29
    THEN = 30
    FOR = 31
    RETURN = 32
    NIL = 33
    THIS = 34
    TO = 35
    DOWNTO = 36
    IO = 37
    ID = 38
    FLOATLIT = 39
    INTLIT = 40
    EQE = 41
    NEQ = 42
    AND = 43
    LET = 44
    GET = 45
    OR = 46
    ADD = 47
    SUB = 48
    MOD = 49
    MUL = 50
    FDIV = 51
    IDIV = 52
    EQ = 53
    LT = 54
    GT = 55
    NOT = 56
    CONCATE = 57
    WS = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'boolean'", "'string'", "'void'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "':='", "';'", "','", "'.'", 
            "':'", "'class'", "'static'", "'final'", "'break'", "'continue'", 
            "'do'", "'else'", "'extends'", "'if'", "'new'", "'then'", "'for'", 
            "'return'", "'nil'", "'this'", "'to'", "'downto'", "'io'", "'=='", 
            "'!='", "'&&'", "'<='", "'>='", "'||'", "'+'", "'-'", "'%'", 
            "'*'", "'/'", "'\\'", "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "VOIDTYPE", "BOOLIT", "STRINGLIT", "LB", "RB", "LP", "RP", "LSB", 
            "RSB", "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", "CLASS", "STATIC", 
            "FINAL", "BREAK", "CONTINUTE", "DO", "ELSE", "EXTENDS", "IF", 
            "NEW", "THEN", "FOR", "RETURN", "NIL", "THIS", "TO", "DOWNTO", 
            "IO", "ID", "FLOATLIT", "INTLIT", "EQE", "NEQ", "AND", "LET", 
            "GET", "OR", "ADD", "SUB", "MOD", "MUL", "FDIV", "IDIV", "EQ", 
            "LT", "GT", "NOT", "CONCATE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "LINE", "BLOCK", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "VOIDTYPE", "BOOLIT", "TRUE", "FALSE", "STRINGLIT", 
                  "ESC", "ILL_ESC", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                  "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", "CLASS", "STATIC", 
                  "FINAL", "BREAK", "CONTINUTE", "DO", "ELSE", "EXTENDS", 
                  "IF", "NEW", "THEN", "FOR", "RETURN", "NIL", "THIS", "TO", 
                  "DOWNTO", "IO", "ID", "FLOATLIT", "EXPONENT", "NUMBER", 
                  "INTLIT", "EQE", "NEQ", "AND", "LET", "GET", "OR", "ADD", 
                  "SUB", "MOD", "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", 
                  "NOT", "CONCATE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.STRINGLIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	ustr= str(self.text)
            	raise UncloseString(ustr[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	istr= str(self.text)
            	raise IllegalEscape(istr[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


