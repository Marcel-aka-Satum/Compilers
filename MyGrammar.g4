grammar MyGrammar;

prog: expr;

expr: opAnd ';' | opAnd ';' expr;

opAnd: opAnd '&&' opOr | opOr;

opOr: opOr '||' opCompare | opCompare;

opCompare: opCompare '==' opAddOrSub | opCompare '<=' opAddOrSub | opCompare '>=' opAddOrSub
	 | opCompare '!=' opAddOrSub | opCompare '<' opAddOrSub | opCompare '>' | opAddOrSub | opAddOrSub;

opAddOrSub: opAddOrSub '+' opMultOrDiv | opAddOrSub '-' opMultOrDiv | opMultOrDiv;

opMultOrDiv: opMultOrDiv '*' opUnary | opMultOrDiv '/' opUnary | opMultOrDiv '%' opUnary | opUnary;

opUnary: '+' brackets | '-' brackets | '!' brackets | brackets;

brackets: '(' opAnd ')' | variableDefinition | variableDeclaration | assignmentStatement | dataTypes;

variableDefinition: variableDeclaration '=' opAddOrSub;

variableDeclaration: constWord referenceID;

assignmentStatement: referenceID '=' opAddOrSub;

constWord: 'const' pointerWord | pointerWord;

pointerWord: reservedWord'*' | reservedWord;

reservedWord: 'int' | 'float' | 'char';

dataTypes: int | float | char | referenceID;

int: INT;

float: FLOAT;

char: CHAR;

referenceID: '&'nameIdentifier | nameIdentifier;

nameIdentifier: ID;

ID: [a-zA-Z]([a-zA-Z0-9_])*;
CHAR: '\'' [a-zA-Z] '\'';
INT: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+ | [0-9]+'.'[0-9]*;
WS: [ \t\r\n]+ -> skip;
