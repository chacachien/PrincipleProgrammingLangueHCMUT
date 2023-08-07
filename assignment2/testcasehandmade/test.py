a='Program([ClassDecl(Id(Triangle),[AttributeDecl(Instance,VarDecl(Id(point1),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point2),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point3),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(edge1),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge2),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge3),FloatType)),MethodDecl(Id(Triangle),Instance,[param(Id(p1),ClassType(Id(Point))),param(Id(p2),ClassType(Id(Point))),param(Id(p3),ClassType(Id(Point)))],Block([],[AssignStmt(FieldAccess(Self(),Id(point1)),Id(p1)),AssignStmt(FieldAccess(Self(),Id(point2)),Id(p2)),AssignStmt(FieldAccess(Self(),Id(point3)),Id(p3)),AssignStmt(FieldAccess(Self(),Id(edge1)),CallExpr(Id(Point),Id(length),[Id(p1),Id(p2)])),AssignStmt(FieldAccess(Self(),Id(edge2)),CallExpr(Id(Point),Id(length),[Id(p2),Id(p3)])),AssignStmt(FieldAccess(Self(),Id(edge3)),CallExpr(Id(Point),Id(length),[Id(p3),Id(p1)]))])),MethodDecl(Id(circumference),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(edge1)),FieldAccess(Self(),Id(edge2))),FieldAccess(Self(),Id(edge3))),IntLit(2)))])),MethodDecl(Id(area),Instance,[],FloatType,Block([VarDecl(Id(p),FloatType)],[AssignStmt(Id(p),CallExpr(Self(),Id(circumference),[])),Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(p),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge1)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge2)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge3))))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(Point))),VarDecl(Id(p2),ClassType(Id(Point))),VarDecl(Id(p3),ClassType(Id(Point))),VarDecl(Id(abc),ClassType(Id(Triangle))),VarDecl(Id(area),FloatType)],[AssignStmt(Id(p1),NewExpr(Id(Point),[IntLit(0),IntLit(0)])),AssignStmt(Id(p2),NewExpr(Id(Point),[IntLit(0),IntLit(1)])),AssignStmt(Id(p3),NewExpr(Id(Point),[IntLit(1),IntLit(0)])),AssignStmt(Id(abc),NewExpr(Id(Triangle),[Id(p1),Id(p2),Id(p3)])),AssignStmt(Id(area),CallExpr(Id(abc),Id(area),[])),Call(Id(io),Id(writeLn),[StringLit(Area of triangle: ),Id(area)])]))])])'
b='Program([ClassDecl(Id(Triangle),[AttributeDecl(Instance,VarDecl(Id(point1),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point2),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point3),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(edge1),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge2),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge3),FloatType)),MethodDecl(Id("<init>"),Instance,[param(Id(p1),ClassType(Id(Point))),param(Id(p2),ClassType(Id(Point))),param(Id(p3),ClassType(Id(Point)))],Block([],[AssignStmt(FieldAccess(Self(),Id(point1)),Id(p1)),AssignStmt(FieldAccess(Self(),Id(point2)),Id(p2)),AssignStmt(FieldAccess(Self(),Id(point3)),Id(p3)),AssignStmt(FieldAccess(Self(),Id(edge1)),CallExpr(Id(Point),Id(length),[Id(p1),Id(p2)])),AssignStmt(FieldAccess(Self(),Id(edge2)),CallExpr(Id(Point),Id(length),[Id(p2),Id(p3)])),AssignStmt(FieldAccess(Self(),Id(edge3)),CallExpr(Id(Point),Id(length),[Id(p3),Id(p1)]))])),MethodDecl(Id(circumference),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(edge1)),FieldAccess(Self(),Id(edge2))),FieldAccess(Self(),Id(edge3))),IntLit(2)))])),MethodDecl(Id(area),Instance,[],FloatType,Block([VarDecl(Id(p),FloatType)],[AssignStmt(Id(p),CallExpr(Self(),Id(circumference),[])),Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(p),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge1)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge2)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge3))))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(Point))),VarDecl(Id(p2),ClassType(Id(Point))),VarDecl(Id(p3),ClassType(Id(Point))),VarDecl(Id(abc),ClassType(Id(Triangle))),VarDecl(Id(area),FloatType)],[AssignStmt(Id(p1),NewExpr(Id(Point),[IntLit(0),IntLit(0)])),AssignStmt(Id(p2),NewExpr(Id(Point),[IntLit(0),IntLit(1)])),AssignStmt(Id(p3),NewExpr(Id(Point),[IntLit(1),IntLit(0)])),AssignStmt(Id(abc),NewExpr(Id(Triangle),[Id(p1),Id(p2),Id(p3)])),AssignStmt(Id(area),CallExpr(Id(abc),Id(area),[])),Call(Id(io),Id(writeLn),[StringLit(Area of triangle: ),Id(area)])]))])])'

for i in range(len(a)):
    if a[i] != b[i]:
        print(i,"--",a[i],"--",b[i])
        break
    
    

import string
x = """
Program([
    ClassDecl(Id(Library), [
        AttributeDecl(Instance, VarDecl(Id(books), ArrayType(IntLit(5), ClassType(Id(Book))))),
        MethodDecl(Id(Library), Instance, [
            param(Id(b), ArrayType(IntLit(5), ClassType(Id(Book))))
        ], VoidType, Block([
            AssignStmt(FieldAccess(Self(), Id(books)), Id(b))
        ])),
        MethodDecl(Id(displayBooks), Instance, [], VoidType, Block([
            Call(Id(io), Id(writeStrLn), [StringLit(Library_Catalog:)]),
            ForStmt(
                Id(i),
                IntLit(0),
                FieldAccess(Id(books), Id(length)),
                True,
                Block([
                    Call(ArrayCell(Id(books), Id(i)), Id(displayInfo), [])
                ])
            )
        ]))
    ]),
    ClassDecl(Id(Test), [
        MethodDecl(Id(main), Static, [], VoidType, Block([
            VarDecl(Id(bookList), ArrayType(IntLit(3), ClassType(Id(Book)))),
            AssignStmt(ArrayCell(Id(bookList), IntLit(0)), NewExpr(Id(Book), [StringLit(Harry Potter), StringLit(J.K. Rowling)])),
            AssignStmt(ArrayCell(Id(bookList), IntLit(1)), NewExpr(Id(Book), [StringLit(The Hobbit, StringLit(J.K. Rowling)]))])
        ])
    ])
        
"""

# a=x.translate({ord(c): None for c in string.whitespace})
# with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/code/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/exp.txt', 'a') as f:
#     f.write(a+"\n---")




