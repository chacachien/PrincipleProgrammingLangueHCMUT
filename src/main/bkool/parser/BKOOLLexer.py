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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\5\2\u0092\n\2\3\2\3")
        buf.write("\2\3\3\3\3\7\3\u0098\n\3\f\3\16\3\u009b\13\3\3\3\5\3\u009e")
        buf.write("\n\3\3\3\3\3\5\3\u00a2\n\3\3\4\3\4\3\4\3\4\7\4\u00a8\n")
        buf.write("\4\f\4\16\4\u00ab\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\5\t\u00ca\n\t\3\t\3\t\7")
        buf.write("\t\u00ce\n\t\f\t\16\t\u00d1\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00da\n\n\3\13\3\13\5\13\u00de\n\13\3\13\3")
        buf.write("\13\3\f\6\f\u00e3\n\f\r\f\16\f\u00e4\3\r\3\r\3\r\7\r\u00ea")
        buf.write("\n\r\f\r\16\r\u00ed\13\r\3\r\3\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)")
        buf.write("\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\7C\u01a8\n")
        buf.write("C\fC\16C\u01ab\13C\3D\6D\u01ae\nD\rD\16D\u01af\3D\3D\3")
        buf.write("E\3E\3E\3F\3F\3F\3G\3G\3G\4\u0099\u00a9\2H\3\3\5\2\7\2")
        buf.write("\t\4\13\5\r\6\17\7\21\b\23\t\25\2\27\2\31\n\33\2\35\13")
        buf.write("\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27")
        buf.write("\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W")
        buf.write("(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:")
        buf.write("};\177<\u0081=\u0083>\u0085?\u0087@\u0089A\u008bB\u008d")
        buf.write("C\3\2\13\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u01c4\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0091")
        buf.write("\3\2\2\2\5\u0095\3\2\2\2\7\u00a3\3\2\2\2\t\u00af\3\2\2")
        buf.write("\2\13\u00b3\3\2\2\2\r\u00b9\3\2\2\2\17\u00c1\3\2\2\2\21")
        buf.write("\u00c9\3\2\2\2\23\u00d9\3\2\2\2\25\u00db\3\2\2\2\27\u00e2")
        buf.write("\3\2\2\2\31\u00e6\3\2\2\2\33\u00f0\3\2\2\2\35\u00f3\3")
        buf.write("\2\2\2\37\u00f5\3\2\2\2!\u00f7\3\2\2\2#\u00f9\3\2\2\2")
        buf.write("%\u00fb\3\2\2\2\'\u00fd\3\2\2\2)\u00ff\3\2\2\2+\u0101")
        buf.write("\3\2\2\2-\u0103\3\2\2\2/\u0105\3\2\2\2\61\u0107\3\2\2")
        buf.write("\2\63\u0109\3\2\2\2\65\u010b\3\2\2\2\67\u010d\3\2\2\2")
        buf.write("9\u010f\3\2\2\2;\u0111\3\2\2\2=\u0117\3\2\2\2?\u011e\3")
        buf.write("\2\2\2A\u0124\3\2\2\2C\u012a\3\2\2\2E\u0133\3\2\2\2G\u0136")
        buf.write("\3\2\2\2I\u013b\3\2\2\2K\u0143\3\2\2\2M\u0146\3\2\2\2")
        buf.write("O\u014a\3\2\2\2Q\u014f\3\2\2\2S\u0153\3\2\2\2U\u015a\3")
        buf.write("\2\2\2W\u015f\3\2\2\2Y\u0165\3\2\2\2[\u016a\3\2\2\2]\u016e")
        buf.write("\3\2\2\2_\u0173\3\2\2\2a\u0176\3\2\2\2c\u017d\3\2\2\2")
        buf.write("e\u0180\3\2\2\2g\u0183\3\2\2\2i\u0186\3\2\2\2k\u0189\3")
        buf.write("\2\2\2m\u018c\3\2\2\2o\u018f\3\2\2\2q\u0191\3\2\2\2s\u0193")
        buf.write("\3\2\2\2u\u0195\3\2\2\2w\u0197\3\2\2\2y\u0199\3\2\2\2")
        buf.write("{\u019b\3\2\2\2}\u019d\3\2\2\2\177\u019f\3\2\2\2\u0081")
        buf.write("\u01a1\3\2\2\2\u0083\u01a3\3\2\2\2\u0085\u01a5\3\2\2\2")
        buf.write("\u0087\u01ad\3\2\2\2\u0089\u01b3\3\2\2\2\u008b\u01b6\3")
        buf.write("\2\2\2\u008d\u01b9\3\2\2\2\u008f\u0092\5\7\4\2\u0090\u0092")
        buf.write("\5\5\3\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0094\b\2\2\2\u0094\4\3\2\2\2\u0095")
        buf.write("\u0099\7%\2\2\u0096\u0098\13\2\2\2\u0097\u0096\3\2\2\2")
        buf.write("\u0098\u009b\3\2\2\2\u0099\u009a\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u009a\u00a1\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e")
        buf.write("\7\17\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a2\7\f\2\2\u00a0\u00a2\7\2\2\3")
        buf.write("\u00a1\u009d\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\6\3\2\2")
        buf.write("\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\7,\2\2\u00a5\u00a9")
        buf.write("\3\2\2\2\u00a6\u00a8\13\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7")
        buf.write(",\2\2\u00ad\u00ae\7\61\2\2\u00ae\b\3\2\2\2\u00af\u00b0")
        buf.write("\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\n")
        buf.write("\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\f")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7p\2\2\u00c0\16\3\2\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\20")
        buf.write("\3\2\2\2\u00c8\u00ca\7/\2\2\u00c9\u00c8\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cf\t\2\2\2")
        buf.write("\u00cc\u00ce\t\3\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3")
        buf.write("\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\22")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\5\27\f\2\u00d3")
        buf.write("\u00d4\5-\27\2\u00d4\u00d5\5\27\f\2\u00d5\u00da\3\2\2")
        buf.write("\2\u00d6\u00d7\5\27\f\2\u00d7\u00d8\5\25\13\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d2\3\2\2\2\u00d9\u00d6\3\2\2\2\u00da")
        buf.write("\24\3\2\2\2\u00db\u00dd\t\4\2\2\u00dc\u00de\t\5\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e0\5\27\f\2\u00e0\26\3\2\2\2\u00e1\u00e3\t\3")
        buf.write("\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\30\3\2\2\2\u00e6\u00eb")
        buf.write("\7$\2\2\u00e7\u00ea\5\33\16\2\u00e8\u00ea\n\6\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2")
        buf.write("\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3")
        buf.write("\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7$\2\2\u00ef\32")
        buf.write("\3\2\2\2\u00f0\u00f1\7^\2\2\u00f1\u00f2\t\7\2\2\u00f2")
        buf.write("\34\3\2\2\2\u00f3\u00f4\7*\2\2\u00f4\36\3\2\2\2\u00f5")
        buf.write("\u00f6\7+\2\2\u00f6 \3\2\2\2\u00f7\u00f8\7}\2\2\u00f8")
        buf.write("\"\3\2\2\2\u00f9\u00fa\7\177\2\2\u00fa$\3\2\2\2\u00fb")
        buf.write("\u00fc\7]\2\2\u00fc&\3\2\2\2\u00fd\u00fe\7_\2\2\u00fe")
        buf.write("(\3\2\2\2\u00ff\u0100\7=\2\2\u0100*\3\2\2\2\u0101\u0102")
        buf.write("\7.\2\2\u0102,\3\2\2\2\u0103\u0104\7\60\2\2\u0104.\3\2")
        buf.write("\2\2\u0105\u0106\7<\2\2\u0106\60\3\2\2\2\u0107\u0108\7")
        buf.write("\13\2\2\u0108\62\3\2\2\2\u0109\u010a\7\16\2\2\u010a\64")
        buf.write("\3\2\2\2\u010b\u010c\7\17\2\2\u010c\66\3\2\2\2\u010d\u010e")
        buf.write("\7\f\2\2\u010e8\3\2\2\2\u010f\u0110\7\n\2\2\u0110:\3\2")
        buf.write("\2\2\u0111\u0112\7e\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7u\2\2\u0115\u0116\7u\2\2\u0116<\3")
        buf.write("\2\2\2\u0117\u0118\7u\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7e\2\2\u011d>\3\2\2\2\u011e\u011f\7h\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7c\2\2\u0122\u0123")
        buf.write("\7n\2\2\u0123@\3\2\2\2\u0124\u0125\7d\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7g\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7m\2\2\u0129B\3\2\2\2\u012a\u012b\7e\2\2\u012b\u012c")
        buf.write("\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e\7v\2\2\u012e\u012f")
        buf.write("\7k\2\2\u012f\u0130\7p\2\2\u0130\u0131\7w\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132D\3\2\2\2\u0133\u0134\7f\2\2\u0134\u0135")
        buf.write("\7q\2\2\u0135F\3\2\2\2\u0136\u0137\7g\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7u\2\2\u0139\u013a\7g\2\2\u013aH\3")
        buf.write("\2\2\2\u013b\u013c\7g\2\2\u013c\u013d\7z\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141")
        buf.write("\7f\2\2\u0141\u0142\7u\2\2\u0142J\3\2\2\2\u0143\u0144")
        buf.write("\7k\2\2\u0144\u0145\7h\2\2\u0145L\3\2\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7g\2\2\u0148\u0149\7y\2\2\u0149N\3")
        buf.write("\2\2\2\u014a\u014b\7v\2\2\u014b\u014c\7j\2\2\u014c\u014d")
        buf.write("\7g\2\2\u014d\u014e\7p\2\2\u014eP\3\2\2\2\u014f\u0150")
        buf.write("\7h\2\2\u0150\u0151\7q\2\2\u0151\u0152\7t\2\2\u0152R\3")
        buf.write("\2\2\2\u0153\u0154\7t\2\2\u0154\u0155\7g\2\2\u0155\u0156")
        buf.write("\7v\2\2\u0156\u0157\7w\2\2\u0157\u0158\7t\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159T\3\2\2\2\u015a\u015b\7v\2\2\u015b\u015c")
        buf.write("\7t\2\2\u015c\u015d\7w\2\2\u015d\u015e\7g\2\2\u015eV\3")
        buf.write("\2\2\2\u015f\u0160\7h\2\2\u0160\u0161\7c\2\2\u0161\u0162")
        buf.write("\7n\2\2\u0162\u0163\7u\2\2\u0163\u0164\7g\2\2\u0164X\3")
        buf.write("\2\2\2\u0165\u0166\7x\2\2\u0166\u0167\7q\2\2\u0167\u0168")
        buf.write("\7k\2\2\u0168\u0169\7f\2\2\u0169Z\3\2\2\2\u016a\u016b")
        buf.write("\7p\2\2\u016b\u016c\7k\2\2\u016c\u016d\7n\2\2\u016d\\")
        buf.write("\3\2\2\2\u016e\u016f\7v\2\2\u016f\u0170\7j\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7u\2\2\u0172^\3\2\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7q\2\2\u0175`\3\2\2\2\u0176\u0177")
        buf.write("\7f\2\2\u0177\u0178\7q\2\2\u0178\u0179\7y\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7v\2\2\u017b\u017c\7q\2\2\u017cb\3")
        buf.write("\2\2\2\u017d\u017e\7?\2\2\u017e\u017f\7?\2\2\u017fd\3")
        buf.write("\2\2\2\u0180\u0181\7#\2\2\u0181\u0182\7?\2\2\u0182f\3")
        buf.write("\2\2\2\u0183\u0184\7(\2\2\u0184\u0185\7(\2\2\u0185h\3")
        buf.write("\2\2\2\u0186\u0187\7>\2\2\u0187\u0188\7?\2\2\u0188j\3")
        buf.write("\2\2\2\u0189\u018a\7@\2\2\u018a\u018b\7?\2\2\u018bl\3")
        buf.write("\2\2\2\u018c\u018d\7~\2\2\u018d\u018e\7~\2\2\u018en\3")
        buf.write("\2\2\2\u018f\u0190\7-\2\2\u0190p\3\2\2\2\u0191\u0192\7")
        buf.write("/\2\2\u0192r\3\2\2\2\u0193\u0194\7\'\2\2\u0194t\3\2\2")
        buf.write("\2\u0195\u0196\7,\2\2\u0196v\3\2\2\2\u0197\u0198\7\61")
        buf.write("\2\2\u0198x\3\2\2\2\u0199\u019a\7^\2\2\u019az\3\2\2\2")
        buf.write("\u019b\u019c\7?\2\2\u019c|\3\2\2\2\u019d\u019e\7>\2\2")
        buf.write("\u019e~\3\2\2\2\u019f\u01a0\7@\2\2\u01a0\u0080\3\2\2\2")
        buf.write("\u01a1\u01a2\7#\2\2\u01a2\u0082\3\2\2\2\u01a3\u01a4\7")
        buf.write("`\2\2\u01a4\u0084\3\2\2\2\u01a5\u01a9\t\b\2\2\u01a6\u01a8")
        buf.write("\t\t\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u0086\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ac\u01ae\t\n\2\2\u01ad\u01ac\3")
        buf.write("\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\bD\2\2\u01b2")
        buf.write("\u0088\3\2\2\2\u01b3\u01b4\13\2\2\2\u01b4\u01b5\bE\3\2")
        buf.write("\u01b5\u008a\3\2\2\2\u01b6\u01b7\13\2\2\2\u01b7\u01b8")
        buf.write("\bF\4\2\u01b8\u008c\3\2\2\2\u01b9\u01ba\13\2\2\2\u01ba")
        buf.write("\u01bb\bG\5\2\u01bb\u008e\3\2\2\2\21\2\u0091\u0099\u009d")
        buf.write("\u00a1\u00a9\u00c9\u00cf\u00d9\u00dd\u00e4\u00e9\u00eb")
        buf.write("\u01a9\u01af\6\b\2\2\3E\2\3F\3\3G\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTTYPE = 2
    FLOATYPE = 3
    BOOLEANTYPE = 4
    STRINGTYPE = 5
    INTLIT = 6
    FLOATLIT = 7
    STRINGLIT = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    LSB = 13
    RSB = 14
    SEMI = 15
    COMMA = 16
    DOT = 17
    COLON = 18
    TAB = 19
    FF = 20
    CR = 21
    LR = 22
    BS = 23
    CLASS = 24
    STATIC = 25
    FINAL = 26
    BREAK = 27
    CONTINUTE = 28
    DO = 29
    ELSE = 30
    EXTENDS = 31
    IF = 32
    NEW = 33
    THEN = 34
    FOR = 35
    RETURN = 36
    TRUE = 37
    FALSE = 38
    VOID = 39
    NIL = 40
    THIS = 41
    TO = 42
    DOWNTO = 43
    EQE = 44
    NEQ = 45
    AND = 46
    LET = 47
    GET = 48
    OR = 49
    ADD = 50
    SUB = 51
    MOD = 52
    MUL = 53
    FDIV = 54
    IDIV = 55
    EQ = 56
    LT = 57
    GT = 58
    NOT = 59
    CONCATE = 60
    ID = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'boolean'", "'string'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "';'", "','", "'.'", "':'", "'\t'", "'\f'", 
            "'\r'", "'\n'", "'\b'", "'class'", "'static'", "'final'", "'break'", 
            "'continue'", "'do'", "'else'", "'extends'", "'if'", "'new'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'to'", "'downto'", "'=='", "'!='", "'&&'", 
            "'<='", "'>='", "'||'", "'+'", "'-'", "'%'", "'*'", "'/'", "'\\'", 
            "'='", "'<'", "'>'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "LB", "RB", "LP", "RP", "LSB", 
            "RSB", "SEMI", "COMMA", "DOT", "COLON", "TAB", "FF", "CR", "LR", 
            "BS", "CLASS", "STATIC", "FINAL", "BREAK", "CONTINUTE", "DO", 
            "ELSE", "EXTENDS", "IF", "NEW", "THEN", "FOR", "RETURN", "TRUE", 
            "FALSE", "VOID", "NIL", "THIS", "TO", "DOWNTO", "EQE", "NEQ", 
            "AND", "LET", "GET", "OR", "ADD", "SUB", "MOD", "MUL", "FDIV", 
            "IDIV", "EQ", "LT", "GT", "NOT", "CONCATE", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "LINE", "BLOCK", "INTTYPE", "FLOATYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "INTLIT", "FLOATLIT", "EXPONENT", "NUMBER", 
                  "STRINGLIT", "ESC", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                  "SEMI", "COMMA", "DOT", "COLON", "TAB", "FF", "CR", "LR", 
                  "BS", "CLASS", "STATIC", "FINAL", "BREAK", "CONTINUTE", 
                  "DO", "ELSE", "EXTENDS", "IF", "NEW", "THEN", "FOR", "RETURN", 
                  "TRUE", "FALSE", "VOID", "NIL", "THIS", "TO", "DOWNTO", 
                  "EQE", "NEQ", "AND", "LET", "GET", "OR", "ADD", "SUB", 
                  "MOD", "MUL", "FDIV", "IDIV", "EQ", "LT", "GT", "NOT", 
                  "CONCATE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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
     


