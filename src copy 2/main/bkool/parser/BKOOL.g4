//2011797
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
//------------------------- progam structure -------------------------
bkool: classdecl bkool | classdecl;
classdecl: CLASS ID (EXTENDS ID)? LP listmember RP;
listmember: listmemberprime |;
listmemberprime: member listmemberprime | member;
member: attribute
		| method
		| constructor;
attribute: (mutableatt|immutableatt) SEMI;
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
constructor: STATIC? ID LB listparameter RB blockstatement;


//------------------------ statement ------------------------
statement: blockstatement
		|assignmentstatement
		|ifstatement
		|forstatement
		|breakstatment
		|continuestatement
		|returnstatement
		|methodinvocationstatement; //not good

blockstatement: LP listblock RP;
listblock: blockdecllist blockbodylist;
blockdecllist: blockdeclprime| ;
blockdeclprime: blockdecl blockdeclprime| blockdecl;

blockbodylist: blockbodyprime| ;
blockbodyprime: statement blockbodyprime | statement;

blockdecl: vardecl SEMI; //all of them
vardecl: FINAL? typ listatt;

// ASSIGN 
assignmentstatement: lhs ASSIGN expression SEMI;

lhs: indexexpression | ID | instanceattributeaccess|staticattributeaccess; //something like a.b 


ifstatement: IF expression THEN statement (ELSE statement)?; //expression or statement ?

forstatement: FOR ID ASSIGN expression (TO | DOWNTO) expression DO statement; //interger
breakstatment: BREAK SEMI;
continuestatement: CONTINUTE SEMI;
returnstatement: RETURN expression SEMI;
methodinvocationstatement: (instancemethodinvocation|staticmethodinvocation) SEMI;

// object creation
//objectcreation: NEW ID listexpression;


expression: exp1 LT exp1| exp1 GT exp1| exp1 LET exp1| exp1 GET exp1| exp1;
exp1: exp2 EQE exp2| exp2 NEQ exp2| exp2;
exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUB exp4| exp4;
exp4: exp4 MUL exp5 | exp4 FDIV exp5| exp4 IDIV exp5| exp4 MOD exp5| exp5;
exp5: exp5 CONCATE exp6| exp6;
exp6: NOT exp6 | exp7; //hmmm
exp7: ADD exp7| SUB exp7 | exp8  ;
exp8: exp9 LSB expression RSB | exp9 | literal |NIL; //test later
exp9: exp9 DOT (ID |methodinvocation) | exp10; //| exp9 DOT ID
//exp9: memberaccess| exp10;
exp10: classcreate | exp11;
//exp10: classcreate| ID | literal;
exp11: LB expression RB | ID | THIS |IO;

//member access
memberaccess: instanceattributeaccess|staticattributeaccess|instancemethodinvocation|staticmethodinvocation;
instanceattributeaccess: exp9 DOT ID; //(ID|THIS|IO)
staticattributeaccess: ID DOT ID;
instancemethodinvocation: exp9 DOT ID LB listexpression RB;
staticmethodinvocation: ID DOT ID LB listexpression RB; 
//think at night
methodinvocation: ID LB listexpression RB;


listexpression: expressionprime | ; //i think it can be null
expressionprime: expression COMMA expressionprime | expression;


literal: INTLIT | FLOATLIT | BOOLIT | STRINGLIT|arraylit;



indexexpression: exp9 LSB expression RSB; //ID IS ARRAY TYPE
//NOT MAKE SENSE


classcreate: NEW ID LB listexpression RB;



arraylit: LP array RP;
array: arrayelement COMMA array | arrayelement;
arrayelement: INTLIT | FLOATLIT | BOOLIT | STRINGLIT;

intoperator: ADD|SUB|MUL|FDIV|LT|LET|EQ|GT|GET|EQE|NEQ|IDIV|MOD;
floatoperator: ADD|SUB|MUL|FDIV|LT|LET|GT|GET|EQ;
booloperator: EQE|NEQ|NOT|AND|OR;
stringoperator: CONCATE;


typ: INTTYPE|FLOATYPE|BOOLEANTYPE|STRINGTYPE|VOIDTYPE|ID|arraytyp;
arraytyp: (INTTYPE|FLOATYPE|BOOLEANTYPE|STRINGTYPE|ID)  LSB INTLIT RSB ;

INTTYPE:'int';
FLOATYPE: 'float';
BOOLEANTYPE: 'boolean';
STRINGTYPE:'string';
VOIDTYPE: 'void';

BOOLIT: TRUE | FALSE;
fragment TRUE: 'true';
fragment FALSE: 'false';

STRINGLIT: '"' (ESC | ~[\r\n\\"])* '"'; 
fragment ESC: '\\' [bftnr"\\];
fragment ILL_ESC: '\\' ~[bftnr"\\];


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
THEN: 'then'; FOR: 'for'; RETURN: 'return'; VOID:'void';
NIL: 'nil'; THIS: 'this'; TO: 'to'; DOWNTO: 'downto';
IO: 'io';
ID: [a-zA-Z_][0-9A-Za-z_]*;
FLOATLIT: NUMBER EXPONENT
		|NUMBER DOT NUMBER?
		|NUMBER DOT NUMBER? EXPONENT;
fragment EXPONENT: ('e'|'E') ('+'|'-')? NUMBER;
fragment NUMBER: [0-9]+;
INTLIT: [1-9][0-9]*| '0';
//operator

EQE: '=='; NEQ: '!=';  AND: '&&';
LET: '<='; GET: '>='; OR: '||';
ADD: '+'; SUB: '-'; MOD: '%';
MUL: '*'; FDIV: '/'; IDIV: '\\';
EQ: '='; LT: '<'; GT: '>';
NOT: '!'; CONCATE: '^'; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: ('"' (ESC | ~[\t\b\f\r\n\\"])* EOF?) {
	ustr= str(self.text)
	raise UncloseString(ustr[1:])
};
ILLEGAL_ESCAPE: ('"' (~[\b\t\f\r\n\\"]|ESC)* ILL_ESC) {
	istr= str(self.text)
	raise IllegalEscape(istr[1:])
};
ERROR_CHAR: .{raise ErrorToken(self.text)};
