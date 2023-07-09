# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01f3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\5\2\u009c\n\2\3\2\3\2\3\3\3\3\7\3\u00a2\n\3")
        buf.write("\f\3\16\3\u00a5\13\3\3\3\5\3\u00a8\n\3\3\3\3\3\5\3\u00ac")
        buf.write("\n\3\3\4\3\4\3\4\3\4\7\4\u00b2\n\4\f\4\16\4\u00b5\13\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00da\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\7\r\u00ea\n\r\f\r\16\r\u00ed\13\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\7\63")
        buf.write("\u017e\n\63\f\63\16\63\u0181\13\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\5\64\u0189\n\64\3\64\3\64\3\64\5\64\u018e\n")
        buf.write("\64\3\64\3\64\5\64\u0192\n\64\3\65\3\65\5\65\u0196\n\65")
        buf.write("\3\65\3\65\3\66\6\66\u019b\n\66\r\66\16\66\u019c\3\67")
        buf.write("\3\67\7\67\u01a1\n\67\f\67\16\67\u01a4\13\67\3\67\5\67")
        buf.write("\u01a7\n\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<")
        buf.write("\3<\3=\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\3I\6I\u01d2\nI\rI\16I\u01d3")
        buf.write("\3I\3I\3J\3J\3J\7J\u01db\nJ\fJ\16J\u01de\13J\3J\5J\u01e1")
        buf.write("\nJ\3J\3J\3K\3K\3K\7K\u01e8\nK\fK\16K\u01eb\13K\3K\3K")
        buf.write("\3K\3K\3L\3L\3L\4\u00a3\u00b3\2M\3\3\5\2\7\2\t\4\13\5")
        buf.write("\r\6\17\7\21\b\23\t\25\2\27\2\31\n\33\2\35\2\37\13!\f")
        buf.write("#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279")
        buf.write("\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)")
        buf.write("]*_+a,c-e.g/i\2k\2m\60o\61q\62s\63u\64w\65y\66{\67}8\177")
        buf.write("9\u0081:\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008f")
        buf.write("A\u0091B\u0093C\u0095D\u0097E\3\2\f\6\2\f\f\17\17$$^^")
        buf.write("\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\2GGgg\4")
        buf.write("\2--//\3\2\62;\3\2\63;\5\2\13\f\17\17\"\"\6\2\n\f\16\17")
        buf.write("$$^^\2\u0201\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\3\u009b\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00ad\3\2\2\2\t\u00b9\3\2\2\2\13\u00bd\3\2\2\2\r")
        buf.write("\u00c3\3\2\2\2\17\u00cb\3\2\2\2\21\u00d2\3\2\2\2\23\u00d9")
        buf.write("\3\2\2\2\25\u00db\3\2\2\2\27\u00e0\3\2\2\2\31\u00e6\3")
        buf.write("\2\2\2\33\u00f0\3\2\2\2\35\u00f3\3\2\2\2\37\u00f6\3\2")
        buf.write("\2\2!\u00f8\3\2\2\2#\u00fa\3\2\2\2%\u00fc\3\2\2\2\'\u00fe")
        buf.write("\3\2\2\2)\u0100\3\2\2\2+\u0102\3\2\2\2-\u0105\3\2\2\2")
        buf.write("/\u0107\3\2\2\2\61\u0109\3\2\2\2\63\u010b\3\2\2\2\65\u010d")
        buf.write("\3\2\2\2\67\u010f\3\2\2\29\u0111\3\2\2\2;\u0113\3\2\2")
        buf.write("\2=\u0115\3\2\2\2?\u0117\3\2\2\2A\u011d\3\2\2\2C\u0124")
        buf.write("\3\2\2\2E\u012a\3\2\2\2G\u0130\3\2\2\2I\u0139\3\2\2\2")
        buf.write("K\u013c\3\2\2\2M\u0141\3\2\2\2O\u0149\3\2\2\2Q\u014c\3")
        buf.write("\2\2\2S\u0150\3\2\2\2U\u0155\3\2\2\2W\u0159\3\2\2\2Y\u0160")
        buf.write("\3\2\2\2[\u0165\3\2\2\2]\u0169\3\2\2\2_\u016e\3\2\2\2")
        buf.write("a\u0171\3\2\2\2c\u0178\3\2\2\2e\u017b\3\2\2\2g\u0191\3")
        buf.write("\2\2\2i\u0193\3\2\2\2k\u019a\3\2\2\2m\u01a6\3\2\2\2o\u01a8")
        buf.write("\3\2\2\2q\u01ab\3\2\2\2s\u01ae\3\2\2\2u\u01b1\3\2\2\2")
        buf.write("w\u01b4\3\2\2\2y\u01b7\3\2\2\2{\u01ba\3\2\2\2}\u01bc\3")
        buf.write("\2\2\2\177\u01be\3\2\2\2\u0081\u01c0\3\2\2\2\u0083\u01c2")
        buf.write("\3\2\2\2\u0085\u01c4\3\2\2\2\u0087\u01c6\3\2\2\2\u0089")
        buf.write("\u01c8\3\2\2\2\u008b\u01ca\3\2\2\2\u008d\u01cc\3\2\2\2")
        buf.write("\u008f\u01ce\3\2\2\2\u0091\u01d1\3\2\2\2\u0093\u01d7\3")
        buf.write("\2\2\2\u0095\u01e4\3\2\2\2\u0097\u01f0\3\2\2\2\u0099\u009c")
        buf.write("\5\7\4\2\u009a\u009c\5\5\3\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\b\2\2\2")
        buf.write("\u009e\4\3\2\2\2\u009f\u00a3\7%\2\2\u00a0\u00a2\13\2\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00ab\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a8\7\17\2\2\u00a7\u00a6\3\2\2")
        buf.write("\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac")
        buf.write("\7\f\2\2\u00aa\u00ac\7\2\2\3\u00ab\u00a7\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\6\3\2\2\2\u00ad\u00ae\7\61\2\2\u00ae")
        buf.write("\u00af\7,\2\2\u00af\u00b3\3\2\2\2\u00b0\u00b2\13\2\2\2")
        buf.write("\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b6\u00b7\7,\2\2\u00b7\u00b8\7\61\2\2\u00b8")
        buf.write("\b\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\n\3\2\2\2\u00bd\u00be\7h\2\2\u00be")
        buf.write("\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7c\2\2\u00c1")
        buf.write("\u00c2\7v\2\2\u00c2\f\3\2\2\2\u00c3\u00c4\7d\2\2\u00c4")
        buf.write("\u00c5\7q\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7n\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\16\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd")
        buf.write("\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7i\2\2\u00d1\20\3\2\2\2\u00d2\u00d3\7x\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7f\2\2\u00d6")
        buf.write("\22\3\2\2\2\u00d7\u00da\5\25\13\2\u00d8\u00da\5\27\f\2")
        buf.write("\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\24\3\2")
        buf.write("\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7w\2\2\u00de\u00df\7g\2\2\u00df\26\3\2\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7g\2\2\u00e5\30\3\2\2\2\u00e6\u00eb")
        buf.write("\7$\2\2\u00e7\u00ea\5\33\16\2\u00e8\u00ea\n\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2")
        buf.write("\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3")
        buf.write("\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7$\2\2\u00ef\32")
        buf.write("\3\2\2\2\u00f0\u00f1\7^\2\2\u00f1\u00f2\t\3\2\2\u00f2")
        buf.write("\34\3\2\2\2\u00f3\u00f4\7^\2\2\u00f4\u00f5\n\3\2\2\u00f5")
        buf.write("\36\3\2\2\2\u00f6\u00f7\7*\2\2\u00f7 \3\2\2\2\u00f8\u00f9")
        buf.write("\7+\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7}\2\2\u00fb$\3\2")
        buf.write("\2\2\u00fc\u00fd\7\177\2\2\u00fd&\3\2\2\2\u00fe\u00ff")
        buf.write("\7]\2\2\u00ff(\3\2\2\2\u0100\u0101\7_\2\2\u0101*\3\2\2")
        buf.write("\2\u0102\u0103\7<\2\2\u0103\u0104\7?\2\2\u0104,\3\2\2")
        buf.write("\2\u0105\u0106\7=\2\2\u0106.\3\2\2\2\u0107\u0108\7.\2")
        buf.write("\2\u0108\60\3\2\2\2\u0109\u010a\7\60\2\2\u010a\62\3\2")
        buf.write("\2\2\u010b\u010c\7<\2\2\u010c\64\3\2\2\2\u010d\u010e\7")
        buf.write("\13\2\2\u010e\66\3\2\2\2\u010f\u0110\7\16\2\2\u01108\3")
        buf.write("\2\2\2\u0111\u0112\7\17\2\2\u0112:\3\2\2\2\u0113\u0114")
        buf.write("\7\f\2\2\u0114<\3\2\2\2\u0115\u0116\7\n\2\2\u0116>\3\2")
        buf.write("\2\2\u0117\u0118\7e\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7u\2\2\u011b\u011c\7u\2\2\u011c@\3")
        buf.write("\2\2\2\u011d\u011e\7u\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7c\2\2\u0120\u0121\7v\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7e\2\2\u0123B\3\2\2\2\u0124\u0125\7h\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129D\3\2\2\2\u012a\u012b\7d\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e\7c\2\2\u012e\u012f")
        buf.write("\7m\2\2\u012fF\3\2\2\2\u0130\u0131\7e\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7p\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7p\2\2\u0136\u0137\7w\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138H\3\2\2\2\u0139\u013a\7f\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013bJ\3\2\2\2\u013c\u013d\7g\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e\u013f\7u\2\2\u013f\u0140\7g\2\2\u0140L\3")
        buf.write("\2\2\2\u0141\u0142\7g\2\2\u0142\u0143\7z\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7g\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7f\2\2\u0147\u0148\7u\2\2\u0148N\3\2\2\2\u0149\u014a")
        buf.write("\7k\2\2\u014a\u014b\7h\2\2\u014bP\3\2\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\u014e\7g\2\2\u014e\u014f\7y\2\2\u014fR\3")
        buf.write("\2\2\2\u0150\u0151\7v\2\2\u0151\u0152\7j\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7p\2\2\u0154T\3\2\2\2\u0155\u0156")
        buf.write("\7h\2\2\u0156\u0157\7q\2\2\u0157\u0158\7t\2\2\u0158V\3")
        buf.write("\2\2\2\u0159\u015a\7t\2\2\u015a\u015b\7g\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\u015d\7w\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015fX\3\2\2\2\u0160\u0161\7x\2\2\u0161\u0162")
        buf.write("\7q\2\2\u0162\u0163\7k\2\2\u0163\u0164\7f\2\2\u0164Z\3")
        buf.write("\2\2\2\u0165\u0166\7p\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\\\3\2\2\2\u0169\u016a\7v\2\2\u016a\u016b")
        buf.write("\7j\2\2\u016b\u016c\7k\2\2\u016c\u016d\7u\2\2\u016d^\3")
        buf.write("\2\2\2\u016e\u016f\7v\2\2\u016f\u0170\7q\2\2\u0170`\3")
        buf.write("\2\2\2\u0171\u0172\7f\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write("\7y\2\2\u0174\u0175\7p\2\2\u0175\u0176\7v\2\2\u0176\u0177")
        buf.write("\7q\2\2\u0177b\3\2\2\2\u0178\u0179\7k\2\2\u0179\u017a")
        buf.write("\7q\2\2\u017ad\3\2\2\2\u017b\u017f\t\4\2\2\u017c\u017e")
        buf.write("\t\5\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180f\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0183\5k\66\2\u0183\u0184\5i\65\2")
        buf.write("\u0184\u0192\3\2\2\2\u0185\u0186\5k\66\2\u0186\u0188\5")
        buf.write("\61\31\2\u0187\u0189\5k\66\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u0192\3\2\2\2\u018a\u018b\5k\66\2")
        buf.write("\u018b\u018d\5\61\31\2\u018c\u018e\5k\66\2\u018d\u018c")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0190\5i\65\2\u0190\u0192\3\2\2\2\u0191\u0182\3\2\2\2")
        buf.write("\u0191\u0185\3\2\2\2\u0191\u018a\3\2\2\2\u0192h\3\2\2")
        buf.write("\2\u0193\u0195\t\6\2\2\u0194\u0196\t\7\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0198\5k\66\2\u0198j\3\2\2\2\u0199\u019b\t\b\2\2\u019a")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019dl\3\2\2\2\u019e\u01a2\t\t\2")
        buf.write("\2\u019f\u01a1\t\b\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a7\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7\7\62\2")
        buf.write("\2\u01a6\u019e\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7n\3\2")
        buf.write("\2\2\u01a8\u01a9\7?\2\2\u01a9\u01aa\7?\2\2\u01aap\3\2")
        buf.write("\2\2\u01ab\u01ac\7#\2\2\u01ac\u01ad\7?\2\2\u01adr\3\2")
        buf.write("\2\2\u01ae\u01af\7(\2\2\u01af\u01b0\7(\2\2\u01b0t\3\2")
        buf.write("\2\2\u01b1\u01b2\7>\2\2\u01b2\u01b3\7?\2\2\u01b3v\3\2")
        buf.write("\2\2\u01b4\u01b5\7@\2\2\u01b5\u01b6\7?\2\2\u01b6x\3\2")
        buf.write("\2\2\u01b7\u01b8\7~\2\2\u01b8\u01b9\7~\2\2\u01b9z\3\2")
        buf.write("\2\2\u01ba\u01bb\7-\2\2\u01bb|\3\2\2\2\u01bc\u01bd\7/")
        buf.write("\2\2\u01bd~\3\2\2\2\u01be\u01bf\7\'\2\2\u01bf\u0080\3")
        buf.write("\2\2\2\u01c0\u01c1\7,\2\2\u01c1\u0082\3\2\2\2\u01c2\u01c3")
        buf.write("\7\61\2\2\u01c3\u0084\3\2\2\2\u01c4\u01c5\7^\2\2\u01c5")
        buf.write("\u0086\3\2\2\2\u01c6\u01c7\7?\2\2\u01c7\u0088\3\2\2\2")
        buf.write("\u01c8\u01c9\7>\2\2\u01c9\u008a\3\2\2\2\u01ca\u01cb\7")
        buf.write("@\2\2\u01cb\u008c\3\2\2\2\u01cc\u01cd\7#\2\2\u01cd\u008e")
        buf.write("\3\2\2\2\u01ce\u01cf\7`\2\2\u01cf\u0090\3\2\2\2\u01d0")
        buf.write("\u01d2\t\n\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3")
        buf.write("\2\2\2\u01d5\u01d6\bI\2\2\u01d6\u0092\3\2\2\2\u01d7\u01dc")
        buf.write("\7$\2\2\u01d8\u01db\5\33\16\2\u01d9\u01db\n\13\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e0\3")
        buf.write("\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e1\7\2\2\3\u01e0\u01df")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e3\bJ\3\2\u01e3\u0094\3\2\2\2\u01e4\u01e9\7$\2\2\u01e5")
        buf.write("\u01e8\n\13\2\2\u01e6\u01e8\5\33\16\2\u01e7\u01e5\3\2")
        buf.write("\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01ec\u01ed\5\35\17\2\u01ed\u01ee\3\2\2")
        buf.write("\2\u01ee\u01ef\bK\4\2\u01ef\u0096\3\2\2\2\u01f0\u01f1")
        buf.write("\13\2\2\2\u01f1\u01f2\bL\5\2\u01f2\u0098\3\2\2\2\31\2")
        buf.write("\u009b\u00a3\u00a7\u00ab\u00b3\u00d9\u00e9\u00eb\u017f")
        buf.write("\u0188\u018d\u0191\u0195\u019c\u01a2\u01a6\u01d3\u01da")
        buf.write("\u01dc\u01e0\u01e7\u01e9\6\b\2\2\3J\2\3K\3\3L\4")
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
    TAB = 20
    FF = 21
    CR = 22
    LR = 23
    BS = 24
    CLASS = 25
    STATIC = 26
    FINAL = 27
    BREAK = 28
    CONTINUTE = 29
    DO = 30
    ELSE = 31
    EXTENDS = 32
    IF = 33
    NEW = 34
    THEN = 35
    FOR = 36
    RETURN = 37
    VOID = 38
    NIL = 39
    THIS = 40
    TO = 41
    DOWNTO = 42
    IO = 43
    ID = 44
    FLOATLIT = 45
    INTLIT = 46
    EQE = 47
    NEQ = 48
    AND = 49
    LET = 50
    GET = 51
    OR = 52
    ADD = 53
    SUB = 54
    MOD = 55
    MUL = 56
    FDIV = 57
    IDIV = 58
    EQ = 59
    LT = 60
    GT = 61
    NOT = 62
    CONCATE = 63
    WS = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'boolean'", "'string'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "':='", "';'", "','", "'.'", "':'", "'\t'", 
            "'\f'", "'\r'", "'\n'", "'\b'", "'class'", "'static'", "'final'", 
            "'break'", "'continue'", "'do'", "'else'", "'extends'", "'if'", 
            "'new'", "'then'", "'for'", "'return'", "'nil'", "'this'", "'to'", 
            "'downto'", "'io'", "'=='", "'!='", "'&&'", "'<='", "'>='", 
            "'||'", "'+'", "'-'", "'%'", "'*'", "'/'", "'\\'", "'='", "'<'", 
            "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "VOIDTYPE", "BOOLIT", "STRINGLIT", "LB", "RB", "LP", "RP", "LSB", 
            "RSB", "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", "TAB", "FF", 
            "CR", "LR", "BS", "CLASS", "STATIC", "FINAL", "BREAK", "CONTINUTE", 
            "DO", "ELSE", "EXTENDS", "IF", "NEW", "THEN", "FOR", "RETURN", 
            "VOID", "NIL", "THIS", "TO", "DOWNTO", "IO", "ID", "FLOATLIT", 
            "INTLIT", "EQE", "NEQ", "AND", "LET", "GET", "OR", "ADD", "SUB", 
            "MOD", "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", "CONCATE", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "LINE", "BLOCK", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "VOIDTYPE", "BOOLIT", "TRUE", "FALSE", "STRINGLIT", 
                  "ESC", "ILL_ESC", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                  "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", "TAB", "FF", 
                  "CR", "LR", "BS", "CLASS", "STATIC", "FINAL", "BREAK", 
                  "CONTINUTE", "DO", "ELSE", "EXTENDS", "IF", "NEW", "THEN", 
                  "FOR", "RETURN", "VOID", "NIL", "THIS", "TO", "DOWNTO", 
                  "IO", "ID", "FLOATLIT", "EXPONENT", "NUMBER", "INTLIT", 
                  "EQE", "NEQ", "AND", "LET", "GET", "OR", "ADD", "SUB", 
                  "MOD", "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", 
                  "CONCATE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	ustr= str(self.text)
            	raise UncloseString(ustr[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	istr= str(self.text)
            	raise IllegalEscape(istr[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


