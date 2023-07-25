#ex1 class ASTGeneration(MPVisitor):
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls())+1
        

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        if ctx.getChildCount()>0:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return 0

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) +1

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1
    
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() > 1:
            return self.visit(ctx.ids()) + 2
        else:
            return 1
        
#ex2
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls()) + 1
        
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) + 1

    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        if ctx.getChildCount()>0:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) + 1
        return 1

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1
    
    def visitIds(self,ctx:MPParser.IdsContext):
        return 1 + self.visit(ctx.ids()) if ctx.getChildCount() > 1 else 1

#ex3
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl())+self.visit(ctx.vardecltail())
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        return [] if ctx.getChildCount()==0 else self.visit(ctx.vardecl())+self.visit(ctx.vardecltail())
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x: VarDecl(x,self.visit(ctx.mptype())),self.visit(ctx.ids())))
    def visitMptype(self,ctx:MPParser.MptypeContext):

        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(ctx.ID().getText())] if ctx.getChildCount()==1 else [Id(ctx.ID().getText())]+self.visit(ctx.ids())        


#ex4 
from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda x,y: x+self.visit(y), ctx.vardecl(),[]))
    
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x: VarDecl(x,self.visit(ctx.mptype())),self.visit(ctx.ids())))
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()
    def visitIds(self,ctx:MPParser.IdsContext):
        return map(lambda x: Id(x.getText()), ctx.ID())
    
    
#ex5
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
    

    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount()==1:
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.operand())
        return Binary(ctx.ANDOR().getText(),self.visit(ctx.factor()), self.visit(ctx.operand()))
        
            

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return self.visit(ctx.exp())
        
        
#ex6
from functools import reduce
class ASTGeneration(MPVisitor):
# program: exp EOF;


# term: factor COMPARE factor | factor;

# factor: operand (ANDOR operand)*; 

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

# exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        # if ctx.getChildCount() == 1:
        #     return self.visit(ctx.term(0))
        return reduce(lambda y,x: Binary(x[1].getText(), self.visit(x[0]), y), list(zip(ctx.term(),ctx.ASSIGN()))[::-1], self.visit(ctx.term()[-1]))
        # terms = [self.visit(x) for x in ctx.term()]
        # assign = [x.getText() for x in ctx.ASSIGN()]
        # right = terms[-1]
        # for i in range(len(assign)):
        #     op = assign[len(assign)-i-1]
        #     left = terms[len(terms)-i-2]
        #     right = Binary(op, left, right)
        # return right

    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount()==1:
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
 

    def visitFactor(self,ctx:MPParser.FactorContext):
        # if ctx.getChildCount()==1:
        #     return self.visit(ctx.operand(0))
        return reduce(lambda y, x: Binary(x[0].getText(),y, self.visit(x[1])), zip(ctx.ANDOR(),ctx.operand()[1:]), self.visit(ctx.operand(0)))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return self.visit(ctx.exp())