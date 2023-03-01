grammar MyGrammar;
prog:   (expr)*;
expr:   expr ('+'|'-'|'*'|'/') expr
    |   expr ('<'|'>'|'==') expr
    |   '(' expr ')'
    |	expr ('&&'|'||'|'!') expr
    |	expr ('<='|'>='|'!=') expr
    |	expr ('%') expr
    |	'-' expr
    |	'+' expr
    |	INT
    ;
NEWLINE : [\r\n]+ -> skip;
INT     : [0-9]+ ;
WS	: [\n\t\r]+ -> skip;
