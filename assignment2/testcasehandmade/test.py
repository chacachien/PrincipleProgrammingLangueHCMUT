a="""Program([ClassDecl(Id(Bank),[AttributeDecl(Instance,VarDecl(Id(interestRate),FloatType)),MethodDecl(Id(Bank),Instance,[param(Id(rate),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(interestRate)),Id(rate))])),MethodDecl(Id(calculateInterest),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(*,Id(principal),FieldAccess(Self(),Id(interestRate))))]))]),ClassDecl(Id(SavingsAccount),Id(Bank),[MethodDecl(Id(SavingsAccount),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(+,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),IntLit(100)))]))]),ClassDecl(Id(FixedDeposit),Id(Bank),[MethodDecl(Id(FixedDeposit),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType),param(Id(years),IntType)],FloatType,Block([],[Return(BinaryOp(*,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),Id(years)))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bank1),ClassType(Id(Bank))),VarDecl(Id(bank2),ClassType(Id(Bank))),VarDecl(Id(principal),FloatType,FloatLit(1000.0)),VarDecl(Id(interest1),FloatType),VarDecl(Id(interest2),FloatType)],[AssignStmt(Id(bank1),NewExpr(Id(SavingsAccount),[FloatLit(0.05)])),AssignStmt(Id(bank2),NewExpr(Id(FixedDeposit),[FloatLit(0.08)])),AssignStmt(Id(interest1),CallExpr(Id(bank1),Id(calculateInterest),[Id(principal)])),AssignStmt(Id(interest2),CallExpr(Id(bank2),Id(calculateInterest),[Id(principal),IntLit(5)])),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Savings_Account:),Id(interest1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Fixed Deposit:),Id(interest2))])]))])])"""
b="""Program([ClassDecl(Id(Bank),[AttributeDecl(Instance,VarDecl(Id(interestRate),FloatType)),MethodDecl(Id(Bank),Instance,[param(Id(rate),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(interestRate)),Id(rate))])),MethodDecl(Id(calculateInterest),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(*,Id(principal),FieldAccess(Self(),Id(interestRate))))]))]),ClassDecl(Id(SavingsAccount),Id(Bank),[MethodDecl(Id(SavingsAccount),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(+,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),IntLit(100)))]))]),ClassDecl(Id(FixedDeposit),Id(Bank),[MethodDecl(Id(FixedDeposit),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType),param(Id(years),IntType)],FloatType,Block([],[Return(BinaryOp(*,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),Id(years)))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bank1),ClassType(Id(Bank))),VarDecl(Id(bank2),ClassType(Id(Bank))),VarDecl(Id(principal),FloatType,FloatLit(1000.0)),VarDecl(Id(interest1),FloatType),VarDecl(Id(interest2),FloatType)],[AssignStmt(Id(bank1),NewExpr(Id(SavingsAccount),[FloatLit(0.05)])),AssignStmt(Id(bank2),NewExpr(Id(FixedDeposit),[FloatLit(0.08)])),AssignStmt(Id(interest1),CallExpr(Id(bank1),Id(calculateInterest),[Id(principal)])),AssignStmt(Id(interest2),CallExpr(Id(bank2),Id(calculateInterest),[Id(principal),IntLit(5)])),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Savings_Account:),Id(interest1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Fixed_Deposit:),Id(interest2))])]))])])"""
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

a=x.translate({ord(c): None for c in string.whitespace})
with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/code/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/exp.txt', 'a') as f:
    f.write(a+"\n---")

