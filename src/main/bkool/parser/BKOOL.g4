//201177977
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// program  : mptype 'main' LB RB LP body? RP EOF ;

// mptype: INTTYPE | VOIDTYPE ;

// body: funcall SEMI;

// exp: funcall | INTLIT ;

// funcall: ID LB exp? RB ;

// INTTYPE: 'int' ;

// VOIDTYPE: 'void'  ;

// ID: [a-zA-Z]+ ;

// INTLIT: [0-9]+;

// LB: '(' ;

// RB: ')' ;

// LP: '{';

// RP: '}';

// SEMI: ';' ;

program: bkool EOF;

COMMENT: (BLOCK | LINE) ->skip;
fragment LINE: '#' (.*?) ('\r'? '\n'|EOF) ;
fragment BLOCK: '/*' .*? '*/';
//progam structure
bkool: classdecl bkool | classdecl;
classdecl: CLASS ID (EXTENDS ID)? LP listmember RP;
listmember: listmemberprime|;
listmemberprime: member SEMI listmemberprime | member SEMI;
member: attribute|method;
attribute: mutableatt|immutableatt;
mutableatt: (STATIC)? typ listatt; //expresion is ok?
immutableatt: FINAL (STATIC)? typ listatt
			| (STATIC)? FINAL typ listatt;
listatt: attributename COMMA listatt | attributename;
attributename: ID (EQ expression)?;
method: STATIC? typ ID LB listparameter RB blockstatement;
listparameter: listparameterprime | ;
listparameterprime: paradecl SEMI listparameterprime | paradecl;
paradecl: typ idlist;
idlist: ID COMMA idlist | ID;
constructor: ID LB listparameter blockstatement;


//statement
statement: blockstatement|assignmentstatement|ifstatement|; //not good
blockstatement: LP listblock RP;
listblock: blockdecllist blockbodylist;
blockdecllist: blockdeclprime| ;
blockdeclprime: blockdecl SEMI blockdeclprime| blockdecl;

blockbodylist: blockbodyprime| ;
blockbodyprime: statement SEMI blockbodyprime | statement;

blockdecl: arraydecl|vardecl; //all of them
vardecl: FINAL typ listatt;

// ASSIGN 
assignmentstatement: lhs ASSIGN expression SEMI;

lhs: indexexpression | localvariable | instanceattributeaccess|staticattributeaccess; //something like a.b 
localvariable: ID;

ifstatement: IF expression THEN statement ELSE statement; //expression or statement ?

forstatement: FOR ID ASSIGN expression (TO | DOWNTO) expression DO statement; //interger
breakstatment: BREAK SEMI;
continuestatement: CONTINUTE SEMI;
returnstatement: RETURN expression SEMI;
methodinvocationstatement: instancemethodinvocation|staticmethodinvocation SEMI;

// object creation
objectcreation: NEW ID listexpression;

// member access
memberaccess: instanceattributeaccess|staticattributeaccess|instancemethodinvocation|staticmethodinvocation;
instanceattributeaccess: expression DOT ID;
staticattributeaccess: ID DOT ID;
instancemethodinvocation: expression DOT ID listexpression;
staticmethodinvocation: ID DOT ID listexpression;



listexpression: expressionprime | ; //i think it can be null
expressionprime: expression COMMA expressionprime | expression;

expression: exp1 LT exp1| exp1 GT exp1| exp1 LET exp1| exp1 GET exp1| exp1;
exp1: exp2 EQE exp2| exp2 NEQ exp2| exp2;
exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUB exp4| exp4;
exp4: exp4 MUL exp5 | exp4 FDIV exp5| exp4 IDIV exp5| exp4 MOD exp5| exp5;
exp5: exp5 CONCATE exp6| exp6;
exp6: NOT exp6 | exp7; //hmmm
exp7: ADD exp7| SUB exp7 | exp8;
exp8: LSB exp9 RSB | exp9;
exp9: exp9 DOT exp10| exp10;
exp10: NEW exp10| ID; //id???




indexexpression: ID LSB index RSB; //ID IS ARRAY TYPE
index: INTLIT | indexexpression; //NOT MAKE SENSE


classcreate: NEW ID LB RB;

arraydecl: arraytype LSB INTLIT RSB ID;
arraytype: INTTYPE|FLOATYPE|STRINGTYPE|BOOLEANTYPE;

arraylist: LP array RP;
array: arrayelement COMMA array | arrayelement;
arrayelement: INTLIT | FLOATLIT | booleanlit | STRINGLIT;

intoperator: ADD|SUB|MUL|FDIV|LT|LET|EQ|GT|GET|EQE|NEQ|IDIV|MOD;
floatoperator: ADD|SUB|MUL|FDIV|LT|LET|GT|GET|EQ;
booloperator: EQE|NEQ|NOT|AND|OR;
stringoperator: CONCATE;


typ: INTTYPE|FLOATYPE|BOOLEANTYPE|STRINGTYPE;
INTTYPE:'int';
FLOATYPE: 'float';
BOOLEANTYPE: 'boolean';
STRINGTYPE:'string';
VOIDTYPE: 'void';
INTLIT: '-'?[1-9][0-9]*;
FLOATLIT: NUMBER DOT NUMBER | NUMBER EXPONENT;
fragment EXPONENT: ('e'|'E') ('+'|'-')? NUMBER;
fragment NUMBER: [0-9]+;
booleanlit: TRUE | FALSE;

STRINGLIT: '"' (ESC | ~[\r\n\\"])* '"'; 
fragment ESC: '\\' [bftnr"\\];

LB: '(' ; 	RB: ')' ;
LP: '{';	RP: '}';
LSB: '['; RSB: ']';
ASSIGN: ':=';
SEMI: ';' ; COMMA: ','; DOT: '.' ; COLON: ':';

TAB: '\t'; FF:'\f'; CR: '\r'; LR: '\n'; 
BS: '\b'; 
CLASS: 'class'; STATIC: 'static'; FINAL: 'final';
BREAK: 'break'; CONTINUTE: 'continue'; DO: 'do'; ELSE: 'else';
EXTENDS: 'extends';  IF: 'if'; NEW: 'new';
THEN: 'then'; FOR: 'for'; RETURN: 'return'; TRUE: 'true'; FALSE: 'false'; VOID:'void';
NIL: 'nil'; THIS: 'this'; TO: 'to'; DOWNTO: 'downto';
//operator
EQE: '=='; NEQ: '!=';  AND: '&&';
LET: '<='; GET: '>='; OR: '||';
ADD: '+'; SUB: '-'; MOD: '%';
MUL: '*'; FDIV: '/'; IDIV: '\\';
EQ: '='; LT: '<'; GT: '>';
NOT: '!'; CONCATE: '^'; 


ID: [a-zA-Z_][0-9A-Za-z_]* ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .{raise UnclosedString(self.text)};
ILLEGAL_ESCAPE: .{raise IllegalEscape(self.text)};