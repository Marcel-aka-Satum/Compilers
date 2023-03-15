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

brackets: '(' opAnd ')' | int | float;

int: INT;

float: FLOAT;

INT: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+ | [0-9]+'.'[0-9]*;
WS: [ \t\r\n]+ -> skip;
