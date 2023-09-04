
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
    def __init__(self,name,mtype,isFinal, static, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isFinal = isFinal
        self.static = static

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
    elif type(ast) is Symbol:
        name = ast.name
    
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
    elif type(ast) is Symbol:
        typ = ast.mtype
    elif type(ast) is ClassDecl:
        typ = ClassType(ast.classname)
        
    return typ


def checkRedeclaredMember(ast, l):
    wasDecl = [False, False]
    for mem in l:
        if mem is ast:
            
            wasDecl[1] = True
            break
        if getName(mem) == getName(ast):
            wasDecl[0] = True
    
    if wasDecl[0] and wasDecl[1]:
        return True
    return False

def findInList(name, l):
    for mem in l:
        if getName(mem) == name:
            return mem
    return None

def findField(name, thisO, o):
    fatherC = findInList(thisO, o)
    while fatherC:
        infor = findInList(name, fatherC.memlist)
        if infor:
            return infor
        fatherO = fatherC.parentname
        fatherC = findInList(getName(fatherO), o)
    return None

def checkCoerTypeAssign(lhs, rhs):
    if type(lhs) is type(rhs):
        return type(lhs)
    elif type(lhs) is IntType:
        if type(rhs) is IntType:
            return IntType()
    elif type(lhs) is FloatType:
        if type(rhs) in [FloatType, IntType]:
            
            return FloatType()
    elif type(lhs) is BoolType:
        if type(rhs) is BoolType:
            return BoolType()
        
    return False

def checkCoerTypeExp(lhs, rhs):
    if type(lhs) is type(rhs):
        return type(lhs)
    elif type(lhs) is FloatType or type(rhs) is FloatType:
        return FloatType()
    return False

def checkIsChild(child, parent, o):
    # child and parent is String
    # o is list of ClassDecl
    if child == parent:
        return True
    for decl in o:
        if decl.classname.name == child:
            if decl.parentname:
                return checkIsChild(decl.parentname.name, parent, o)
            else:
                return False
    
    


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
            
        c = []  # list of Att or Method
        for m in ast.memlist:
            c = c + [self.visit(m, c)]
        return o + [ast]
    
    def visitAttributeDecl(self, ast, o):
        # class AttributeDecl(MemDecl):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl
        # return VarDecl or ConstDecl

        return ast

    
    def visitMethodDecl(self, ast, o):

        return ast
    

class StaticChecker(BaseVisitor):
    # global_envi = [
    # Symbol("getInt",MType([],IntType())),
    # Symbol("putIntLn",MType([IntType()],VoidType())),
    # ]

    
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
        o = [ast, c, []]
        for mem in ast.memlist:
            self.visit(mem, o) # c is tuple (this class, list of ClassDeclared)
        
    def visitVarDecl(self, ast, c):
        # class VarDecl(StoreDecl):
        # variable : Id
        # varType : Type
        # varInit : Expr = None 
        
        if type(c[0]) is MethodDecl:
        # c is tuple (this method, list of ClassDeclared, this class)
            if checkRedeclaredMember(ast, c[0].param + c[0].body.decl):
                raise Redeclared(Variable(), getName(ast))
            
            vartyp = self.visit(ast.varType, c)
            if type(vartyp) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(vartyp) is ClassType:
                if not findInList(vartyp.classname.name, c[1]):
                    raise Undeclared(Class(), vartyp.classname.name)
                    
            if ast.varInit:
                typ = self.visit(ast.varInit, c)                  # Symbol 
                    
                if type(typ.mtype) in [IntType, FloatType]:
                    coer = checkCoerTypeAssign(ast.varType, typ.mtype)
                    if not coer:
                        raise TypeMismatchInStatement(ast)
                    else:
                        rhs = findInList(ast.varInit, c[0].param + c[0].body.decl)
                        if type(rhs) is VarDecl:
                            rhs.varType = coer
                        elif type(rhs) is ConstDecl:
                            rhs.constType = coer
                else:
                    if not type(ast.varType) is type(typ.mtype):
                        raise TypeMismatchInStatement(ast)
                    
        elif type(c[0]) is ClassDecl:
            pass
        return Symbol(getName(ast), ast.varType, False, None, ast.varInit)
        
    def visitConstDecl(self, ast, c):
        # class ConstDecl(StoreDecl):
        # constant : Id
        # constType : Type
        # value : Expr
    
        if type(c[0]) is MethodDecl:
        # c is tuple (this method, list of ClassDeclared, this class)
            if checkRedeclaredMember(ast, c[0].param + c[0].body.decl):
                raise Redeclared(Constant(), getName(ast))
            
            vartyp = self.visit(ast.constType, c)
            if type(vartyp) is VoidType:
                raise TypeMismatchInConstant(ast)
            if type(vartyp) is ClassType:
                if not findInList(vartyp.classname.name, c[1]):
                    raise Undeclared(Class(), vartyp.classname.name)
                    
            if ast.value:
                typ = self.visit(ast.value, c)                  # literal, type
                # if not typ:
                #     raise Undeclared(Identifier(), getName(ast.value))
                
                if type(typ.mtype) in [IntType, FloatType]:
                    coer = checkCoerTypeAssign(ast.constType, typ.mtype)
                    if not coer:
                        raise TypeMismatchInConstant(ast)
                    else:
                        rhs = findInList(ast.value, c[0].param + c[0].body.decl)
                        # change type of rhs
                        if type(rhs) is VarDecl:
                            rhs.varType = coer
                        elif type(rhs) is ConstDecl:
                            rhs.constType = coer
                else:
                    if not type(ast.constType) is type(typ.mtype):
                        raise TypeMismatchInConstant(ast)
                if typ.value is None:
                    raise IllegalConstantExpression(ast.value)                
            else:
                raise IllegalConstantExpression(None)
        elif type(c[0]) is ClassDecl:
            pass
        
        return Symbol(getName(ast), ast.constType, False, None, ast.value)
        
    def visitStatic(self, ast, param):
        return Static()
    
    def visitInstance(self, ast, param): 
        return Instance()
    
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
        
        o = [ast, o[1], o[0]]
        self.visit(ast.body, o)
        
        return ast # not yet now
    
    
    def visitAttributeDecl(self, ast, o): 
        # class AttributeDecl(MemDecl):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl
        
        # o = (this class, list of ClassDetail)
        #if type(ast.decl.)
        
        decl = self.visit(ast.decl, o)  # decl is a Symbol (name, mtype, value) 
        if type(decl.mtype) is ClassType:
            if not findInList(decl.mtype.classname.name, o[1]):
                raise Undeclared(Class(), decl.mtype.classname.name)

        if checkRedeclaredMember(ast, o[0].memlist):
            raise Redeclared(Attribute(), getName(ast.decl))
        
        final = False
        if type(ast.decl) is VarDecl:
            if type(ast.decl.varInit) is Id:
                raise TypeMismatchInStatement(ast)
        
        elif type(ast.decl) is ConstDecl:
            if type(ast.decl.value) is Id:
                raise TypeMismatchInStatement(ast)
            final = True
            
        lhs = self.visit(decl.mtype, o)  # lhs is a Type
        
        if decl.value:
            rhs = self.visit(decl.value, o) # rhs is a SYmbol
            
            if type(rhs.mtype) is ClassType and type(lhs) is ClassType:
                if not findInList(rhs.name, o[1]):
                    raise Undeclared(Class(), getName(rhs))
                if not checkIsChild(rhs.name, lhs.classname.name, o[1]):
                    raise TypeMismatchInStatement(ast)
            elif not checkCoerTypeAssign(lhs, rhs.mtype):
                raise TypeMismatchInStatement(ast)
        return Symbol(getName(ast), lhs, final, self.visit(ast.kind, o), decl.value)

        #return o # not yet now
            
    
    def visitArrayType(self, ast, param):
        # class ArrayType(Type):
        # size : int
        # eleType:Type
        return ArrayType(ast.size, self.visit(ast.eleType, param))
    
    def visitBinaryOp(self, ast, o):
        # class BinaryOp(Expr):
        # op:str
        # left:Expr
        # right:Expr
        l = self.visit(ast.left, o)

        r = self.visit(ast.right, o)

        v = True if l.value and r.value else None
        op = ast.op
        if op in ['+','-','*']:
            if type(l.mtype) in [IntType, FloatType] and type(r.mtype) in [IntType, FloatType]:
                if type(l.mtype) is FloatType or type(r.mtype) is FloatType:
                    return Symbol(None, FloatType(), True, v)
                else:
                    return Symbol(None, IntType(), True, v)

        if op in ['%','\\']:
            if type(l.mtype) is IntType and type(r.mtype) is IntType:
                return Symbol(None, IntType(), True, v)
            else:
                raise TypeMismatchInExpression(ast)
        if op in ['/']:
            if type(l.mtype) in [IntType, FloatType] and type(r.mtype) in [IntType, FloatType]:
                return Symbol(None, FloatType(), True, v)
            else:
                raise TypeMismatchInExpression(ast)
        
        
        
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, o):
        # class CallExpr(Expr):
        # obj: Expr
        # method:Id
        # param:List[Expr]
        
        # o = (classDecl, list of ClassDecl)
        oname, otype = self.visit(ast.obj, o)  # ob is a Type
        if not type(otype) is ClassType:
            raise TypeMismatchInExpression(ast)
        
        fatherO = o[0].classname
        fatherC = list(filter(lambda x: x.name == fatherO, o[1]))[0]
        flag = False
        infor = None
        while fatherO:
            if findInList(oname, fatherC):
                flag = True
                infor = fatherC
                break
            fatherO = fatherC.parentname
            fatherC = list(filter(lambda x: x.name == fatherO, o[1]))[0]
        if not flag:
            raise Undeclared(Class(), oname)
        
        if not type(infor) is type(otype):
            raise TypeMismatchInExpression(ast)
            
            
        
            
    
        
    
    def visitNewExpr(self, ast, o):
        
        # class NewExpr(Expr):
        # classname:Id
        # param:List[Expr]
        
        # o = (this class, list of ClassDetail) 
        [self.visit(x,o) for x in ast.param]        #handle later 
        return Symbol(ast.classname.name, ClassType(ast.classname), False, None) 
    
    def visitId(self, ast, o):
        
        # class Id(LHS):
        # name:str
        # o is tuple (this method, list of ClassDeclared)
        # or o is tuple (this class, list of ClassDetail)
        id = None
        flag = False
        if type(o[0]) is MethodDecl:
            id = findInList(ast.name, o[0].param + o[0].body.decl)
            if id:
                flag = True
        if not flag:
            id = findInList(ast.name, o[1])
            if id:
                return Symbol(getName(id), id, False,None) # this is a ClassDeclare
            raise Undeclared(Identifier(), ast.name)
        else:
            if type(id) is VarDecl:
                return Symbol(getName(id), getType(id), False, None, id.varInit)     # this is a VarDeclare or ConstDeclare
            elif type(id) is ConstDecl:
                return Symbol(getName(id), getType(id), True, None, id.value)
        
    def visitArrayCell(self, ast, o):
        # class ArrayCell(LHS):
        # arr:Expr
        # idx:Expr
        
        e1 = self.visit(ast.arr, o)
        e2 = self.visit(ast.idx, o)
        if type(e1) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if type(e2) is not IntType:
            raise TypeMismatchInExpression(ast)
        
    
    def visitFieldAccess(self, ast, o):
        # this.a , x.y, A.b        this.a.b
        # class FieldAccess(LHS):
        # obj:Expr
        # fieldname:Id
        # o is tuple (Class decl, list of ClassDecl)
        
        obj = self.visit(ast.obj, o)  # Symbol 

        if not obj:
            raise Undeclared(Identifier(), ast.obj.name)
        if not type(obj.mtype) in [SelfLiteral, ClassType, ClassDecl]:
            raise TypeMismatchInExpression(ast)
        if type(o[0]) is ClassDecl:
            # check if obj is a Class Name 
            field = ast.fieldname.name
            infor = None
            if type(ast.obj) is Id:
                # obj = A, obj = ClassType
                # find field
                if not type(obj.mtype) is ClassDecl:
                    raise TypeMismatchInExpression(ast)
                infor = findField(field , ast.obj.name, o[1])                
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Instance:
                    raise IllegalMemberAccess(ast)
                
                if type(infor.decl) is ConstDecl:
                    return Symbol(getName(infor), getType(infor), True, Static(), infor.decl.value)
                elif type(infor.decl) is VarDecl:
                    return Symbol(getName(infor), getType(infor), False, Static(), infor.decl.varInit)
            elif type(obj.mtype) is SelfLiteral:
                infor = findField(field, o[0].classname.name, o[1])     # this is a attribute declare
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(obj.mtype) is ClassType:          # sure ? 
                infor = findField(field, obj.mtype.classname.name, o[1])
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            #return getType(infor)
            if type(infor.decl) is ConstDecl:
                return Symbol(getName(infor), getType(infor), True, Instance(), infor.decl.value)
            elif type(infor.decl) is VarDecl:
                return Symbol(getName(infor), getType(infor), False, Instance(), infor.decl.varInit)
        elif type(o[0]) is MethodDecl:
            field = ast.fieldname.name
            infor = None
            if type(ast.obj) is Id:
                infor = findField(field , ast.obj.name, o[1])
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(obj.mtype) is ClassDecl:
                    if type(infor.kind) is Instance:
                        raise IllegalMemberAccess(ast)
                elif type(obj.mtype) is ClassType:
                    if type(infor.kind) is Static:
                        raise IllegalMemberAccess(ast)
                
                if type(infor.decl) is ConstDecl:
                    return Symbol(getName(infor), getType(infor), True, Static(), infor.decl.value)
                elif type(infor.decl) is VarDecl:
                    return Symbol(getName(infor), getType(infor), False, Static(), infor.decl.varInit)
            elif type(obj.mtype) is SelfLiteral:
                infor = findField(field, o[2].classname.name, o[1])     # this is a attribute declare
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(obj.mtype) is ClassType:
                infor = findField(field, o[2].classname.name, o[1])
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)   
                 
            if type(infor.decl) is ConstDecl:
                return Symbol(getName(infor), getType(infor), True, Instance(), infor.decl.value)
            elif type(infor.decl) is VarDecl:
                return Symbol(getName(infor), getType(infor), False, Instance(), infor.decl.varInit)

                
    
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
    
    
    def visitSelfLiteral(self, ast, o):
        return Symbol(None, SelfLiteral(), True, None)

    def visitArrayLiteral(self, ast, param):
        return None 












    def visitClassType(self, ast, param):
        return ClassType(ast.classname)

    def visitIntType(self, ast, param):
        return IntType()
    
    def visitFloatType(self, ast, param):
        return FloatType()
    
    def visitBoolType(self, ast, param):
        return BoolType()  
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitVoidType(self, ast, param):
        return VoidType()


    def visitIntLiteral(self, ast, param):
        return Symbol(None, IntType(), True, None, ast.value)
    
    def visitFloatLiteral(self, ast, param):
        return Symbol(None, FloatType(), True, None, ast.value)
    
    def visitBooleanLiteral(self, ast, param):
        return Symbol(None, BoolType(), True, None, ast.value)
    
    def visitStringLiteral(self, ast, param):
        return Symbol(None, StringType(), True, None, ast.value)
    
    def visitNullLiteral(self, ast, param): # check it later
        return Symbol(None, NullLiteral(), True, None, ast.value)