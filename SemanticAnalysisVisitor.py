from SymbolTable import *


class SemanticAnalysisVisitor:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.line = 0

    def visit(self, node):
        if node.node.getRuleName() == "expr":
            self.visit_expr(node)
        elif node.node.getRuleName() == "variableDefinition":
            self.visit_variable_definition(node)
        elif node.node.getRuleName() == "variableDeclaration":
            self.visit_variable_declaration(node)
        elif node.node.getRuleName() == "nameIdentifier":
            self.visit_name_identifier(node)
        elif node.node.getRuleName() == "assignmentStatement":
            self.visit_assignment_statement(node)
        else:
            for child in node.children:
                self.visit(child)

    def visit_expr(self, node):
        self.line += 1
        for child in node.children:
            self.visit(child)

    def visit_assignment_statement(self, node):
        if node.children[0].node.getRuleName() == "nameIdentifier":
            var_name = node.children[0].children[0].node.getRuleName()
        else:
            var_name = node.children[0].children[1].children[0].node.getRuleName()
        if self.symbol_table.get_symbol(var_name) != None:
            check = self.symbol_table.get_symbol(var_name)[1]
            if check == "const":
                print(f"[ Error ] at line {self.line}: Can not assign variable {var_name} with type const")
                exit()
        else:
            print(f"[ Error ] at line {self.line}: Can not assign the undeclared variable {var_name} ")
            exit()
        for child in node.children:
            self.visit(child)
    def visit_variable_declaration(self, node):
        if node.parent.node.getRuleName() != "variableDefinition":
            var_name = node.children[1].children[0].node.getRuleName()
            # Check if the variable has already been defined in the current scope
            if self.symbol_table.get_symbol(var_name) is not None:
                print(f"[ Error ] at line {self.line}: Variable {var_name} has already been defined in the current scope")
                exit()
            # Check if the variable is not declared const
            extra = None
            if node.children[0].node.getRuleName() == "constWord":
                print(f"[ Error ] at line {self.line}: Variable {var_name} needs to be initialised because it is declared const")
                exit()
            elif node.children[0].node.getRuleName() == "pointerWord":
                extra = "pointer"


            # Add the variable to the symbol table
            if extra == "pointer":
                type = node.children[0].children[0].children[0].node.getRuleName()
            else:
                type = node.children[0].children[0].node.getRuleName()
            tempArray = [type, extra]
            self.symbol_table.insert_symbol(var_name, tempArray)

        # Visit its children
        for child in node.children:
            self.visit(child)




    def visit_variable_definition(self, node):
        # Check if the variable has already been defined in the current scope
        var_name = node.children[0].children[1].children[0].node.getRuleName()
        if self.symbol_table.get_symbol(var_name) is not None:
            print(f"[ Error ] at line {self.line}: Variable {var_name} has already been defined in the current scope")
            exit()

        # Add the variable to the symbol table
        extra = None
        if node.children[0].children[0].node.getRuleName() == "constWord":
            extra = "const"
        if node.children[0].children[0].node.getRuleName() != "reservedWord":
            if node.children[0].children[0].children[1].node.getRuleName() == "pointerWord":
                extra = "const pointer"
            if node.children[0].children[0].node.getRuleName() == "pointerWord":
                extra = "pointer"

        if extra == "const":
            type = node.children[0].children[0].children[1].children[0].node.getRuleName()
        elif extra == "pointer":
            type = node.children[0].children[0].children[0].children[0].node.getRuleName()
        elif extra == "const pointer":
            type = node.children[0].children[0].children[1].children[0].children[0].node.getRuleName()
        else:
            type = node.children[0].children[0].children[0].node.getRuleName()
        rightside = node.children[2]
        tempArray = [type, extra, rightside]
        self.symbol_table.insert_symbol(var_name, tempArray)

        # Visit its children
        for child in node.children:
            self.visit(child)

    def visit_name_identifier(self, node):
        # Check if the variable has been declared or initialised before it is used
        var_name = node.children[0].node.getRuleName()
        var_node = self.symbol_table.get_symbol(var_name)
        if var_node is None:
            print(f"[ Error ] at line {self.line}: Variable {var_name} has not been initialized or declared")
            exit()

        # Visit its children
        for child in node.children:
            self.visit(child)
