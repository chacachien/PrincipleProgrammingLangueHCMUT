

#def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
#def printout(self, in_):
#def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
#def emitPUTSTATIC(self, lexeme, in_, frame):
#ex1
def visitValDecl(self, ctx, o):
    if o.frame is None:
        code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
        self.emit.printout(code)
        return Symbol(ctx.name, ctx.typ, CName(self.className))
    else:
        indx = o.frame.getNewIndex()
        code = self.emit.emitVAR( indx,ctx.name, ctx.typ,o.frame.getStartLabel(),o.frame.getEndLabel(), o.frame)
        self.emit.printout(code)
        return Symbol(ctx.name, ctx.typ, Index(indx))
#ex2
def visitId(self, ctx, o):
    sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
    if o.isLeft:
        if type(sym.value) is CName:
            code = self.emit.emitPUTSTATIC(sym.value.value+'.'+ctx.name, sym.mtype, o.frame)
            
            
        else:
            #def emitWRITEVAR(self, name, inType, index, frame):
            code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value , o.frame)
            
    else:
        if type(sym.value) is CName:
            
            code = self.emit.emitGETSTATIC(sym.value.value+'.'+ctx.name, sym.mtype, o.frame)
            
        else:
            #def emitREADVAR(self, name, inType, index, frame):
            code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
    return code, sym.mtype    

#ex3
def visitAssign(self, ctx, o):
    rc, rt = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
    self.emit.printout(rc)
    lc, lt = self.visit(ctx.lhs, Access(o.frame, o.sym, True))
    self.emit.printout(lc)
    
    
    
#ex4 if
def visitIf(self, ctx, o):
    ec, et = self.visit(ctx.expr,Access(o.frame, o.sym, False) )
    self.emit.printout(ec)
    flabel = o.frame.getNewLabel()
    
    code = self.emit.emitIFFALSE(flabel, o.frame)
    self.emit.printout(code)
    
    self.visit(ctx.tstmt, o)
    if ctx.estmt is None:
        code = self.emit.emitLABEL(flabel, o.frame)
        self.emit.printout(code)
    else:
        tlabel = o.frame.getNewLabel()
        
        code = self.emit.emitGOTO(tlabel, o.frame)
        self.emit.printout(code)
        
        code = self.emit.emitLABEL(flabel, o.frame)
        self.emit.printout(code)
        
        self.visit(ctx.estmt, o)
        code = self.emit.emitLABEL(tlabel, o.frame)
        self.emit.printout(code) 
    
#ex5 while
def visitWhile(self, ctx, o):
    o.frame.enterLoop()
    cLable = o.frame.getContinueLabel()
    bLable = o.frame.getBreakLabel()
    
    code = self.emit.emitLABEL(cLable, o.frame)
    self.emit.printout(code)
    
    ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
    self.emit.printout(ec)
    
    code = self.emit.emitIFFALSE(bLable, o.frame)
    self.emit.printout(code)
    
    self.visit(ctx.stmt, o)
    # code = self.emit.emitGOTO(cLable, o.frame)
    # self.emit.printout(code)
    
    code = self.emit.emitLABLE(bLable, o.frame)
    self.emit.printout(code)
    o.frame.exitLoop()













    # sinh ma cho exp
    # ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
    # # xin tu fram flabel
    # flable = o.frame.getNewLabel()
    # # jum to flabel if false
    # code = self.emit.emitIFFALSE(flabel, o.frame)
    # self.emit.printout(code)
    
    # # sinh ma cho stmt
    # self.visit(ctx.tstmt, o)
    # if ctx.estmt is None:
    #     # dat flabel tai day
    #     code = self.emit.emitLABEL(flabel, o.frame)
    #     self.emit.printout(code)
    # else:
    #     ## xin tu fram elabel
    #     elable = o.frame.getNewLabel()
    #     # jump to elabel
    #     code = self.emit.emitGOTO(elable, o.frame)
    #     self.emit.printout(code)
        
        
    #     code = self.emit.emitLABEL(elabel, o.frame)
    #     self.emit.printout(code)
        
    #     self.visit(ctx.estmt, o)
    #     code = self.emit.emitLABEL(elabel, o.frame)
        
        

    