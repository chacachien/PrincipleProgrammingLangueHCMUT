from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

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
    #       return a list of MemberDecl
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#attribute.
    #   attribute: (mutableatt|immutableatt) SEMI;
    #       return a list of AttributeDecl
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visit(ctx.getChild(0))          

    # Visit a parse tree produced by BKOOLParser#mutableatt.
    #   mutableatt: (STATIC)? typ listattmu;
    def visitMutableatt(self, ctx:BKOOLParser.MutableattContext):
        if ctx.getChildCount()==3:
            return list(map(lambda x: AttributeDecl(Static(), VarDecl(x[0], self.visit(ctx.typ()), x[1])), self.visit(ctx.listatt())))
        else:
            return list(map(lambda x: AttributeDecl(Instance(), VarDecl(x[0], self.visit(ctx.typ()), x[1])), self.visit(ctx.listatt())))
    
    # Visit a parse tree produced by BKOOLParser#immutableatt.
    #immutableatt: FINAL (STATIC)? typ listatt
	#              | (STATIC)? FINAL typ listatt;
    def visitImmutableatt(self, ctx:BKOOLParser.ImmutableattContext):
        if ctx.getChildCount()==4:
            return list(map(lambda x: AttributeDecl(Static(),ConstDecl(x[0],self.visit(ctx.typ()),x[1])), self.visit(ctx.listatt()) ))
        else:
            return list(map(lambda x: AttributeDecl(Instance(),ConstDecl(x[0],self.visit(ctx.typ()),x[1])), self.visit(ctx.listatt()) ))

    # Visit a parse tree produced by BKOOLParser#listatt.
    #    listatt: attributename COMMA listatt | attributename;
    def visitListatt(self, ctx:BKOOLParser.ListattContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.attributename())]
        else:
            return [self.visit(ctx.attributename())] + self.visit(ctx.listatt())

    # Visit a parse tree produced by BKOOLParser#attributename.
    #   attributename: ID (EQ expression)?;
    def visitAttributename(self, ctx:BKOOLParser.AttributenameContext):
        if ctx.getChildCount()==1:
            return (Id(ctx.ID().getText()), None)
        return (Id(ctx.ID().getText()), self.visit(ctx.expression()))

    # Visit a parse tree produced by BKOOLParser#method.
    #       method: STATIC? typ ID LB listparameter RB blockstatement;
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        if ctx.ID().getText()=="main":
            return [MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.listparameter()), self.visit(ctx.typ()), self.visit(ctx.blockstatement()))]
        if ctx.STATIC():
            return [MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.listparameter()), self.visit(ctx.typ()), self.visit(ctx.blockstatement()))]
        else:
            return [MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.listparameter()), self.visit(ctx.typ()), self.visit(ctx.blockstatement()))]
    
    # Visit a parse tree produced by BKOOLParser#listparameter.
    #       listparameter: listparameterprime | ;
    def visitListparameter(self, ctx:BKOOLParser.ListparameterContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.listparameterprime())

    # Visit a parse tree produced by BKOOLParser#listparameterprime.
    #       listparameterprime: paradecl SEMI listparameterprime | paradecl;
    #       return a list of VarDecl
    #       (float a,b; int c; string d,e)
    def visitListparameterprime(self, ctx:BKOOLParser.ListparameterprimeContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.paradecl()) # this is a list of VarDecl
        else:
            return self.visit(ctx.paradecl()) + self.visit(ctx.listparameterprime())

    # Visit a parse tree produced by BKOOLParser#paradecl.
    #       paradecl: typ idlist;
    #           return a list of VarDecl
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
    #       constructor: STATIC? ID LB listparameter RB blockstatement;
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        if ctx.STATIC():
            return [MethodDecl(Static(), Id("<init>"), self.visit(ctx.listparameter()),None ,self.visit(ctx.blockstatement()))]
        else:
            return [MethodDecl(Instance(), Id("<init>"), self.visit(ctx.listparameter()),None,self.visit(ctx.blockstatement()))]

    # Visit a parse tree produced by BKOOLParser#statement.
    #       statement:....
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#blockstatement.
    #       blockstatement: LP listblock RP;
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return Block(self.visit(ctx.listblock())[0], self.visit(ctx.listblock())[1])

    # Visit a parse tree produced by BKOOLParser#listblock.
    #       listblock: blockdecllist blockbodylist;
    ##      return a tuple of list of VarDecl and list of Stmt
    def visitListblock(self, ctx:BKOOLParser.ListblockContext):
        return (self.visit(ctx.blockdecllist()), self.visit(ctx.blockbodylist()))

    # Visit a parse tree produced by BKOOLParser#blockdecllist.
    #       blockdecllist: blockdeclprime| ;
    #       return a list of VarDecl
    def visitBlockdecllist(self, ctx:BKOOLParser.BlockdecllistContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.blockdeclprime())

    # Visit a parse tree produced by BKOOLParser#blockdeclprime.
    #   `   blockdeclprime: blockdecl blockdeclprime| blockdecl;
    def visitBlockdeclprime(self, ctx:BKOOLParser.BlockdeclprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.blockdecl())
        else:
            return self.visit(ctx.blockdecl()) + self.visit(ctx.blockdeclprime())
        
    # Visit a parse tree produced by BKOOLParser#blockbodylist.
    #      blockbodylist: blockbodyprime | ;
    def visitBlockbodylist(self, ctx:BKOOLParser.BlockbodylistContext):
        return self.visit(ctx.blockbodyprime()) if ctx.getChildCount() == 1 else []

    # Visit a parse tree produced by BKOOLParser#blockbodyprime.
    #       blockbodyprime: statement blockbodyprime | statement;
    def visitBlockbodyprime(self, ctx:BKOOLParser.BlockbodyprimeContext):
        return [self.visit(ctx.statement())] if ctx.getChildCount() == 1 else [self.visit(ctx.statement())] + self.visit(ctx.blockbodyprime())

    # Visit a parse tree produced by BKOOLParser#blockdecl.
    #       blockdecl: vardecl|vardeclmu SEMI; //all of them
    def visitBlockdecl(self, ctx:BKOOLParser.BlockdeclContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by BKOOLParser#vardecl.
    #       vardecl: FINAL? typ listatt;
    #       return a list of ConstDecl
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return list(map(lambda x: ConstDecl(x[0], self.visit(ctx.typ()), x[1]) if ctx.FINAL() else VarDecl(x[0], self.visit(ctx.typ()), x[1]), self.visit(ctx.listatt())))
       
    # Visit a parse tree produced by BKOOLParser#assignmentstatement.
    #       assignmentstatement: lhs ASSIGN expression SEMI;
    def visitAssignmentstatement(self, ctx:BKOOLParser.AssignmentstatementContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))

    # Visit a parse tree produced by BKOOLParser#lhs.
    #       lhs: indexexpression | ID | instanceattributeaccess|staticattributeaccess; 
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.getChild(0))

    # Visit a parse tree produced by BKOOLParser#ifstatement.
    #       ifstatement: IF expression THEN statement (ELSE statement)?; 
    def visitIfstatement(self, ctx:BKOOLParser.IfstatementContext):
        return If(self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1))) if ctx.ELSE() else If(self.visit(ctx.expression()), self.visit(ctx.statement(0)))

    # Visit a parse tree produced by BKOOLParser#forstatement.
    #       forstatement: FOR ID ASSIGN expression (TO | DOWNTO) expression DO statement; //interger
    def visitForstatement(self, ctx:BKOOLParser.ForstatementContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)),bool(ctx.TO()), self.visit(ctx.statement()))

    # Visit a parse tree produced by BKOOLParser#breakstatment.
    def visitBreakstatment(self, ctx:BKOOLParser.BreakstatmentContext):
        return Break()

    # Visit a parse tree produced by BKOOLParser#continuestatement.
    def visitContinuestatement(self, ctx:BKOOLParser.ContinuestatementContext):
        return Continue()

    # Visit a parse tree produced by BKOOLParser#returnstatement.
    #       returnstatement: RETURN expression SEMI;
    def visitReturnstatement(self, ctx:BKOOLParser.ReturnstatementContext):
        return Return(self.visit(ctx.expression()))

    # Visit a parse tree produced by BKOOLParser#methodinvocationstatement.
    #       methodinvocationstatement: (instancemethodinvocation|staticmethodinvocation) SEMI
    def visitMethodinvocationstatement(self, ctx:BKOOLParser.MethodinvocationstatementContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by BKOOLParser#expression.
    #       exp1 LT exp1| exp1 GT exp1| exp1 LET exp1| exp1 GET exp1| exp1;
    #       return a BinaryOp or UnaryOp
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)
        
    # Visit a parse tree produced by BKOOLParser#exp1.
    #       exp1: exp2 EQE exp2| exp2 NEQ exp2| exp2;
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    # Visit a parse tree produced by BKOOLParser#exp2.
    #       exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    # Visit a parse tree produced by BKOOLParser#exp3.
    #       exp3: exp3 ADD exp4 | exp3 SUB exp4| exp4;
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    # Visit a parse tree produced by BKOOLParser#exp4.
    #       exp4: exp4 MUL exp5 | exp4 FDIV exp5| exp4 IDIV exp5| exp4 MOD exp5| exp5;
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp5())
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    # Visit a parse tree produced by BKOOLParser#exp5.
    #       exp5: exp5 CONCATE exp6| exp6;
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp6())
        else:
            left = self.visit(ctx.exp5())
            right = self.visit(ctx.exp6())
            return BinaryOp(ctx.getChild(1).getText(), left, right)

    # Visit a parse tree produced by BKOOLParser#exp6.
    #       exp6: NOT exp6 | exp7; //hmmm
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))

    # Visit a parse tree produced by BKOOLParser#exp7.
    #       exp7: ADD exp7| SUB exp7 | exp8  ;
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp8())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7()))

    # Visit a parse tree produced by BKOOLParser#exp8.
    #       exp8: exp9 LSB expression RSB | exp9 ; //test later
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp9())
        else:
            return ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.expression()))
            
    # Visit a parse tree produced by BKOOLParser#exp9.
    #       exp9: exp9 DOT (ID |methodinvocation) | exp10; 
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp10())
        else:
            return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText())) if ctx.ID() else CallExpr(self.visit(ctx.exp9()), self.visit(ctx.methodinvocation())[0], self.visit(ctx.methodinvocation())[1])


    # Visit a parse tree produced by BKOOLParser#exp10.
    #       exp10: classcreate | exp11;
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by BKOOLParser#exp11.
    #       exp11: LB expression RB | ID | THIS |IO | NIL |literal;
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.THIS():
                return SelfLiteral()
            elif ctx.IO():
                return Id(ctx.IO().getText()) # hmmmmmmm
            elif ctx.NIL():
                return NullLiteral()
            else:
                return self.visit(ctx.literal())

    # Visit a parse tree produced by BKOOLParser#instanceattributeaccess.
    #       instanceattributeaccess: expression DOT ID; 
    def visitInstanceattributeaccess(self, ctx:BKOOLParser.InstanceattributeaccessContext):
        return FieldAccess(self.visit(ctx.expression()), Id(ctx.ID().getText()))

    # Visit a parse tree produced by BKOOLParser#staticattributeaccess.
    #       staticattributeaccess: ID DOT ID;
    def visitStaticattributeaccess(self, ctx:BKOOLParser.StaticattributeaccessContext):
        return FieldAccess(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()))

    # Visit a parse tree produced by BKOOLParser#instancemethodinvocation.
    #       instancemethodinvocation: expression DOT methodinvocation;
    def visitInstancemethodinvocation(self, ctx:BKOOLParser.InstancemethodinvocationContext):
        return CallStmt(self.visit(ctx.expression()), self.visit(ctx.methodinvocation())[0], self.visit(ctx.methodinvocation())[1])

    # Visit a parse tree produced by BKOOLParser#staticmethodinvocation.
    #       staticmethodinvocation: ID DOT methodinvocation; 
    def visitStaticmethodinvocation(self, ctx:BKOOLParser.StaticmethodinvocationContext):
        return CallStmt(Id(ctx.ID(0).getText()), self.visit(ctx.methodinvocation())[0], self.visit(ctx.methodinvocation())[1])

    # Visit a parse tree produced by BKOOLParser#methodinvocation.
    #       methodinvocation: ID LB listexpression RB;
    def visitMethodinvocation(self, ctx:BKOOLParser.MethodinvocationContext):
        return Id(ctx.ID().getText()), self.visit(ctx.listexpression())

    # Visit a parse tree produced by BKOOLParser#listexpression.
    #       listexpression: expressionprime | ;
    #       return a list of expression
    def visitListexpression(self, ctx:BKOOLParser.ListexpressionContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.expressionprime())

    # Visit a parse tree produced by BKOOLParser#expressionprime.
    #       expressionprime: expression COMMA expressionprime | expression;
    def visitExpressionprime(self, ctx:BKOOLParser.ExpressionprimeContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.expressionprime())

    # Visit a parse tree produced by BKOOLParser#literal.
    #       literal: INTLIT | FLOATLIT | BOOLIT | STRINGLIT|arraylit;
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText()=="true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.arraylit())

    # Visit a parse tree produced by BKOOLParser#indexexpression.
    #          indexexpression: exp9 LSB expression RSB;
    def visitIndexexpression(self, ctx:BKOOLParser.IndexexpressionContext):
        return ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.expression()))

    # Visit a parse tree produced by BKOOLParser#classcreate.
    #       classcreate: NEW ID LB listexpression RB;
    def visitClasscreate(self, ctx:BKOOLParser.ClasscreateContext):
        return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.listexpression()))

    # Visit a parse tree produced by BKOOLParser#arraylit.
    #       arraylit: LP array RP;
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.array()))

    # Visit a parse tree produced by BKOOLParser#array.
    #       array: arrayelement COMMA array | arrayelement;
    def visitArray(self, ctx:BKOOLParser.ArrayContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.arrayelement())]
        else:
            return [self.visit(ctx.arrayelement())] + self.visit(ctx.array())

    # Visit a parse tree produced by BKOOLParser#arrayelement.
    #       arrayelement: INTLIT | FLOATLIT | BOOLIT | STRINGLIT;
    def visitArrayelement(self, ctx:BKOOLParser.ArrayelementContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText()=="true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())

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