testcase305:Program([ClassDecl(Id(Rectangle),[MethodDecl(Instance,Id(getArea),[],FloatType,Block([],[(Return(BinaryOp(*,FieldAccess(SelfLiteral(),Id(length)),FieldAccess(SelfLiteral(),Id(width)))))]))])],Id(Shape))])
---
testcase306:Program([ClassDecl(Id(Rectangle),[MethodDecl(Instance,Id(getArea),[],FloatType,Block([],[(Return(BinaryOp(*,FieldAccess(SelfLiteral(),Id(length)),FieldAccess(SelfLiteral(),Id(width)))))])),MethodDecl(Instance,Id(getLength),[],FloatType,Block([],[(Return(BinaryOp(+,FieldAccess(SelfLiteral(),Id(length)),FieldAccess(SelfLiteral(),Id(width)))))]))])],Id(Shape))])
---
testcase307:Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),AttributeDecl(Static,MethodDecl(Static,Id(getNumOfShape),[],IntType,Block([],[(Return(FieldAccess(SelfLiteral(),Id(numOfShape))))]))])])])
---
testcase308:Program([ClassDecl(Id(Rectangle),[MethodDecl(Instance,Id(getArea),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),IntType)],FloatType,Block([],[(Return(BinaryOp(*,FieldAccess(SelfLiteral(),Id(length)),FieldAccess(SelfLiteral(),Id(width)))))]))])])
---