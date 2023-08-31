
#ex1
# class StaticCheck(Visitor):

#     def visitProgram(self,ctx:Program,o:object): 
#         o = [[]]
#         for decl in ctx.decl:
#             o = self.visit(decl,o)
#     def visitClassDecl(self,ctx:ClassDecl,o:object):
#         c = []
#         for m in ctx.mem:
#             c = self.visit(m,c)
#         return o + c
#     def visitVarDecl(self,ctx:VarDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredField(ctx.name)
#         return o + [ctx.name]
#     def visitFuncDecl(self,ctx:FuncDecl,o:object):
#         if ctx.name in o:
#             raise RedeclaredMethod(ctx.name)
#         return o + [ctx.name]
#     def visitIntType(self,ctx:IntType,o:object):
#         pass

#     def visitFloatType(self,ctx:FloatType,o:object): pass

#     def visitClassType(self,ctx:ClassType,o:object): pass

#     def visitIntLit(self,ctx:IntLit,o:object):pass

#     def visitId(self,ctx:Id,o:object):pass

#     def visitFieldAccess(self,ctx:FieldAccess,o:object): pass
    
    
    
#ex2 and ex3


class NameCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o = self.visit(decl,o)
        return o
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        c = []
        for m in ctx.mem:
            c = self.visit(m,c)
        return o + [(ctx.name, ctx.parent, c)]
    def visitVarDecl(self,ctx:VarDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        return o + [ctx]

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object): 
        o = NameCheck().visit(ctx, o)
        for decl in ctx.decl:
            self.visit(decl,o)
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        
        for m in ctx.mem:
            self.visit(m,o) if type(m) is FuncDecl else None
        
    def visitVarDecl(self,ctx:VarDecl,o:object): pass
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        local = ctx.param + ctx.body[0]
        for expr in ctx.body[1]:
            self.visit(expr, (local,o))
        
    def visitIntType(self,ctx:IntType,o:object): IntType()

    def visitFloatType(self,ctx:FloatType,o:object): FloatType()

    def visitClassType(self,ctx:ClassType,o:object): ClassType()

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        for decl in o[0]:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)

    # m.a
    def visitFieldAccess(self,ctx:FieldAccess,o:object): 
        typ = self.visit(ctx.exp,o)
        
        if type(typ) is ClassType:
            infor = None
            f = False
            father = ""
            # find m
            for decl in o[1]:
                if decl[0]==typ.name:
                    infor = decl
                    f = True
                    father = decl[1]
                    break
                
            if not f: raise UndeclaredClass(typ.name)
            
            
            # find a
            for decl in o[1]:
                for mem in infor[2]:
                    if mem.name == ctx.field:
                        return mem.typ
                if father != "":
                    for x in o[1]:
                        if father == x[0]:
                            infor = x
                            father = x[1]
            raise UndeclaredField(ctx.field)
        