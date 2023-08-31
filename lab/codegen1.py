#ex5
#ex5
    def visitBinExpr(self,ctx,o):
        e1c, e1t = self.visit(ctx.e1,o)
        e2c, e2t = self.visit(ctx.e2,o)
        op = ctx.op
        code = e1c +e2c
        if type(e1t) is type(e2t):
            typ = e1t
        elif type(e1t) is IntType:
            code =e1c + self.emit.emitI2F(o.frame) + e2c
            typ = e2t
        elif type(e2t) is IntType:
            code = e1c + e2c + self.emit.emitI2F(o.frame)
            typ = e1t
        if op in ['+', '-']:
            op = self.emit.emitADDOP(op, typ, o.frame)
        elif op in ['*']:
            op = self.emit.emitMULOP(op, typ, o.frame)
        elif op in ['/']:
            if type(e1t) is IntType and type(e2t) is IntType:
                code = e1c + self.emit.emitI2F(o.frame)
                code = code + e2c + self.emit.emitI2F(o.frame)
                typ = FloatType()
            op = self.emit.emitMULOP(op, typ, o.frame)
        else:
            op = self.emit.emitREOP(op, typ, o.frame)
            typ = BoolType()
        return code + op, typ