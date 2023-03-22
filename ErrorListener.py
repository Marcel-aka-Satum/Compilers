from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = "Syntax error at line {}, column {}: {}".format(line, column, msg)
        raise ValueError(error_message)