grammar MyGrammar;

prog: expr;

expr: opAnd ';' | opAnd ';' expr | comment expr | funcDefinition expr |;

opAnd: opAnd '&&' opOr | opOr;

opOr: opOr '||' opCompare | opCompare;

opCompare: opCompare '==' opAddOrSub | opCompare '<=' opAddOrSub | opCompare '>=' opAddOrSub
	 | opCompare '!=' opAddOrSub | opCompare '<' opAddOrSub | opCompare '>' opAddOrSub | opAddOrSub;

opAddOrSub: opAddOrSub '+' opMultOrDiv | opAddOrSub '-' opMultOrDiv | opMultOrDiv;

opMultOrDiv: opMultOrDiv '*' opUnary | opMultOrDiv '/' opUnary | opMultOrDiv '%' opUnary | opUnary;

opUnary: '+' brackets | '-' brackets | '!' brackets | brackets;

brackets: '(' opAnd ')' | variableDefinition | variableDeclaration | assignmentStatement | dataTypes | printFunction;

variableDefinition: variableDeclaration '=' opAnd;

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

printFunction: 'printf' '(' opAnd ')';

comment: BLOCK_COMMENT+ | COMMENT+;

argument: referenceID;

funcDefinition: 'int' ID '(' argument* ')' '{' body '}';

body: expr;

POINTER: '*';
POINTERS: ('*')+;
ID: [a-zA-Z]([a-zA-Z0-9_])*;
CHAR: '\'' ([a-zA-Z] | INT | .)'\'';
INT: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+ | [0-9]+'.'[0-9]*;
COMMENT: '//' .*? '\r'? '\n';
BLOCK_COMMENT: '/*' .*? '*/';
WS: [ \t\r\n]+ -> skip;