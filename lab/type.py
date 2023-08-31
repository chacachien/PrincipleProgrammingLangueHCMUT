#ex1
# class Type(ABC):
#     pass
# class IntType(Type):pass
# class FloatType(Type): pass
# class BoolType(Type): pass

# class StaticCheck(Visitor):

#     def visitBinOp(self,ctx:BinOp,o): 
#         l = self.visit(ctx.e1,o)
#         r = self.visit(ctx.e2,o)
#         op = ctx.op
#         if op in ['*', '+', '-']:
#             if type(l) is BoolType or type(r) is BoolType : raise TypeMismatchInExpression(ctx)
#             if type(l) is FloatType or type(r) is FloatType:
#                 return FloatType()
#             return IntType()
#         if op == '/':
#             if type(l) is BoolType or type(r) is BoolType: raise TypeMismatchInExpression(ctx)
#             return FloatType()
#         if op in ['&&', '||']:
#             if type(l) is not BoolType or type(r) is not BoolType: raise TypeMismatchInExpression(ctx)
#             return BoolType()
        
#         if op in ['>', '<', '==', '!=']:
#             if type(l)!=type(r): raise TypeMismatchInExpression(ctx)
#             return BoolType()
#     def visitUnOp(self,ctx:UnOp,o):
#         if ctx.op == '-':
#             if type(self.visit(ctx.e,o)) is BoolType: raise TypeMismatchInExpression(ctx)
#             if type(self.visit(ctx.e,o)) is FloatType:
#                 return FloatType()
#             return IntType()
#         if ctx.op == '!':
#             if type(self.visit(ctx.e,o)) is not BoolType: raise TypeMismatchInExpression(ctx)
#             return BoolType()
        
#     def visitIntLit(self,ctx:IntLit,o): 
#         return IntType()
#     def visitFloatLit(self,ctx,o): 
#         return FloatType()
#     def visitBoolLit(self,ctx,o): 
#         return BoolType()


#ex2
# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o):
#         o = []
#         for decl in ctx.decl:
#             o = self.visit(decl, o)
#         self.visit(ctx.exp, o)
#     def visitVarDecl(self,ctx:VarDecl,o): 
#         for decl in o:
#             if decl.name == ctx.name:
#                 raise RedeclaredVariable(ctx.name)
#         return o + [ctx]
#     def visitIntType(self,ctx:IntType,o): 
#         return IntType()
#     def visitFloatType(self,ctx:FloatType,o):
#         return FloatType()

#     def visitBoolType(self,ctx:BoolType,o):
#         return BoolType()

#     def visitBinOp(self,ctx:BinOp,o): 
#         l = self.visit(ctx.e1,o)
#         r = self.visit(ctx.e2,o)
#         op = ctx.op
#         if op in ['*', '+', '-']:
#             if type(l) is BoolType or type(r) is BoolType : raise TypeMismatchInExpression(ctx)
#             if type(l) is FloatType or type(r) is FloatType:
#                 return FloatType()
#             return IntType()
#         if op == '/':
#             if type(l) is BoolType or type(r) is BoolType: raise TypeMismatchInExpression(ctx)
#             return FloatType()
#         if op in ['&&', '||']:
#             if type(l) is not BoolType or type(r) is not BoolType: raise TypeMismatchInExpression(ctx)
#             return BoolType()
        
#         if op in ['>', '<', '==', '!=']:
#             if type(l)!=type(r): raise TypeMismatchInExpression(ctx)
#             return BoolType()
#     def visitUnOp(self,ctx:UnOp,o):
#         if ctx.op == '-':
#             if type(self.visit(ctx.e,o)) is BoolType: raise TypeMismatchInExpression(ctx)
#             if type(self.visit(ctx.e,o)) is FloatType:
#                 return FloatType()
#             return IntType()
#         if ctx.op == '!':
#             if type(self.visit(ctx.e,o)) is not BoolType: raise TypeMismatchInExpression(ctx)
#             return BoolType()

#     def visitIntLit(self,ctx:IntLit,o): return IntType()

#     def visitFloatLit(self,ctx,o): return FloatType()

#     def visitBoolLit(self,ctx,o): return BoolType()

#     def visitId(self,ctx,o):
#         for decl in o:
#             if decl.name == ctx.name:
#                 return decl.typ
#         raise UndeclaredIdentifier(ctx.name)

#ex3

# class Type(ABC): pass
# class IntType(Type):pass
# class FloatType(Type):pass
# class BoolType(Type):pass
# class NoType(Type): pass

# class Symbol:
#     def __init__(self, name, typ):
#         self.name = name
#         self.typ = typ
# class Utils:
#     def infer(symbolList, typ, name):
#         for sym in symbolList:
#             if sym.name == name:
#                 sym.typ = typ
#                 return typ

# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o):
#         o = []
#         for decl in ctx.decl:
#             o = self.visit(decl,o)
        
#         for stmt in ctx.stmts:
#             self.visit(stmt,o)
        
        
#     def visitVarDecl(self,ctx:VarDecl,o): 
#         return o + [Symbol(ctx.name, NoType())]
#     def visitAssign(self,ctx:Assign,o): 
#         l = self.visit(ctx.lhs, o)
#         r = self.visit(ctx.rhs, o)
#         if type(l) is NoType and type(r) is NoType:
#             raise TypeCannotBeInferred(ctx)
        
#         if type(l) is NoType:
#             l = Utils.infer(o, r, ctx.lhs.name)
#             return
#         if type(r) is NoType:
#             r = Utils.infer(o, l, ctx.rhs.name)
#             return
#         if type(l) is type(r): return
#         raise TypeMismatchInStatement(ctx)
        
        
#     def visitBinOp(self,ctx:BinOp,o): 
#         el = self.visit(ctx.e1,o)
#         er = self.visit(ctx.e2,o)
#         op = ctx.op
#         if op in ['+', '-', '*','/']:
#             if type(el) is NoType:
#                 el = Utils.infer(o, IntType(), ctx.e1.name)
                
#             if type(er) is NoType:
#                 er= Utils.infer(o, IntType(), ctx.e2.name)
                
#             if type(el) is IntType and type(er) is IntType: return IntType()
#             raise TypeMismatchInExpression(ctx)
            
    
#         if op in ['+.', '-.','*.','/.']:
#             if type(el) is NoType:
#                 el = Utils.infer(o, FloatType(), ctx.e1.name)
                
#             if type(er) is NoType:
#                 er = Utils.infer(o, FloatType(), ctx.e2.name)
                
#             if type(el)  is  FloatType and type(er) is FloatType:return FloatType()
#             raise TypeMismatchInExpression(ctx)
            

        
#         if op in ['>','=']:
#             if type(el) is NoType:
#                 el = Utils.infer(o, IntType(), ctx.e1.name)
                
#             if type(er) is NoType:
#                 er = Utils.infer(o, IntType(), ctx.e2.name)
                
#             if type(el)  is  IntType and type(er) is IntType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ctx)
#         if op in ['>.','=.']:
#             if type(el) is NoType:
#                 el = Utils.infer(o, FloatType(), ctx.e1.name)
                
#             if type(er) is NoType:
#                 er = Utils.infer(o, FloatType(), ctx.e2.name)
                
#             if type(el)  is  FloatType and type(er) is  FloatType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ctx)
#         if op in ['!','&&','||', '>b','=b']:
#             if type(el) is NoType:
#                 el = Utils.infer(o, BoolType(), ctx.e1.name)
                
#             if type(er) is NoType:
#                 er = Utils.infer(o, BoolType(), ctx.e2.name)
                
#             if type(el)  is  BoolType and type(er) is  BoolType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ctx)
#     def visitUnOp(self,ctx:UnOp,o):
#         op = ctx.op
#         ex = self.visit(ctx.e,o)
#         if op == '-':
            
#             if type(ex) is NoType:
#                 ex= Utils.infer(o, IntType(), ctx.e.name)
                
#             if type(ex) is  IntType:
#                 return IntType()
#             raise TypeMismatchInExpression(ctx)

#         if op == '-.':
            
#             if type(ex) is NoType:
#                 ex= Utils.infer(o, FloatType(), ctx.e.name)
                
#             if type(ex) is  FloatType:
#                 return FloatType()
#             raise TypeMismatchInExpression(ctx)

            
#         if op == '!':
            
#             if type(ex) is NoType:
#                 ex= Utils.infer(o, BoolType(), ctx.e.name)
#             if type(ex) is  BoolType:
#                 return BoolType()
#             raise TypeMismatchInExpression(ctx)
        
#         if op == 'i2f':
#             if type(ex) is NoType:
#                 ex= Utils.infer(o, IntType(), ctx.e.name)
                
#             if type(ex) is IntType:
#                 return FloatType()
#             raise TypeMismatchInExpression(ctx)

            
#         if op == 'floar':
#             if type(ex) is NoType:
#                 ex= Utils.infer(o, FloatType(), ctx.e.name)
                
#             if type(ex) is FloatType:
#                 return IntType()

#             raise TypeMismatchInExpression(ctx)
#     def visitIntLit(self,ctx:IntLit,o): 
#         return IntType()
#     def visitFloatLit(self,ctx,o): 
#         return FloatType()
#     def visitBoolLit(self,ctx,o): 
#         return BoolType()

#     def visitId(self,ctx,o):
#         for sym in o:
#             if sym.name == ctx.name:
#                 return sym.typ
#         raise UndeclaredIdentifier(ctx.name)

