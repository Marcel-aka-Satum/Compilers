from SymbolTable import *


class SemanticAnalysisVisitor:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.line = 0
        self.error = False

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
        elif node.node.getRuleName() == "comment":
            self.visit_comment(node)
        else:
            for child in node.children:
                self.visit(child)

    def visit_expr(self, node):
        self.line += 1
        for child in node.children:
            self.visit(child)

    def visit_comment(self, node):
        comment = node.children[0].node.getRuleName()
        nlines = len(comment.splitlines())
        self.line += nlines

    def visit_assignment_statement(self, node):
        if node.children[0].node.getRuleName() != "nameIdentifier" and node.children[0].node.getRuleName() != "referenceID":
            print(f"[ Error ] at line {self.line}: assignment to an rvalue")
            self.error = True
        if node.children[0].node.getRuleName() == "nameIdentifier":
            var_name = node.children[0].children[0].node.getRuleName()
        else:
            var_name = node.children[0].children[1].children[0].node.getRuleName()
        check = None
        if self.symbol_table.get_symbol(var_name) != None:
            check = self.symbol_table.get_symbol(var_name)[1][0]
            if check == "const" or check == "const pointer":
                if check == "const pointer" and node.children[2].node.getRuleName() == "referenceID":
                    if node.children[0].node.getRuleName() == "referenceID":
                        if node.children[0].children[0].node.getRuleName() == "*":
                            print(f"[ Error ] at line {self.line}: Can not assign variable {var_name} with type const")
                            self.error = True
                else:
                    print(f"[ Error ] at line {self.line}: Can not assign variable {var_name} with type const")
                    self.error = True
        else:
            print(f"[ Error ] at line {self.line}: Can not assign the undeclared variable {var_name} ")
            self.error = True
        if check == "pointer":
            if node.children[2].node.getRuleName() != "referenceID":
                if node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName()[0] != '*':
                        print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                        self.error = True
                    else:
                        size = self.symbol_table.get_symbol(var_name)[1][1]
                        if len(node.children[0].children[0].node.getRuleName()) != size:
                            print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects a {size} pointer")
                            self.error = True
                else:
                    print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                    self.error = True
            if node.children[0].node.getRuleName() == "referenceID":
                type = self.symbol_table.get_symbol(var_name)[0]
                if node.children[0].children[0].node.getRuleName()[0] == '*':
                    if node.children[2].node.getRuleName() == "nameIdentifier":
                        if type != "int" and type != "float" and type != "char":
                            print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            self.error = True
                    elif node.children[2].node.getRuleName() == "referenceID":
                        print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                        self.error = True

        type = self.symbol_table.get_symbol(var_name)[0]
        if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID" and node.children[2].children[0].node.getRuleName() != "*":
            if check != "pointer" and check != "const pointer":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type")
                self.error = True

        if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
            if (node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float") and type == "char":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char ")
                self.error = True
            elif node.children[2].node.getRuleName() == "char" and (type == "int" or type ==  "float"):
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float")
                self.error = True

            if type == "int":
                try:
                    rightSide = int(node.children[2].children[0].node.getRuleName())
                except ValueError:
                    rightSide = float(node.children[2].children[0].node.getRuleName())
                    rightSide = int(rightSide)
            elif type == "float":
                rightSide = float(node.children[2].children[0].node.getRuleName())
            else:
                rightSide = node.children[2].children[0].node.getRuleName()[1]
        elif node.children[2].node.getRuleName() == "nameIdentifier":
            type2 = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName())[0]
            if (type == "int" or type == "float") and type2 == "char":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float")
                self.error = True
            elif type == "char" and (type2 == "int" or type2 == "float"):
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char")
                self.error = True
            rightSide = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName())[2]
        else:
            rightSide = node.children[2]
        self.symbol_table.insert_value(var_name, rightSide)

        for child in node.children:
            self.visit(child)
    def visit_variable_declaration(self, node):
        if node.parent.node.getRuleName() != "variableDefinition":
            var_name = node.children[1].children[0].node.getRuleName()
            # Check if the variable has already been defined in the current scope
            if self.symbol_table.get_symbol(var_name) is not None:
                print(f"[ Error ] at line {self.line}: Variable {var_name} has already been defined in the current scope")
                self.error = True
            # Check if the variable is not declared const
            extra = None
            size = None
            if node.children[0].node.getRuleName() == "constWord":
                print(f"[ Error ] at line {self.line}: Variable {var_name} needs to be initialised because it is declared const")
                self.error = True
            elif node.children[0].node.getRuleName() == "pointerWord":
                extra = "pointer"
                size = len(node.children[0].children[1].node.getRuleName())


            # Add the variable to the symbol table
            if extra == "pointer":
                type = node.children[0].children[0].children[0].node.getRuleName()
            else:
                type = node.children[0].children[0].node.getRuleName()
            tempArray = [type, [extra, size], None]
            self.symbol_table.insert_symbol(var_name, tempArray)

        # Visit its children
        for child in node.children:
            self.visit(child)




    def visit_variable_definition(self, node):
        # Check if the variable has already been defined in the current scope
        var_name = node.children[0].children[1].children[0].node.getRuleName()
        if self.symbol_table.get_symbol(var_name) is not None:
            print(f"[ Error ] at line {self.line}: Variable {var_name} has already been defined in the current scope")
            self.error = True
        else:
            # Add the variable to the symbol table
            extra = None
            size = None
            if node.children[0].children[0].node.getRuleName() == "constWord":
                extra = "const"
            if node.children[0].children[0].node.getRuleName() != "reservedWord":
                if node.children[0].children[0].children[1].node.getRuleName() == "pointerWord":
                    extra = "const pointer"
                    size = len(node.children[0].children[0].children[1].children[1].node.getRuleName())
                if node.children[0].children[0].node.getRuleName() == "pointerWord":
                    extra = "pointer"
                    size = len(node.children[0].children[0].children[1].node.getRuleName())
            if extra == "const":
                type = node.children[0].children[0].children[1].children[0].node.getRuleName()
            elif extra == "pointer":
                type = node.children[0].children[0].children[0].children[0].node.getRuleName()
            elif extra == "const pointer":
                type = node.children[0].children[0].children[1].children[0].children[0].node.getRuleName()
            else:
                type = node.children[0].children[0].children[0].node.getRuleName()
            if extra == "pointer" or extra == "const pointer":
                if node.children[2].node.getRuleName() != "referenceID":
                    print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                    self.error = True
                elif node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName() == "*":
                        if node.children[2].node.getRuleName() == "nameIdentifier":
                            if type != "int" and type != "float" and type != "char":
                                print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                                self.error = True
                        elif node.children[2].node.getRuleName() == "referenceID":
                            print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            self.error = True

            if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID":
                if extra != "pointer" and extra != "const pointer":
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type")
                    self.error = True
                else:
                    if node.children[2].children[0].node.getRuleName() != "&":
                        print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type")
                        self.error = True
            if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
                if (node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float") and type == "char":
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char ")
                    self.error = True
                elif node.children[2].node.getRuleName() == "char" and (type == "int" or type == "float"):
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float ")
                    self.error = True
                if type == "int":
                    try:
                        rightSide = int(node.children[2].children[0].node.getRuleName())
                    except ValueError:
                        rightSide = float(node.children[2].children[0].node.getRuleName())
                        rightSide = int(rightSide)
                elif type == "float":
                    rightSide = float(node.children[2].children[0].node.getRuleName())
                else:
                    rightSide = node.children[2].children[0].node.getRuleName()[1]
            else:
                rightSide = node.children[2]

            tempArray = [type, [extra, size], rightSide]
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
            self.error = True

        # Visit its children
        for child in node.children:
            self.visit(child)
