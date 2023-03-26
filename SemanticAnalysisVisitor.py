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
        check = None
        if self.symbol_table.get_symbol(var_name) != None:
            check = self.symbol_table.get_symbol(var_name)[1]
            if check == "const" or check == "const pointer":
                if check == "const pointer" and node.children[2].node.getRuleName() == "referenceID":
                    if node.children[0].node.getRuleName() == "referenceID":
                        if node.children[0].children[0].node.getRuleName() == "*":
                            print(f"[ Error ] at line {self.line}: Can not assign variable {var_name} with type const")
                            exit()
                else:
                    print(f"[ Error ] at line {self.line}: Can not assign variable {var_name} with type const")
                    exit()
        else:
            print(f"[ Error ] at line {self.line}: Can not assign the undeclared variable {var_name} ")
            exit()
        if check == "pointer":
            if node.children[2].node.getRuleName() != "referenceID":
                if node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName() != "*":
                        print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                        exit()
                else:
                    print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                    exit()
            if node.children[0].node.getRuleName() == "referenceID":
                type = self.symbol_table.get_symbol(var_name)[0]
                if node.children[0].children[0].node.getRuleName() == "*":
                    if node.children[2].node.getRuleName() == "nameIdentifier":
                        if type != "int" and type != "float" and type != "char":
                            print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            exit()
                    elif node.children[2].node.getRuleName() == "referenceID":
                        print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                        exit()


        type = self.symbol_table.get_symbol(var_name)[0]
        if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID" and node.children[2].children[0].node.getRuleName() != "*":
            if check != "pointer" and check != "const pointer":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type")
                exit()

        if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
            if (node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float") and type == "char":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char ")
                exit()
            elif node.children[2].node.getRuleName() == "char" and (type == "int" or type ==  "float"):
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float")
                exit()

            if type == "int":
                rightSide = int(node.children[2].children[0].node.getRuleName())
            elif type == "float":
                rightSide = float(node.children[2].children[0].node.getRuleName())
            else:
                rightSide = node.children[2].children[0].node.getRuleName()[1]
        elif node.children[2].node.getRuleName() == "nameIdentifier":
            type2 = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName())[0]
            if (type == "int" or type == "float") and type2 == "char":
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float")
                exit()
            elif type == "char" and (type2 == "int" or type2 == "float"):
                print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char")
                exit()
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
            tempArray = [type, extra, None]
            self.symbol_table.insert_symbol(var_name, tempArray)

        # Visit its children
        for child in node.children:
            self.visit(child)




    def visit_variable_definition(self, node):
        # Check if the variable has already been defined in the current scope
        var_name = node.children[0].children[1].children[0].node.getRuleName()
        if self.symbol_table.get_symbol(var_name) is not None:
            print(f"[ Error ] at line {self.line}: Variable {var_name} has already been defined in the current scope")
        else:
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
            if extra == "pointer" or extra == "const pointer":
                if node.children[2].node.getRuleName() != "referenceID":
                    print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an address")
                    exit()
                elif node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName() == "*":
                        if node.children[2].node.getRuleName() == "nameIdentifier":
                            if type != "int" and type != "float" and type != "char":
                                print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                                exit()
                        elif node.children[2].node.getRuleName() == "referenceID":
                            print(f"[ Error ] at line {self.line}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            exit()

            if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID":
                if extra != "pointer" and extra != "const pointer" and node.children[2].children[0].node.getRuleName() != "*":
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type")
                    exit()
            if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
                if (node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float") and type == "char":
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected char ")
                    exit()
                elif node.children[2].node.getRuleName() == "char" and (type == "int" or type ==  "float"):
                    print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int or float ")
                    exit()
                if type == "int":
                    try:
                        rightSide = int(node.children[2].children[0].node.getRuleName())
                    except:
                        print(f"[ Error ] at line {self.line}: {var_name} got assigned an incompatible type: expected int")
                        exit()
                elif type == "float":
                    rightSide = float(node.children[2].children[0].node.getRuleName())
                else:
                    rightSide = node.children[2].children[0].node.getRuleName()[1]
            else:
                rightSide = node.children[2]
            tempArray = [type, extra, rightSide]
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