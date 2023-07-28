a= """Program([
    ClassDecl(Id(Shape),[],[
        AttributeDecl(Instance,VarDecl(Id(length),FloatType)),
        AttributeDecl(Instance,VarDecl(Id(width),FloatType)),
        MethodDecl(Id(__init__Shape),Instance,[ParamDecl(Id(l),FloatType),ParamDecl(Id(w),FloatType)],VoidType,Block([],[
            Assign(FieldAccess(Self(),Id(length)),Id(l)),
            Assign(FieldAccess(Self(),Id(width)),Id(w))
        ]))
    ]),
    ClassDecl(Id(Circle),Id(Shape),[
        MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[
            Return(BinaryOp(*,BinaryOp(*,FloatLit(3.14),FieldAccess(Self(),Id(radius))),FieldAccess(Self(),Id(radius))))
        ]))
    ]),
    ClassDecl(Id(Test),[],[
        MethodDecl(Id(main),Static,[],VoidType,Block([],[
            VarDecl(Id(c),Id(Circle)),
            VarDecl(Id(area),FloatType),
            Assign(Id(c),NewExpr(Id(Circle),[FloatLit(5.0), FloatLit(5.0)])),
            Assign(Id(area),CallExpr(FieldAccess(Id(c),Id(getArea)),[])),
            CallStmt(
                Call(Id(io),Id(writeStrLn),[
                    BinaryOp(+,StringLit(Area of Circle: ),Id(area))
                ])
            )
        ]))
    ])
])

"""
import string
a=a.translate({ord(c): None for c in string.whitespace})
print(a)