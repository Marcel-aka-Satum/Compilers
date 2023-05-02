from antlr4.error.ErrorListener import ErrorListener


class errorAnalysis(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line, {line}, and column {column}, {msg} ")