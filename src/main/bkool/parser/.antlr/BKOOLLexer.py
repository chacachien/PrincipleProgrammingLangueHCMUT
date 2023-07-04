# Generated from d:\HDD\Documents\Uni\hk223\PPL\assignment\assignment 1\initial1\initial\pull\PrincipleProgrammingLangueHCMUT\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\u01c8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\5\2\u0096")
        buf.write("\n\2\3\2\3\2\3\3\3\3\7\3\u009c\n\3\f\3\16\3\u009f\13\3")
        buf.write("\3\3\5\3\u00a2\n\3\3\3\3\3\5\3\u00a6\n\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00ac\n\4\f\4\16\4\u00af\13\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\5\n\u00d3\n\n\3\n\3\n\7\n\u00d7\n\n\f\n\16")
        buf.write("\n\u00da\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00e3\n\13\3\f\3\f\5\f\u00e7\n\f\3\f\3\f\3\r\6\r\u00ec")
        buf.write("\n\r\r\r\16\r\u00ed\3\16\3\16\3\16\7\16\u00f3\n\16\f\16")
        buf.write("\16\16\u00f6\13\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3")
        buf.write("?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\7E\u01b4\nE\fE\16")
        buf.write("E\u01b7\13E\3F\6F\u01ba\nF\rF\16F\u01bb\3F\3F\3G\3G\3")
        buf.write("G\3H\3H\3H\3I\3I\3I\4\u009d\u00ad\2J\3\3\5\2\7\2\t\4\13")
        buf.write("\5\r\6\17\7\21\b\23\t\25\n\27\2\31\2\33\13\35\2\37\f!")
        buf.write("\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\30")
        buf.write("9\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]")
        buf.write("+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:};\177")
        buf.write("<\u0081=\u0083>\u0085?\u0087@\u0089A\u008bB\u008dC\u008f")
        buf.write("D\u0091E\3\2\13\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f")
        buf.write("\f\17\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\2\u01d0\2\3\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0095\3\2\2")
        buf.write("\2\5\u0099\3\2\2\2\7\u00a7\3\2\2\2\t\u00b3\3\2\2\2\13")
        buf.write("\u00b7\3\2\2\2\r\u00bd\3\2\2\2\17\u00c5\3\2\2\2\21\u00cc")
        buf.write("\3\2\2\2\23\u00d2\3\2\2\2\25\u00e2\3\2\2\2\27\u00e4\3")
        buf.write("\2\2\2\31\u00eb\3\2\2\2\33\u00ef\3\2\2\2\35\u00f9\3\2")
        buf.write("\2\2\37\u00fc\3\2\2\2!\u00fe\3\2\2\2#\u0100\3\2\2\2%\u0102")
        buf.write("\3\2\2\2\'\u0104\3\2\2\2)\u0106\3\2\2\2+\u0108\3\2\2\2")
        buf.write("-\u010b\3\2\2\2/\u010d\3\2\2\2\61\u010f\3\2\2\2\63\u0111")
        buf.write("\3\2\2\2\65\u0113\3\2\2\2\67\u0115\3\2\2\29\u0117\3\2")
        buf.write("\2\2;\u0119\3\2\2\2=\u011b\3\2\2\2?\u011d\3\2\2\2A\u0123")
        buf.write("\3\2\2\2C\u012a\3\2\2\2E\u0130\3\2\2\2G\u0136\3\2\2\2")
        buf.write("I\u013f\3\2\2\2K\u0142\3\2\2\2M\u0147\3\2\2\2O\u014f\3")
        buf.write("\2\2\2Q\u0152\3\2\2\2S\u0156\3\2\2\2U\u015b\3\2\2\2W\u015f")
        buf.write("\3\2\2\2Y\u0166\3\2\2\2[\u016b\3\2\2\2]\u0171\3\2\2\2")
        buf.write("_\u0176\3\2\2\2a\u017a\3\2\2\2c\u017f\3\2\2\2e\u0182\3")
        buf.write("\2\2\2g\u0189\3\2\2\2i\u018c\3\2\2\2k\u018f\3\2\2\2m\u0192")
        buf.write("\3\2\2\2o\u0195\3\2\2\2q\u0198\3\2\2\2s\u019b\3\2\2\2")
        buf.write("u\u019d\3\2\2\2w\u019f\3\2\2\2y\u01a1\3\2\2\2{\u01a3\3")
        buf.write("\2\2\2}\u01a5\3\2\2\2\177\u01a7\3\2\2\2\u0081\u01a9\3")
        buf.write("\2\2\2\u0083\u01ab\3\2\2\2\u0085\u01ad\3\2\2\2\u0087\u01af")
        buf.write("\3\2\2\2\u0089\u01b1\3\2\2\2\u008b\u01b9\3\2\2\2\u008d")
        buf.write("\u01bf\3\2\2\2\u008f\u01c2\3\2\2\2\u0091\u01c5\3\2\2\2")
        buf.write("\u0093\u0096\5\7\4\2\u0094\u0096\5\5\3\2\u0095\u0093\3")
        buf.write("\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\b\2\2\2\u0098\4\3\2\2\2\u0099\u009d\7%\2\2\u009a\u009c")
        buf.write("\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a5\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u00a0\u00a2\7\17\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a6\7\f\2\2\u00a4\u00a6\7\2\2\3\u00a5\u00a1\3\2\2\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a6\6\3\2\2\2\u00a7\u00a8\7\61")
        buf.write("\2\2\u00a8\u00a9\7,\2\2\u00a9\u00ad\3\2\2\2\u00aa\u00ac")
        buf.write("\13\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b0\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00b0\u00b1\7,\2\2\u00b1\u00b2\7")
        buf.write("\61\2\2\u00b2\b\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\n\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7v\2\2\u00bc\f\3\2\2\2\u00bd\u00be")
        buf.write("\7d\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7n\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\20\3\2\2\2\u00cc\u00cd")
        buf.write("\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7f\2\2\u00d0\22\3\2\2\2\u00d1\u00d3\7/\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d8\t\2\2\2\u00d5\u00d7\t\3\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3")
        buf.write("\2\2\2\u00d9\24\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc")
        buf.write("\5\31\r\2\u00dc\u00dd\5\61\31\2\u00dd\u00de\5\31\r\2\u00de")
        buf.write("\u00e3\3\2\2\2\u00df\u00e0\5\31\r\2\u00e0\u00e1\5\27\f")
        buf.write("\2\u00e1\u00e3\3\2\2\2\u00e2\u00db\3\2\2\2\u00e2\u00df")
        buf.write("\3\2\2\2\u00e3\26\3\2\2\2\u00e4\u00e6\t\4\2\2\u00e5\u00e7")
        buf.write("\t\5\2\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00e9\5\31\r\2\u00e9\30\3\2\2\2\u00ea")
        buf.write("\u00ec\t\3\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\32\3\2")
        buf.write("\2\2\u00ef\u00f4\7$\2\2\u00f0\u00f3\5\35\17\2\u00f1\u00f3")
        buf.write("\n\6\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f7\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7")
        buf.write("$\2\2\u00f8\34\3\2\2\2\u00f9\u00fa\7^\2\2\u00fa\u00fb")
        buf.write("\t\7\2\2\u00fb\36\3\2\2\2\u00fc\u00fd\7*\2\2\u00fd \3")
        buf.write("\2\2\2\u00fe\u00ff\7+\2\2\u00ff\"\3\2\2\2\u0100\u0101")
        buf.write("\7}\2\2\u0101$\3\2\2\2\u0102\u0103\7\177\2\2\u0103&\3")
        buf.write("\2\2\2\u0104\u0105\7]\2\2\u0105(\3\2\2\2\u0106\u0107\7")
        buf.write("_\2\2\u0107*\3\2\2\2\u0108\u0109\7<\2\2\u0109\u010a\7")
        buf.write("?\2\2\u010a,\3\2\2\2\u010b\u010c\7=\2\2\u010c.\3\2\2\2")
        buf.write("\u010d\u010e\7.\2\2\u010e\60\3\2\2\2\u010f\u0110\7\60")
        buf.write("\2\2\u0110\62\3\2\2\2\u0111\u0112\7<\2\2\u0112\64\3\2")
        buf.write("\2\2\u0113\u0114\7\13\2\2\u0114\66\3\2\2\2\u0115\u0116")
        buf.write("\7\16\2\2\u01168\3\2\2\2\u0117\u0118\7\17\2\2\u0118:\3")
        buf.write("\2\2\2\u0119\u011a\7\f\2\2\u011a<\3\2\2\2\u011b\u011c")
        buf.write("\7\n\2\2\u011c>\3\2\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7c\2\2\u0120\u0121\7u\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122@\3\2\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7c\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7e\2\2\u0129B\3\2\2\2\u012a\u012b")
        buf.write("\7h\2\2\u012b\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7n\2\2\u012fD\3\2\2\2\u0130\u0131")
        buf.write("\7d\2\2\u0131\u0132\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7m\2\2\u0135F\3\2\2\2\u0136\u0137")
        buf.write("\7e\2\2\u0137\u0138\7q\2\2\u0138\u0139\7p\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7k\2\2\u013b\u013c\7p\2\2\u013c\u013d")
        buf.write("\7w\2\2\u013d\u013e\7g\2\2\u013eH\3\2\2\2\u013f\u0140")
        buf.write("\7f\2\2\u0140\u0141\7q\2\2\u0141J\3\2\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143\u0144\7n\2\2\u0144\u0145\7u\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146L\3\2\2\2\u0147\u0148\7g\2\2\u0148\u0149")
        buf.write("\7z\2\2\u0149\u014a\7v\2\2\u014a\u014b\7g\2\2\u014b\u014c")
        buf.write("\7p\2\2\u014c\u014d\7f\2\2\u014d\u014e\7u\2\2\u014eN\3")
        buf.write("\2\2\2\u014f\u0150\7k\2\2\u0150\u0151\7h\2\2\u0151P\3")
        buf.write("\2\2\2\u0152\u0153\7p\2\2\u0153\u0154\7g\2\2\u0154\u0155")
        buf.write("\7y\2\2\u0155R\3\2\2\2\u0156\u0157\7v\2\2\u0157\u0158")
        buf.write("\7j\2\2\u0158\u0159\7g\2\2\u0159\u015a\7p\2\2\u015aT\3")
        buf.write("\2\2\2\u015b\u015c\7h\2\2\u015c\u015d\7q\2\2\u015d\u015e")
        buf.write("\7t\2\2\u015eV\3\2\2\2\u015f\u0160\7t\2\2\u0160\u0161")
        buf.write("\7g\2\2\u0161\u0162\7v\2\2\u0162\u0163\7w\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164\u0165\7p\2\2\u0165X\3\2\2\2\u0166\u0167")
        buf.write("\7v\2\2\u0167\u0168\7t\2\2\u0168\u0169\7w\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016aZ\3\2\2\2\u016b\u016c\7h\2\2\u016c\u016d")
        buf.write("\7c\2\2\u016d\u016e\7n\2\2\u016e\u016f\7u\2\2\u016f\u0170")
        buf.write("\7g\2\2\u0170\\\3\2\2\2\u0171\u0172\7x\2\2\u0172\u0173")
        buf.write("\7q\2\2\u0173\u0174\7k\2\2\u0174\u0175\7f\2\2\u0175^\3")
        buf.write("\2\2\2\u0176\u0177\7p\2\2\u0177\u0178\7k\2\2\u0178\u0179")
        buf.write("\7n\2\2\u0179`\3\2\2\2\u017a\u017b\7v\2\2\u017b\u017c")
        buf.write("\7j\2\2\u017c\u017d\7k\2\2\u017d\u017e\7u\2\2\u017eb\3")
        buf.write("\2\2\2\u017f\u0180\7v\2\2\u0180\u0181\7q\2\2\u0181d\3")
        buf.write("\2\2\2\u0182\u0183\7f\2\2\u0183\u0184\7q\2\2\u0184\u0185")
        buf.write("\7y\2\2\u0185\u0186\7p\2\2\u0186\u0187\7v\2\2\u0187\u0188")
        buf.write("\7q\2\2\u0188f\3\2\2\2\u0189\u018a\7?\2\2\u018a\u018b")
        buf.write("\7?\2\2\u018bh\3\2\2\2\u018c\u018d\7#\2\2\u018d\u018e")
        buf.write("\7?\2\2\u018ej\3\2\2\2\u018f\u0190\7(\2\2\u0190\u0191")
        buf.write("\7(\2\2\u0191l\3\2\2\2\u0192\u0193\7>\2\2\u0193\u0194")
        buf.write("\7?\2\2\u0194n\3\2\2\2\u0195\u0196\7@\2\2\u0196\u0197")
        buf.write("\7?\2\2\u0197p\3\2\2\2\u0198\u0199\7~\2\2\u0199\u019a")
        buf.write("\7~\2\2\u019ar\3\2\2\2\u019b\u019c\7-\2\2\u019ct\3\2\2")
        buf.write("\2\u019d\u019e\7/\2\2\u019ev\3\2\2\2\u019f\u01a0\7\'\2")
        buf.write("\2\u01a0x\3\2\2\2\u01a1\u01a2\7,\2\2\u01a2z\3\2\2\2\u01a3")
        buf.write("\u01a4\7\61\2\2\u01a4|\3\2\2\2\u01a5\u01a6\7^\2\2\u01a6")
        buf.write("~\3\2\2\2\u01a7\u01a8\7?\2\2\u01a8\u0080\3\2\2\2\u01a9")
        buf.write("\u01aa\7>\2\2\u01aa\u0082\3\2\2\2\u01ab\u01ac\7@\2\2\u01ac")
        buf.write("\u0084\3\2\2\2\u01ad\u01ae\7#\2\2\u01ae\u0086\3\2\2\2")
        buf.write("\u01af\u01b0\7`\2\2\u01b0\u0088\3\2\2\2\u01b1\u01b5\t")
        buf.write("\b\2\2\u01b2\u01b4\t\t\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u008a\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01ba\t\n\2\2")
        buf.write("\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be")
        buf.write("\bF\2\2\u01be\u008c\3\2\2\2\u01bf\u01c0\13\2\2\2\u01c0")
        buf.write("\u01c1\bG\3\2\u01c1\u008e\3\2\2\2\u01c2\u01c3\13\2\2\2")
        buf.write("\u01c3\u01c4\bH\4\2\u01c4\u0090\3\2\2\2\u01c5\u01c6\13")
        buf.write("\2\2\2\u01c6\u01c7\bI\5\2\u01c7\u0092\3\2\2\2\21\2\u0095")
        buf.write("\u009d\u00a1\u00a5\u00ad\u00d2\u00d8\u00e2\u00e6\u00ed")
        buf.write("\u00f2\u00f4\u01b5\u01bb\6\b\2\2\3G\2\3H\3\3I\4")
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
    INTLIT = 7
    FLOATLIT = 8
    STRINGLIT = 9
    LB = 10
    RB = 11
    LP = 12
    RP = 13
    LSB = 14
    RSB = 15
    ASSIGN = 16
    SEMI = 17
    COMMA = 18
    DOT = 19
    COLON = 20
    TAB = 21
    FF = 22
    CR = 23
    LR = 24
    BS = 25
    CLASS = 26
    STATIC = 27
    FINAL = 28
    BREAK = 29
    CONTINUTE = 30
    DO = 31
    ELSE = 32
    EXTENDS = 33
    IF = 34
    NEW = 35
    THEN = 36
    FOR = 37
    RETURN = 38
    TRUE = 39
    FALSE = 40
    VOID = 41
    NIL = 42
    THIS = 43
    TO = 44
    DOWNTO = 45
    EQE = 46
    NEQ = 47
    AND = 48
    LET = 49
    GET = 50
    OR = 51
    ADD = 52
    SUB = 53
    MOD = 54
    MUL = 55
    FDIV = 56
    IDIV = 57
    EQ = 58
    LT = 59
    GT = 60
    NOT = 61
    CONCATE = 62
    ID = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'boolean'", "'string'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "':='", "';'", "','", "'.'", "':'", "'\t'", 
            "'\f'", "'\r'", "'\n'", "'\b'", "'class'", "'static'", "'final'", 
            "'break'", "'continue'", "'do'", "'else'", "'extends'", "'if'", 
            "'new'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'nil'", "'this'", "'to'", "'downto'", "'=='", "'!='", "'&&'", 
            "'<='", "'>='", "'||'", "'+'", "'-'", "'%'", "'*'", "'/'", "'\\'", 
            "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "VOIDTYPE", "INTLIT", "FLOATLIT", "STRINGLIT", "LB", "RB", "LP", 
            "RP", "LSB", "RSB", "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", 
            "TAB", "FF", "CR", "LR", "BS", "CLASS", "STATIC", "FINAL", "BREAK", 
            "CONTINUTE", "DO", "ELSE", "EXTENDS", "IF", "NEW", "THEN", "FOR", 
            "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "TO", "DOWNTO", 
            "EQE", "NEQ", "AND", "LET", "GET", "OR", "ADD", "SUB", "MOD", 
            "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", "CONCATE", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "LINE", "BLOCK", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "VOIDTYPE", "INTLIT", "FLOATLIT", "EXPONENT", 
                  "NUMBER", "STRINGLIT", "ESC", "LB", "RB", "LP", "RP", 
                  "LSB", "RSB", "ASSIGN", "SEMI", "COMMA", "DOT", "COLON", 
                  "TAB", "FF", "CR", "LR", "BS", "CLASS", "STATIC", "FINAL", 
                  "BREAK", "CONTINUTE", "DO", "ELSE", "EXTENDS", "IF", "NEW", 
                  "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", 
                  "THIS", "TO", "DOWNTO", "EQE", "NEQ", "AND", "LET", "GET", 
                  "OR", "ADD", "SUB", "MOD", "MUL", "FDIV", "IDIV", "EQ", 
                  "LT", "GT", "NOT", "CONCATE", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UnclosedString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     


