class ASTVisitor:
    def visit_AST(self, ast):
        print("Visiting AST node:", ast.node.getRuleName())
        if ast.node.getRuleName() == "prog":
            self.visit_prog(ast)
        elif ast.node.getRuleName() == "expr":
            self.visit_expr(ast)
        elif ast.node.getRuleName() == "variableDefinition":
            self.visit_variable_definition(ast)
        elif ast.node.getRuleName() == "nameIdentifier":
            self.visit_name_identifier(ast)
        elif ast.node.getRuleName() == "int":
            self.visit_int(ast)
        elif ast.node.getRuleName() == "float":
            self.visit_float(ast)
        elif ast.node.getRuleName() == "char":
            self.visit_char(ast)
        elif ast.node.getRuleName() == "opAddOrSub":
            self.visit_op_add_or_sub(ast)
        elif ast.node.getRuleName() == "opMultOrDiv":
            self.visit_op_mult_or_div(ast)

    def visit_prog(self, ast):
        print("Visiting prog node")
        for child in ast.children:
            self.visit_AST(child)

    def visit_expr(self, ast):
        print("Visiting expr node")
        for child in ast.children:
            self.visit_AST(child)

    def visit_variable_definition(self, ast):
        print("Visiting variable definition node")
        for child in ast.children:
            self.visit_AST(child)

    def visit_name_identifier(self, ast):
        print("Visiting name identifier node")

    def visit_int(self, ast):
        print("Visiting int node")

    def visit_float(self, ast):
        print("Visiting float node")

    def visit_char(self, ast):
        print("Visiting char node")

    def visit_op_add_or_sub(self, ast):
        print("Visiting add or sub node")
        for child in ast.children:
            self.visit_AST(child)

    def visit_op_mult_or_div(self, ast):
        print("Visiting mult or div node")
        for child in ast.children:
            self.visit_AST(child)
