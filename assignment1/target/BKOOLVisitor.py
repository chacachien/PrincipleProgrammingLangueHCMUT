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


    # Visit a parse tree produced by BKOOLParser#bkool.
    def visitBkool(self, ctx:BKOOLParser.BkoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listmember.
    def visitListmember(self, ctx:BKOOLParser.ListmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listmemberprime.
    def visitListmemberprime(self, ctx:BKOOLParser.ListmemberprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableatt.
    def visitMutableatt(self, ctx:BKOOLParser.MutableattContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableatt.
    def visitImmutableatt(self, ctx:BKOOLParser.ImmutableattContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listatt.
    def visitListatt(self, ctx:BKOOLParser.ListattContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributename.
    def visitAttributename(self, ctx:BKOOLParser.AttributenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listparameter.
    def visitListparameter(self, ctx:BKOOLParser.ListparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listparameterprime.
    def visitListparameterprime(self, ctx:BKOOLParser.ListparameterprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paradecl.
    def visitParadecl(self, ctx:BKOOLParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstatement.
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listblock.
    def visitListblock(self, ctx:BKOOLParser.ListblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockdecllist.
    def visitBlockdecllist(self, ctx:BKOOLParser.BlockdecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockdeclprime.
    def visitBlockdeclprime(self, ctx:BKOOLParser.BlockdeclprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockbodylist.
    def visitBlockbodylist(self, ctx:BKOOLParser.BlockbodylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockbodyprime.
    def visitBlockbodyprime(self, ctx:BKOOLParser.BlockbodyprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockdecl.
    def visitBlockdecl(self, ctx:BKOOLParser.BlockdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignmentstatement.
    def visitAssignmentstatement(self, ctx:BKOOLParser.AssignmentstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstatement.
    def visitIfstatement(self, ctx:BKOOLParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstatement.
    def visitForstatement(self, ctx:BKOOLParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstatment.
    def visitBreakstatment(self, ctx:BKOOLParser.BreakstatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continuestatement.
    def visitContinuestatement(self, ctx:BKOOLParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstatement.
    def visitReturnstatement(self, ctx:BKOOLParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodinvocationstatement.
    def visitMethodinvocationstatement(self, ctx:BKOOLParser.MethodinvocationstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression.
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberaccess.
    def visitMemberaccess(self, ctx:BKOOLParser.MemberaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instanceattributeaccess.
    def visitInstanceattributeaccess(self, ctx:BKOOLParser.InstanceattributeaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#staticattributeaccess.
    def visitStaticattributeaccess(self, ctx:BKOOLParser.StaticattributeaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instancemethodinvocation.
    def visitInstancemethodinvocation(self, ctx:BKOOLParser.InstancemethodinvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#staticmethodinvocation.
    def visitStaticmethodinvocation(self, ctx:BKOOLParser.StaticmethodinvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodinvocation.
    def visitMethodinvocation(self, ctx:BKOOLParser.MethodinvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listexpression.
    def visitListexpression(self, ctx:BKOOLParser.ListexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expressionprime.
    def visitExpressionprime(self, ctx:BKOOLParser.ExpressionprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexexpression.
    def visitIndexexpression(self, ctx:BKOOLParser.IndexexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classcreate.
    def visitClasscreate(self, ctx:BKOOLParser.ClasscreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylit.
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array.
    def visitArray(self, ctx:BKOOLParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayelement.
    def visitArrayelement(self, ctx:BKOOLParser.ArrayelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#intoperator.
    def visitIntoperator(self, ctx:BKOOLParser.IntoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#floatoperator.
    def visitFloatoperator(self, ctx:BKOOLParser.FloatoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booloperator.
    def visitBooloperator(self, ctx:BKOOLParser.BooloperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stringoperator.
    def visitStringoperator(self, ctx:BKOOLParser.StringoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytyp.
    def visitArraytyp(self, ctx:BKOOLParser.ArraytypContext):
        return self.visitChildren(ctx)



del BKOOLParser