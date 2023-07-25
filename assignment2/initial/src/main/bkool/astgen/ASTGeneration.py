from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    #   program: bkool EOF;
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.bkool()))

    # Visit a parse tree produced by BKOOLParser#bkool.
    #   bkool: classdecl bkool | classdecl;
    #   return a list of classdecl
    def visitBkool(self, ctx:BKOOLParser.BkoolContext):
        if ctx.getChildCount() ==1:
            return [self.visit(ctx.classdecl())]
        else:
            return [self.visit(ctx.classdecl())] + self.visit(ctx.bkool())


    # Visit a parse tree produced by BKOOLParser#classdecl.
    #   classdecl: CLASS ID (EXTENDS ID)? LP listmember RP;
    #   return a ClassDecl object
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        if ctx.getChildCount() == 5:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.listmember()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.listmember()), Id(ctx.ID(1).getText()))
        
    # Visit a parse tree produced by BKOOLParser#listmember.
    #   listmember: listmemberprime |;
    def visitListmember(self, ctx:BKOOLParser.ListmemberContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.listmemberprime())


    # Visit a parse tree produced by BKOOLParser#listmemberprime.
    #   listmemberprime: member listmemberprime | member;
    #   return a list of member
    def visitListmemberprime(self, ctx:BKOOLParser.ListmemberprimeContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.member())
        else:
            return self.visit(ctx.member()) + self.visit(ctx.listmemberprime())


    # Visit a parse tree produced by BKOOLParser#member.
    #   member: attribute
	# 	        | method
	# 	        | constructor;
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    #   attribute: (mutableatt|immutableatt) SEMI;
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by BKOOLParser#mutableatt.
    #   mutableatt: (STATIC)? typ listattmu;
    def visitMutableatt(self, ctx:BKOOLParser.MutableattContext):
        if ctx.getChildCount()==3:
            return list(map(lambda x: AttributeDecl(Static(), VarDecl(x[0], self.visit(ctx.typ()), x[1])), self.visit(ctx.listattmu())))
        else:
            return list(map(lambda x: AttributeDecl(Instance(), VarDecl(x[0], self.visit(ctx.typ()), x[1])), self.visit(ctx.listattmu())))
    # Visit a parse tree produced by BKOOLParser#listattmu.
    #   listattmu: attributenamemu COMMA listattmu | attributenamemu;
    def visitListattmu(self,ctx:BKOOLParser.ListattmuContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.attributenamemu())]
        else:
            return [self.visit(ctx.attributenamemu())] + self.visit(ctx.listattmu())
    #   attributenamemu: ID (EQ expression)?;
    def visitAttributenamemu(self,ctx:BKOOLParser.AttributenamemuContext):
        if ctx.getChildCount()==1:
            return (Id(ctx.ID().getText()), None)
        else:
            return (Id(ctx.ID().getText()), self.visit(ctx.expression()))   
    # Visit a parse tree produced by BKOOLParser#immutableatt.
    #immutableatt: FINAL (STATIC)? typ listatt
	#              | (STATIC)? FINAL typ listatt;
    def visitImmutableatt(self, ctx:BKOOLParser.ImmutableattContext):
        if ctx.getChildCount()==4:
            return map(lambda x: AttributeDecl(Static(),ConstDecl(x[0],self.visit(ctx.typ()),x[1])), self.visit(ctx.listatt()) )
        else:
            return map(lambda x: AttributeDecl(Instance(),ConstDecl(x[0],self.visit(ctx.typ()),x[1])), self.visit(ctx.listatt()) )


    # Visit a parse tree produced by BKOOLParser#listatt.
    #    listatt: attributename COMMA listatt | attributename;
    def visitListatt(self, ctx:BKOOLParser.ListattContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.attributename())]
        else:
            return [self.visit(ctx.attributename())] + self.visit(ctx.listatt())


    # Visit a parse tree produced by BKOOLParser#attributename.
    #   attributename: ID EQ expression;
    def visitAttributename(self, ctx:BKOOLParser.AttributenameContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by BKOOLParser#method.
    #       method: STATIC? typ ID LB listparameter RB blockstatement;
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return 'method'


    # Visit a parse tree produced by BKOOLParser#listparameter.
    #       listparameter: listparameterprime | ;
    def visitListparameter(self, ctx:BKOOLParser.ListparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listparameterprime.
    #       listparameterprime: paradecl SEMI listparameterprime | paradecl;
    def visitListparameterprime(self, ctx:BKOOLParser.ListparameterprimeContext):
        pass


    # Visit a parse tree produced by BKOOLParser#paradecl.
    #       paradecl: typ idlist;
    def visitParadecl(self, ctx:BKOOLParser.ParadeclContext):
        return list(map(lambda x: VarDecl(x, self.visit(ctx.typ())), self.visit(ctx.idlist())))

    # Visit a parse tree produced by BKOOLParser#idlist.
    #       idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        if ctx.getChildCount()==1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return 'constructor'


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
        return 'e'


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
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATYPE():
            return FloatType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.VOIDTYPE():
            return VoidType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.arraytyp())


    # Visit a parse tree produced by BKOOLParser#arraytyp.
    def visitArraytyp(self, ctx:BKOOLParser.ArraytypContext):
        if ctx.INTTYPE():
            return ArrayType(int(ctx.INTLIT().getText()),IntType())
        elif ctx.FLOATYPE():
            return ArrayType(int(ctx.INTLIT().getText()),FloatType())
        elif ctx.BOOLEANTYPE():
            return ArrayType(int(ctx.INTLIT().getText()),BoolType())
        elif ctx.STRINGTYPE():
            return ArrayType(int(ctx.INTLIT().getText()),StringType())
        elif ctx.ID():
            return ArrayType(int(ctx.INTLIT().getText()),ClassType(Id(ctx.ID().getText())))
            