
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *

from StaticError import *
from functools import reduce


class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return  "MType([" + ','.join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"
class Symbol:
    def __init__(self,name,mtype,isFinal, static, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isFinal = isFinal
        self.static = static
    def __str__(self):
        return str(self.name) + "," + str(self.mtype) + ", " + str(self.value) + ", " + str(self.isFinal) + ", " + str(self.static)
class ClassDetail:
    def __init__(self, name, parent =None, member = []):
        self.name = name        # Id
        self.parent = parent    # Id
        self.member = member    # list of AttributeDecl or MethodDecl
    def __str__(self):
        return "(" + str(self.name) +","+ str(self.parent) +","+ str(self.member) +")"


'''
This will receive any type of AST
Return name of this AST 
'''
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


'''
This will receive any type of AST
Return type of this AST
'''
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


'''
Input: a ast, a list of this same ast
Output: True if this ast is redeclared in this list
'''
def checkRedeclaredMember(ast, l):
    wasDecl = [False, False]
    for mem in l:
        if mem is ast:
            wasDecl[1] = True
            break
        elif type(mem) is AttributeDecl:
            if mem.decl is ast:
                wasDecl[1] = True
                break
        if getName(mem) == getName(ast):
            wasDecl[0] = True
    
    if wasDecl[0] and wasDecl[1]:
        return True
    return False


'''
Input: a name, a list of any type of ast
Output: the ast which has this name in this list'''
def findInList(name, l):
    for mem in l:
        if getName(mem) == name:
            return mem
    return None


'''
Input: a name, a list of member in classdecl
Output: the member which has this name in this list'''
def findField(name, thisO, o):
    fatherC = findInList(thisO, o)
    while fatherC:
        infor = findInList(name, fatherC.memlist)
        if infor:
            return infor
        fatherO = fatherC.parentname
        fatherC = findInList(getName(fatherO), o)
    return None



'''
Check if a class is a child of another class
'''
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


'''
Check if lhs can be assigned by rhs
This language follow coercions are permitted
'''
def checkAssign(lhs, rhs,o):
    # lhs and rhs are Symbol
    l = lhs
    r = rhs
    if type(lhs) is Symbol:
        l = lhs.mtype
        r = rhs.mtype if not type(rhs.mtype) is MType else rhs.mtype.rettype
    
    if type(l) is VoidType:
        return False
    
    if type(l) is IntType:
        if type(r) is IntType:
            return IntType()
    elif type(l) is FloatType:
        if type(r) in [FloatType, IntType]:
            return FloatType()
    elif type(l) is BoolType:
        if type(r) is BoolType:
            return BoolType()
    elif type(l) is ClassType:
        if type(r) is ClassType:
            if checkIsChild(r.classname.name, l.classname.name, o):
                return ClassType(l.classname)
    elif type(l) is ArrayType:
        if type(r) is ArrayType:
            if l.size == r.size:
                if checkAssign(l.eleType, r.eleType, o):
                    return ArrayType(l.size, l.eleType)
    elif type(l) is type(r):
        return type(l)
    return False
    

'''
This class iterates through the AST to perform further examination
'''
class NameCheck(BaseVisitor):
    def visitProgram(self, ast, o):
        o = []    # list of ClassDecl
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
        return ast

    def visitMethodDecl(self, ast, o):
        return ast



class StaticChecker(BaseVisitor):
    classProgram = [
        ClassDecl(Id('io'), [MethodDecl(Static(), Id('readInt'), [], IntType(), Block([],[])),
                            MethodDecl(Static(), Id('writeIntLn'),[VarDecl(Id('anArg'),IntType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('writeInt'),[VarDecl(Id('anArg'),IntType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('readFloat'), [], FloatType(), Block([],[])),
                            MethodDecl(Static(), Id('writeFloat'),[VarDecl(Id('anArg'),FloatType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('writeFloatLn'),[VarDecl(Id('anArg'),FloatType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('readBool'), [], BoolType(), Block([],[])), 
                            MethodDecl(Static(), Id('writeBool'),[VarDecl(Id('anArg'),BoolType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('writeBoolLn'),[VarDecl(Id('anArg'),BoolType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('readStr'), [], StringType(), Block([],[])),
                            MethodDecl(Static(), Id('writeStr'),[VarDecl(Id('anArg'),StringType())], VoidType(), Block([],[])),
                            MethodDecl(Static(), Id('writeStrLn'),[VarDecl(Id('anArg'),StringType())], VoidType(), Block([],[])),     
                                 ], None),
    ]   
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):

        self.visit(self.ast, StaticChecker.classProgram)
        return ""

    def visitProgram(self, ast, c):
        o = StaticChecker.classProgram + NameCheck().visit(ast, c)
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
            self.visit(mem, o) # c is tuple (this class, list of ClassDeclared, method)
        
    def visitVarDecl(self, ast, c):
        # class VarDecl(StoreDecl):
        # variable : Id
        # varType : Type
        # varInit : Expr = None 
        
        vartyp = self.visit(ast.varType, c)
        if type(vartyp) is ClassType:
            if not findInList(vartyp.classname.name, c[1]):
                raise Undeclared(Class(), vartyp.classname.name)
        if type(vartyp) is VoidType:
            raise TypeMismatchInStatement(ast)
        
        
        # this is a variable
        if type(c[0]) is MethodDecl:
            # Decide if this var is in method or in block
            wasdecl = c[3][0] if not c[3][1] ==[] else c[0].param + c[0].body.decl
            if checkRedeclaredMember(ast, wasdecl):
                raise Redeclared(Variable(), getName(ast))
            
            # Check Type if this var is assigned 
            if ast.varInit:
                typ = self.visit(ast.varInit, c)                  # Symbol 
                if not checkAssign(vartyp, typ.mtype, c[1]):        
                    raise TypeMismatchInStatement(ast)
                
        # this is a class attribute, so we can't throw error Type here
        elif type(c[0]) is ClassDecl:
            if checkRedeclaredMember(ast, c[0].memlist):
                raise Redeclared(Attribute(), getName(ast))
        return Symbol(getName(ast), ast.varType, False, None, ast.varInit)
        
    def visitConstDecl(self, ast, c):
        # class ConstDecl(StoreDecl):
        # constant : Id
        # constType : Type
        # value : Expr
        
        
        vartyp = self.visit(ast.constType, c)       
        if type(vartyp) is ClassType:
            if not findInList(vartyp.classname.name, c[1]):
                raise Undeclared(Class(), vartyp.classname.name)
        elif type(vartyp) is VoidType:
            raise TypeMismatchInConstant(ast)
        
        if type(c[0]) is MethodDecl:
        # c is tuple (this method, list of ClassDeclared, this class)
            wasdecl = c[3][0] if c[3][1] != [] else c[0].param + c[0].body.decl
            if checkRedeclaredMember(ast, wasdecl):
                raise Redeclared(Constant(), getName(ast))
        elif type(c[0]) is ClassDecl:
            if checkRedeclaredMember(ast, c[0].memlist):
                raise Redeclared(Attribute(), getName(ast))
            
        # because this is a const, so we can throw error Type here
        if ast.value:
            typ = self.visit(ast.value, c)                  # literal, type                
            if  not checkAssign(vartyp, typ.mtype, c[1]):
                raise TypeMismatchInConstant(ast)
            
            if type(c[0]) is MethodDecl:    
                if typ.value is None:
                    isPara = findInList(getName(ast.value), c[0].param)
                    if not isPara:
                        raise IllegalConstantExpression(ast.value)                
            else:
                if typ.value is None:
                    raise IllegalConstantExpression(ast.value)
        else:
            raise IllegalConstantExpression(None)
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
        
        # o = (this class, list of ClassDeclared, this method, [])
        
        if ast.returnType:
            typ = self.visit(ast.returnType, o)
            if type(typ) is ClassType:
                if not findInList(typ.classname.name, o[1]):
                    raise Undeclared(Class(), typ.classname.name)
        
        if checkRedeclaredMember(ast, o[0].memlist):
            raise Redeclared(Method(), getName(ast))
        
        for par in ast.param:
            if checkRedeclaredMember(par, ast.param):
                raise Redeclared(Parameter(), getName(par))
        
        o = [ast, o[1], o[0], [[]]]
        
        self.visit(ast.body, o)
        if ast.returnType:
            return Symbol(getName(ast), MType([self.visit(x, o) for x in ast.param], self.visit(ast.returnType, o)), False, self.visit(ast.kind, o))
        return Symbol(getName(ast), MType([self.visit(x, o) for x in ast.param], VoidType()), False, self.visit(ast.kind, o))
    
    def visitAttributeDecl(self, ast, o): 
        # class AttributeDecl(MemDecl):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl
        
        # o = (this class, list of ClassDetail)
        #if type(ast.decl.)
        
        decl = self.visit(ast.decl, o)  # Symbol (name, mtype, isFinal, static, value)         
        
        final = False
        if type(ast.decl) is VarDecl:
            if type(ast.decl.varInit) is Id:
                raise TypeMismatchInStatement(ast)
        
        elif type(ast.decl) is ConstDecl:
            if type(ast.decl.value) is Id:
                raise TypeMismatchInConstant(ast.decl)
            final = True

        lhs = decl.mtype  # type of lhs
        if decl.value:
            rhs = self.visit(decl.value, o) # rhs is a SYmbol
            if type(rhs.mtype) is ClassType and type(lhs) is ClassType:
                if not findInList(rhs.name, o[1]):
                    raise Undeclared(Class(), getName(rhs))
                if not checkIsChild(rhs.name, lhs.classname.name, o[1]):
                    if final:
                        raise TypeMismatchInConstant(ast)
                    raise TypeMismatchInStatement(ast)
            elif not checkAssign(lhs, rhs.mtype, o):
                if final:
                    raise TypeMismatchInConstant(ast.decl)
                raise TypeMismatchInStatement(ast)
        return Symbol(getName(ast), decl.mtype, final, self.visit(ast.kind, o), decl.value)

    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, self.visit(ast.eleType, param))
    
    def visitBinaryOp(self, ast, o):

        l = self.visit(ast.left, o)
        r = self.visit(ast.right, o)
        v = True if l.value and r.value else None
        
        op = ast.op
        if op in ['+','-','*']:
            if type(l.mtype) in [IntType, FloatType] and type(r.mtype) in [IntType, FloatType]:
                if type(l.mtype) is FloatType or type(r.mtype) is FloatType:
                    return Symbol(None, FloatType(), True, None, v)
                else:
                    return Symbol(None, IntType(), True, None, v)
            else:
                raise TypeMismatchInExpression(ast)
        if op in ['%', '\\']:
            if type(l.mtype) is IntType and type(r.mtype) is IntType:
                return Symbol(None, IntType(), True, None, v)
            else:
                raise TypeMismatchInExpression(ast)
        if op in ['/']:
            if type(l.mtype) in [IntType, FloatType] and type(r.mtype) in [IntType, FloatType]:
                return Symbol(None, FloatType(), True, None, v)
            else:
                raise TypeMismatchInExpression(ast)
        if op in ['&&', '||']:
            if type(l.mtype) is BoolType and type(r.mtype) is BoolType:
                return Symbol(None, BoolType(), True, None, v)
            else:
                raise TypeMismatchInExpression(ast)
        if op in ['==', '!=']:
            if type(l.mtype) in [IntType, BoolType] and type(r.mtype) in [IntType, BoolType]:
                if type(l.mtype) is type(r.mtype):
                    return Symbol(None, BoolType(), True, None, v)
            raise TypeMismatchInExpression(ast)
        if op in ['<', '<=', '>', '>=']:
            if type(l.mtype) in [IntType, FloatType] and type(r.mtype) in [IntType, FloatType]:
                return Symbol(None, BoolType(), True, None, v)
            raise TypeMismatchInExpression(ast)
        if op in ['^']:
            if type(l.mtype) is StringType and type(r.mtype) is StringType:
                return Symbol(None, StringType(), True, None, v)
            raise TypeMismatchInExpression(ast)
        
    def visitUnaryOp(self, ast, param):
        # class UnaryOp(Expr):
        # op:str
        # body:Expr
        op = ast.op
        body = self.visit(ast.body, param)
        if op in ['-', '+']:
            if type(body.mtype) in [IntType, FloatType]:
                return Symbol(None, body.mtype, True, None, body.value)
        if op in ['!']:
            if type(body.mtype) is BoolType:
                return Symbol(None, BoolType(), True, None, body.value)
            
        raise TypeMismatchInExpression(ast)
        
            
    def visitCallExpr(self, ast, o):
        # class CallExpr(Expr):
        # obj: Expr
        # method:Id
        # param:List[Expr]
        
        obj = self.visit(ast.obj, o)                 # Symbol
        para = [self.visit(x, o) for x in ast.param] # list of Symbol or []
        field = ast.method.name                      # name of method
        infor = None                                 # method declare
        if not obj:
            raise Undeclared(Identifier(), ast.obj.name)
        if not type(obj.mtype) in [SelfLiteral, ClassType, ClassDecl]:
            raise TypeMismatchInExpression(ast)
        # check the call in classdecl
        if type(o[0]) is ClassDecl:
            
            # check if obj is a Class Name 
            if type(ast.obj) is Id:
                # obj = A 
                # find field
                if not type(obj.mtype) is ClassDecl:
                    raise TypeMismatchInExpression(ast)
                infor = findField(field, ast.obj.name, o[1])       # infor is a method declare
                if not infor:
                    raise Undeclared(Method(), field)
                
                if type(infor.kind) is Instance:
                    raise IllegalMemberAccess(ast)
            elif type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])     # this is a method declare
                
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInExpression(ast)
                
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
            agr = [self.visit(x) for x in infor.param]                
            for i in range(len(para)):
                if not checkAssign(agr[i], para[i], o):
                    raise TypeMismatchInExpression(ast)

        # check the call in method 
        elif type(o[0]) is MethodDecl:                        
            if type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])     # this is a method declare
                
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInExpression(ast)
                
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(ast.obj) is Id:
                # obj = A, obj = ClassType
                infor = findField(field , ast.obj.name, o[1])
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInExpression(ast)
                if type(infor.returnType) is VoidType:
                    raise TypeMismatchInExpression(ast)
                
                if type(obj.mtype) is ClassDecl:
                    if type(infor.kind) is Instance:
                        raise IllegalMemberAccess(ast)
                elif type(obj.mtype) is ClassType:
                    if type(infor.kind) is Static:
                        raise IllegalMemberAccess(ast)
            else:
                raise TypeMismatchInExpression(ast)
            
            agr = [self.visit(x,o) for x in infor.param] # list of Symbol
            if len(agr) != len(para):
                raise TypeMismatchInExpression(ast)
            for i in range(len(para)):
                if not checkAssign(agr[i], para[i], o[1]):
                    
                    raise TypeMismatchInExpression(ast)
        if type(infor.returnType) is VoidType:
            raise TypeMismatchInExpression(ast)
        return Symbol(None, infor.returnType, False, None, infor.body)
    
    def visitNewExpr(self, ast, o):
        
        # class NewExpr(Expr):
        # classname:Id
        # param:List[Expr]
        
        [self.visit(x,o) for x in ast.param] 
        return Symbol(ast.classname.name, ClassType(ast.classname), False, None) 
    
    def visitId(self, ast, o):
        
        # class Id(LHS):
        # name:str
        # o is tuple (this method, list of ClassDeclared, this class, [[], []])
        # or o is tuple (this class, list of ClassDetail)
        id = None
        flag = False
        if type(o[0]) is MethodDecl:
            
            wasDecl = list(reduce(lambda x,y: x+ y, o[3])) + o[0].param + o[0].body.decl
            id = findInList(ast.name, wasDecl)
            if id:
                flag = True
        if not flag:
            id = findInList(ast.name, o[1])
            if id:
                return Symbol(getName(id), id, False,None) # this is a ClassDeclare
            raise Undeclared(Identifier(), ast.name)
        else:
            if type(id) is VarDecl:
                if findInList(ast.name, o[0].param):
                    return Symbol(getName(id), getType(id), False, None, True)
                return Symbol(getName(id), getType(id), False, None, id.varInit)     # this is a VarDeclare or ConstDeclare
            elif type(id) is ConstDecl:
                return Symbol(getName(id), getType(id), True, None, True)
        
    def visitArrayCell(self, ast, o):
        # class ArrayCell(LHS):
        # arr:Expr
        # idx:Expr
        
        e1 = self.visit(ast.arr, o)
        e2 = self.visit(ast.idx, o)
        if not type(e1.mtype) is ArrayType:
            raise TypeMismatchInExpression(ast)
        if not type(e2.mtype) is IntType:
            raise TypeMismatchInExpression(ast)
        return Symbol(None, e1.mtype.eleType, False, None)
    
    def visitFieldAccess(self, ast, o):
        # this.a , x.y, A.b        this.a.b
        # class FieldAccess(LHS):
        # obj:Expr
        # fieldname:Id
        # o is tuple (Class decl, list of ClassDecl)
        
        obj = self.visit(ast.obj, o)  # Symbol 
        field = ast.fieldname.name
        infor = None
        if not obj:
            raise Undeclared(Identifier(), ast.obj.name)
        if not type(obj.mtype) in [SelfLiteral, ClassType, ClassDecl]:
            raise TypeMismatchInExpression(ast)
        if type(o[0]) is ClassDecl:
            # check if obj is a Class Name 
           
            if type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])
                
                if not infor:
                    raise Undeclared(Attribute(), field)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(ast.obj) is Id:
                # obj = A, obj = ClassType
                # find field
                if not type(obj.mtype) is ClassDecl:
                    raise TypeMismatchInExpression(ast)
                infor = findField(field , ast.obj.name, o[1])                
                if not infor:
                    raise Undeclared(Attribute(), field)
                if not type(infor) is AttributeDecl:
                    raise TypeMismatchInExpression(ast)
                if type(infor.kind) is Instance:
                    raise IllegalMemberAccess(ast)
                
                if type(infor.decl) is ConstDecl:
                    return Symbol(getName(infor), getType(infor), True, Static(), infor.decl.value)
                elif type(infor.decl) is VarDecl:
                    return Symbol(getName(infor), getType(infor), False, Static(), infor.decl.varInit)
            else:
                raise TypeMismatchInExpression(ast)
            #return getType(infor)
            
        elif type(o[0]) is MethodDecl:

            if type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])
                if not infor:
                    raise Undeclared(Attribute(), field)
                
                if not type(infor) is AttributeDecl:
                    raise TypeMismatchInExpression(ast)
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(ast.obj) is Id:
                infor = findField(field , ast.obj.name, o[1])
                if not infor:
                    raise Undeclared(Attribute(), field)
                
                if not type(infor) is AttributeDecl:
                    raise TypeMismatchInExpression(ast)
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
            else:
                raise TypeMismatchInExpression(ast)     
        if type(infor.decl) is ConstDecl:
            return Symbol(getName(infor), getType(infor), True, Instance(), infor.decl.value)
        elif type(infor.decl) is VarDecl:
            return Symbol(getName(infor), getType(infor), False, Instance(), infor.decl.varInit)

    def visitBlock(self, ast, o):
            #---------------------
            # decl:List[StoreDecl]
            # stmt:List[Stmt]
            #---------------------
        # o = (this method, list of ClassDetail, this class, [block])
        
        o[3] =  [ast.decl] + o[3]
        for decl in ast.decl:              
            self.visit(decl, o)
        
        for stmt in ast.stmt:
            self.visit(stmt, o)
    
    def visitIf(self, ast, o):
        # class If(Stmt):
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt = None
        expr = self.visit(ast.expr, o)
        if type(expr.mtype) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, o)
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)

    def visitFor(self, ast, param):
        # class For(Stmt):
        # id:Id
        # expr1:Expr
        # expr2:Expr
        # up: bool #True => increase; False => decrease
        # loop:Stmt
        sid = self.visit(ast.id, param)
        if sid.isFinal:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        expr1 = self.visit(ast.expr1, param)
        expr2 = self.visit(ast.expr2, param)
        if not type(expr1.mtype) is IntType or type(expr2.mtype) is not IntType or type(sid.mtype) is not IntType:
            raise TypeMismatchInStatement(ast)
        o = [param[0], param[1], param[2], param[3], True]
        self.visit(ast.loop, o)
        
    def visitContinue(self, ast, param):
        if len(param) < 5:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast, param):
        if len(param) < 5:
            raise MustInLoop(ast)
    def visitReturn(self, ast, o):
        # class Return(Stmt):
        # expr:Expr
        
        l =  o[0].returnType 
        expr = self.visit(ast.expr, o)      # Symbol
        if not checkAssign(l, expr.mtype, o[1]):
            raise TypeMismatchInStatement(ast) 
    
    def visitAssign(self, ast, o):
        # class Assign(Stmt):
        # lhs:Expr
        # exp:Expr
        l = self.visit(ast.lhs, o)
        if l.isFinal:
            raise CannotAssignToConstant(ast)
        r = self.visit(ast.exp, o)

        if not checkAssign(l, r, o[1]):
            raise TypeMismatchInStatement(ast)
        
        
    def visitCallStmt(self, ast, o):
        # class CallStmt(Stmt):
        # obj: Expr  
        # method:Id
        # param:List[Expr]
        obj = self.visit(ast.obj, o)    # Symbol
        para = [self.visit(x, o) for x in ast.param] # list of Symbol or []
        field = ast.method.name
        infor = None
        if not obj:
            raise Undeclared(Identifier(), ast.obj.name)
        if not type(obj.mtype) in [SelfLiteral, ClassType, ClassDecl]:
            raise TypeMismatchInStatement(ast)
        
        
        if type(o[0]) is ClassDecl:
            # check if obj is a Class Name 
            if type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])     # this is a method declare
                
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInStatement(ast)

                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(ast.obj) is Id:
                # obj = A, obj = ClassType
                # find field
                if not type(obj.mtype) is ClassDecl:
                    raise TypeMismatchInStatement(ast)
                infor = findField(field, ast.obj.name, o[1])       # infor is a method declare
                if not infor:
                    raise Undeclared(Method(), field)

                if type(infor.kind) is Instance:
                    raise IllegalMemberAccess(ast)
            else:
                raise TypeMismatchInStatement(ast)

            agr = [self.visit(x) for x in infor.param]                
            for i in range(len(para)):
                if not checkAssign(agr[i], para[i], o):
                    raise TypeMismatchInStatement(ast)
            
        elif type(o[0]) is MethodDecl:
                                    
            if type(obj.mtype) is ClassType:
                infor = findField(field, obj.mtype.classname.name, o[1])     # this is a method declare
                
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInStatement(ast)
                
                if type(infor.kind) is Static:
                    raise IllegalMemberAccess(ast)
            elif type(ast.obj) is Id:
                # obj = A, obj = ClassType
                infor = findField(field , ast.obj.name, o[1])
                if not infor:
                    raise Undeclared(Method(), field)
                if not type(infor) is MethodDecl:
                    raise TypeMismatchInStatement(ast)

                if type(obj.mtype) is ClassDecl:
                    if type(infor.kind) is Instance:
                        raise IllegalMemberAccess(ast)
                elif type(obj.mtype) is ClassType:
                    if type(infor.kind) is Static:
                        raise IllegalMemberAccess(ast)
            else:
                raise TypeMismatchInStatement(ast)
            
            agr = [self.visit(x,o) for x in infor.param] # list of Symbol
            if len(agr) != len(para):
                raise TypeMismatchInStatement(ast)
            for i in range(len(para)):
                if not checkAssign(agr[i], para[i], o[1]):
                    
                    raise TypeMismatchInStatement(ast)
        if not type(infor.returnType) is VoidType:
            raise TypeMismatchInStatement(ast)
        return Symbol(None, infor.returnType, False, None, infor.body)
        
    
    def visitSelfLiteral(self, ast, o):
        if type(o[0]) is MethodDecl:
            return Symbol(SelfLiteral(), ClassType(Id(o[2].classname.name)), False, Instance())
        elif type(o[0]) is ClassDecl:
            return Symbol(SelfLiteral(),ClassType(Id(o[0].classname.name)), False, Instance())

    def visitArrayLiteral(self, ast, o):
        # class ArrayLiteral(Literal):
        # value: List[Literal]
        typ = [self.visit(x, o) for x in ast.value]
        l = typ[0].mtype
        for i in typ:
            if not type(l) is type(i.mtype):
                raise IllegalArrayLiteral(ast)
            
        return Symbol(None, ArrayType(len(typ), l), False, None, True)

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
        return Symbol(None, NullLiteral(), True, None, None)