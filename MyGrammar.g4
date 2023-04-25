grammar MyGrammar;

prog: expr;

expr: opAnd ';' | opAnd ';' expr | comment expr | funcDefinition expr | variableDefinition expr
    | variableDeclaration ';' expr | assignmentStatement ';' expr | printFunction expr | unNamedScope expr
    | conditionStatement expr | BREAK ';' expr | CONTINUE ';' expr |;

opAnd: opAnd '&&' opOr | opOr;

opOr: opOr '||' opCompare | opCompare;

opCompare: opCompare '==' opAddOrSub | opCompare '<=' opAddOrSub | opCompare '>=' opAddOrSub
	 | opCompare '!=' opAddOrSub | opCompare '<' opAddOrSub | opCompare '>' opAddOrSub | opAddOrSub;

opAddOrSub: opAddOrSub '+' opMultOrDiv | opAddOrSub '-' opMultOrDiv | opMultOrDiv;

opMultOrDiv: opMultOrDiv '*' opUnary | opMultOrDiv '/' opUnary | opMultOrDiv '%' opUnary | opUnary;

opUnary: '+' brackets | '-' brackets | '!' brackets | brackets;

brackets: '(' opAnd ')' | dataTypes;

variableDefinition: variableDeclaration '=' opAnd ';';

variableDeclaration: constWord referenceID;

assignmentStatement: referenceID '=' opAddOrSub | dataTypes '=' opAddOrSub | '(' opAnd ')' '=' opAnd;

constWord: 'const' pointerWord | pointerWord;

pointerWord: reservedWord POINTER | reservedWord POINTERS | reservedWord;

reservedWord: 'int' | 'float' | 'char';

dataTypes: int | float | char | referenceID;

int: INT;

float: FLOAT;

char: CHAR;

referenceID: '&'nameIdentifier | POINTER nameIdentifier | POINTERS nameIdentifier | nameIdentifier;

nameIdentifier: ID;

conditionStatement: ifStatement (elifStatement)* (elseStatement)? | whileStatement | forLoop;

printFunction: 'printf' '(' opAnd ')' ';';

ifStatement: 'if' '(' opAnd ')' '{' body '}';

elifStatement: 'else' 'if' '(' opAnd ')' '{' body '}';

elseStatement: 'else' '{' body '}';

whileStatement: 'while' '(' opAnd ')' '{' body '}';

forLoop: 'for' '(' ((variableDeclaration ';' | variableDefinition | assignmentStatement ';') opAnd ';' assignmentStatement
| ';' ';') ')' '{' body '}';

unNamedScope: '{' body '}';

comment: BLOCK_COMMENT+ | COMMENT+;

argument: referenceID;

funcDefinition: 'int' ID '(' argument* ')' '{' body '}';

body: expr;

POINTER: '*';
POINTERS: ('*')+;
BREAK: 'break';
CONTINUE: 'continue';
ID: [a-zA-Z]([a-zA-Z0-9_])*;
CHAR: '\'' ([a-zA-Z] | INT | .)'\'';
INT: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+ | [0-9]+'.'[0-9]*;
COMMENT: '//' .*? '\r'? '\n';
BLOCK_COMMENT: '/*' .*? '*/';
WS: [ \t\r\n]+ -> skip;