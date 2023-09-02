
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class ClassDetail:
    def __init__(self, name, parent =None, member = []):
        self.name = name        # Id
        self.parent = parent    # Id
        self.member = member    # list of AttributeDecl or MethodDecl
    def __str__(self):
        return "(" + str(self.name) +","+ str(self.parent) +","+ str(self.member) +")"

def getName(ast):
    name = None
    if type(ast) is ClassDecl:
        name = ast.classname.name
    elif type(ast) is AttributeDecl:
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
        elif type(ast.decl) is ConstDecl:
            name = ast.decl.constant.name
    elif type(ast) is MethodDecl:
        name = ast.name.name 
    elif type(ast) is VarDecl:
        name = ast.variable.name
    elif type(ast) is ConstDecl:
        name = ast.constant.name
    elif type(ast) is Id:
        name = ast.name
    elif type(ast) is ClassDetail:
        name = ast.name.name
    return name

def getType(ast):
    typ = None
    if type(ast) is VarDecl:
        typ = ast.varType
    elif type(ast) is ConstDecl:
        typ = ast.constType
    elif type(ast) is AttributeDecl:
        if type(ast.decl) is ConstDecl:
            typ = ast.decl.constType
        elif type(ast.decl) is VarDecl:
            typ = ast.decl.varType
    return typ


def checkRedeclaredMember(ast, l):
    wasDecl = [False, False]
    
    for mem in l:
        if mem is ast:
            print(mem,'---',ast)
            wasDecl[1] = True
            break
        if getName(mem) == getName(ast):
            wasDecl[0] = True
    
    if wasDecl[0] and wasDecl[1]:
        return True
    return False

def findInList(name, l):
    if type(l[0]) is AttributeDecl or type(l[0]) is MethodDecl:
        c
    for mem in l:
        if getName(mem) == name:
            return mem
    return None


class NameCheck(BaseVisitor):
    def visitProgram(self, ast, o):
        o = []    # list of ClassDetail
        for decl in ast.decl:
            o = self.visit(decl, o)

        return o
    def visitClassDecl(self, ast, o):
        # ast : ClassDecl
        # class ClassDecl(Decl):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        
        # o is list of ClassDetail
        # for decl in o:
        #     if ast.classname.name == decl.name:
        #         raise Redeclared(Class(), ast.classname.name) # throw later
            
        c = []  # list of Att or Method
        for m in ast.memlist:
            c = c + [self.visit(m, c)]
        return o + [ast]
    
    def visitAttributeDecl(self, ast, o):
        # class AttributeDecl(MemDecl):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl
        # return VarDecl or ConstDecl
        
        # o still list of ClassDetail
        # for decl in o:
        #     if getName(ast.decl) == getName(decl):
        #         raise Redeclared(Attribute(), getName(ast.decl))
        return ast
    
    # def visitVarDecl(self, ast, o):
    #     # o is list of []
    #     for decl in o:
    #         if getName(decl) == getName(ast):
    #             raise Redeclared(Variable(), ast.variable.name)
    #     return ast
    
    # def visitConstDecl(self, ast, o):
    #     # constant : Id
    #     # constType : Type
    #     # value : Expr
    #     for decl in o:
    #         if ast.constant.name == decl:
    #             raise Redeclared(Constant(), ast.constant.name)
    #     return ast
    
    def visitMethodDecl(self, ast, o):
        # class MethodDecl(MemDecl):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        
        # for decl in o:
        #     if getName(decl) == getName(ast):
        #         raise Redeclared(Method(), getName(ast))
        # param = []
        # for p in ast.param:
        #     if getName(p) in param:
        #         raise Redeclared(Parameter(), p.variable.name)
        #     param = param + [p.variable.name]
        return ast
    

class StaticChecker(BaseVisitor):
    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    ]
    # class MethodDecl(MemDecl):
    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # returnType: Type  # None for constructor
    # body: Block
    
    # class VarDecl(StoreDecl):
    # variable : Id
    # varType : Type
    # varInit : Expr = None 
    
    classProgram = [
        ClassDecl(Id('io'), None, [MethodDecl(Static(), Id('readInt'), [], IntType(), Block([],[])),
                                 MethodDecl(Static(), Id('writeIntLn'),[VarDecl(Id('anArg'),IntType())], VoidType(), Block([],[])),
                                 MethodDecl(Static(), Id('writeInt'),[VarDecl(Id('anArg'),IntType())], VoidType(), Block([],[])),
                                 ]),
    ]   
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        self.visit(self.ast, StaticChecker.classProgram)
        return ""

    def visitProgram(self, ast, c):
        # return [self.visit(x,c) for x in ast.decl]
        o = c + NameCheck().visit(ast, c)
        for decl in ast.decl:
            self.visit(decl, o)
        

    def visitClassDecl(self,ast, c): 
        # ast : ClassDecl
        # class ClassDecl(Decl):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        
        # check redeclared class
        if checkRedeclaredMember(ast, c):
            raise Redeclared(Class(), ast.classname.name)
        
        # check undeclared parent
        if ast.parentname:
            if not getName(ast.parentname) in map(lambda x: getName(x), c):
                raise Undeclared(Class(), getName(ast.parentname))
        # check member
        o = [ast, c]
        for mem in ast.memlist:
            self.visit(mem, o) # c is tuple (this class, list of ClassDeclared)
        
    
    

    def visitVarDecl(self, ast, c):
        # class VarDecl(StoreDecl):
        # variable : Id
        # varType : Type
        # varInit : Expr = None 

        # c is tuple (this method, list of ClassDeclared)
        if checkRedeclaredMember(ast, c[0].param + c[0].body.decl):
            raise Redeclared(Variable(), getName(ast))
        if ast.varInit:
            name, typ = self.visit(ast.varInit, c)           # it can be a literal or a Id
            
            if type(typ) is not type(ast.varType):
                raise TypeMismatchInStatement(ast)
            
        
    def visitConstDecl(self, ast, o):
        # class ConstDecl(StoreDecl):
        # constant : Id
        # constType : Type
        # value : Expr
        
        if checkRedeclaredMember(ast, o[0].param + o[0].body.decl):
            raise Redeclared(Constant(), getName(ast))
        
    
    def visitStatic(self, ast, param):
        return None
    
    def visitInstance(self, ast, param): 
        return None
    
    def visitMethodDecl(self, ast, o):
        # class MethodDecl(MemDecl):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        
        
        # o = (this class, list of ClassDetail)
        if checkRedeclaredMember(ast, o[0].memlist):
            raise Redeclared(Method(), getName(ast))
        
        for par in ast.param:
            if checkRedeclaredMember(par, ast.param):
                raise Redeclared(Parameter(), getName(par))
        
        o = [ast, o[1]]
        self.visit(ast.body, o)
        return ast # not yet now
    
    
    def visitAttributeDecl(self, ast, o): 
        # class AttributeDecl(MemDecl):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl
        
        # o = (this class, list of ClassDetail)
        
        if checkRedeclaredMember(ast, o[0].memlist):
            raise Redeclared(Attribute(), getName(ast.decl))
        
        self.visit(ast.decl,o)
        
        return ast # not yet now
            
    def visitIntType(self, ast, param):
        return None
    
    def visitFloatType(self, ast, param):
        return None
    
    def visitBoolType(self, ast, param):
        return None
    
    def visitStringType(self, ast, param):
        return None
    
    def visitVoidType(self, ast, param):
        return None
    
    def visitArrayType(self, ast, param):
        return None
    
    def visitClassType(self, ast, param):
        return None
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitNewExpr(self, ast, param):
        return None
    
    def visitId(self, ast, o):
        
        # class Id(LHS):
        # name:str
        # o is tuple (this method, list of ClassDeclared)
        
        id = findInList(ast.name, o)
        if id:
            return getName(id), getType(id)
        raise Undeclared(Identifier(), ast.name)
        
        
    def visitArrayCell(self, ast, param):
        return None
    
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitBlock(self, ast, o):
            #---------------------
            # decl:List[StoreDecl]
            # stmt:List[Stmt]
            #---------------------
        # o = (this class, list of ClassDetail)
        for decl in ast.decl:
            self.visit(decl, o)
        for stmt in ast.stmt:
            self.visit(stmt, o)
        return ast
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitCallStmt(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return None
    
    def visitFloatLiteral(self, ast, param):
        return None
    
    def visitBooleanLiteral(self, ast, param):
        return None
    
    def visitStringLiteral(self, ast, param):
        return None
    
    def visitNullLiteral(self, ast, param):
        return None
    
    def visitSelfLiteral(self, ast, param):
        return None 

    def visitArrayLiteral(self, ast, param):
        return None 


