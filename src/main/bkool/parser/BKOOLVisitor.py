# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylist.
    def visitArraylist(self, ctx:BKOOLParser.ArraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array.
    def visitArray(self, ctx:BKOOLParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayelement.
    def visitArrayelement(self, ctx:BKOOLParser.ArrayelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booleanlit.
    def visitBooleanlit(self, ctx:BKOOLParser.BooleanlitContext):
        return self.visitChildren(ctx)



del BKOOLParser