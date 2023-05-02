grammar MyGrammar;

prog: expr;

expr: opAnd ';' | opAnd ';' expr | comment expr | funcDefinition expr | funcDeclaration expr | functionCall ';' expr
    | variableDefinition expr | variableDeclaration ';' expr | arrAssign expr | assignmentStatement ';' expr | printFunction expr
    | unNamedScope expr | conditionStatement expr | BREAK ';' expr | CONTINUE ';' expr | returnStatement expr
    | arrDecl expr | arrDef expr | lib expr | scanFunction expr |;

opAnd: opAnd '&&' opOr | opOr;

opOr: opOr '||' opCompare | opCompare;

opCompare: opCompare '==' opAddOrSub | opCompare '<=' opAddOrSub | opCompare '>=' opAddOrSub
	 | opCompare '!=' opAddOrSub | opCompare '<' opAddOrSub | opCompare '>' opAddOrSub | opAddOrSub;

opAddOrSub: opAddOrSub '+' opMultOrDiv | opAddOrSub '-' opMultOrDiv | opMultOrDiv;

opMultOrDiv: opMultOrDiv '*' opUnary | opMultOrDiv '/' opUnary | opMultOrDiv '%' opUnary | opUnary;

opUnary: '+' brackets | '-' brackets | '!' brackets | brackets;

brackets: '(' opAnd ')' | dataTypes;

variableDefinition: variableDeclaration '=' (opAnd | functionCall | arrCall) ';';

variableDeclaration: constWord referenceID;

assignmentStatement: referenceID '=' (opAddOrSub | functionCall | arrCall) | dataTypes '=' opAddOrSub | '(' opAnd ')' '=' opAnd;

constWord: 'const' pointerWord | pointerWord;

pointerWord: reservedWord POINTER | reservedWord POINTERS | reservedWord;

reservedWord: 'int' | 'float' | 'char' | 'void';

dataTypes: int | float | char | referenceID | functionCall | arrCall;

int: INT;

float: FLOAT;

char: CHAR;

string: STRING;

referenceID: '&'nameIdentifier | POINTER nameIdentifier | POINTERS nameIdentifier | nameIdentifier;

nameIdentifier: ID;

conditionStatement: ifStatement (elifStatement)* (elseStatement)? | whileStatement | forLoop;

printFunction: 'printf' '(' printArg ')' ';';

scanFunction: 'scanf' '(' scanArg ')' ';';

scanArg: (string ',' (referenceID ',')*(referenceID)) | string;

printArg: (string ',' (opAnd ',')*(opAnd)) | string;

ifStatement: 'if' '(' opAnd ')' '{' body '}';

elifStatement: 'else' 'if' '(' opAnd ')' '{' body '}';

elseStatement: 'else' '{' body '}';

whileStatement: 'while' '(' opAnd ')' '{' body '}';

forLoop: 'for' '(' ((variableDeclaration ';' | variableDefinition | assignmentStatement ';') opAnd ';' assignmentStatement
| ';' ';') ')' '{' body '}';

unNamedScope: '{' body '}';

comment: BLOCK_COMMENT+ | COMMENT+;

argument: (constWord (ID)? ',')*(constWord (ID)?) |;

funcDefinition: constWord ID '(' argument ')' '{' body '}';

funcDeclaration: constWord ID '(' argument ')' ';';

argumentCall: ((ID | opAnd) ',')*(ID | opAnd) |;

functionCall: ID '(' argumentCall ')';

arrDecl: constWord ID '[' (INT | nameIdentifier) ']' ';';

arrDef: constWord ID '[' (INT | nameIdentifier) ']' '=' arrArg ';';

arrCall: nameIdentifier '[' (INT | nameIdentifier) ']';

arrArg: '{' (dataTypes ',')* (dataTypes)? '}' | '{' '}';

arrAssign: ID '[' (INT | nameIdentifier) ']' '=' dataTypes ';';

lib: '#include' '<stdio.h>';

body: expr;

returnStatement: 'return' opAnd ';';

POINTER: '*';
POINTERS: ('*')+;
BREAK: 'break';
CONTINUE: 'continue';
ID: [a-zA-Z]([a-zA-Z0-9_])*;
CHAR: ['].[']|['][\\].['];
STRING: '\'' (~'"' | '\'' )* '\'' | '"' (~'"' | '\'' )* '"' | CHAR;
INT: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+ | [0-9]+'.'[0-9]*;
COMMENT: '//' .*? '\r'? '\n';
BLOCK_COMMENT: '/*' .*? '*/';
WS: [ \t\r\n]+ -> skip;