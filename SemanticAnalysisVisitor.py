from SymbolTable import *

class SemanticAnalysisVisitor:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visit(self, node):
        if node.node.getRuleName() == "prog":
            self.visit_prog(node)
        elif node.node.getRuleName() == "expr":
            self.visit_expr(node)
        elif node.node.getRuleName() == "variableDefinition":
            self.visit_variable_definition(node)
        elif node.node.getRuleName() == "nameIdentifier":
            self.visit_name_identifier(node)

    def visit_prog(self, node):
        for child in node.children:
            self.visit(child)

    def visit_expr(self, node):
        for child in node.children:
            self.visit(child)

    def visit_variable_definition(self, node):
        # Check if the variable has already been defined in the current scope
        var_name = node.children[0].children[1].children[0].node.getRuleName()
        for i in self.symbol_table.symbol_tables:
            if var_name in i:
                print(f"Error: Variable {var_name} already defined in the current scope")
                return
        # Add the variable to the symbol table
        newdict = dict()
        newdict[var_name] = node
        self.symbol_table.symbol_tables[len(self.symbol_table.symbol_tables)-1] = newdict

    def visit_name_identifier(self, node):
        # Check if the variable has been defined in the symbol table
        var_name = node.children[0].node.getRuleName()
        for i in self.symbol_table.symbol_tables:
            if var_name in i:
                print(f"Error: Variable {var_name} not defined")
                return
        # Check if the variable has been initialized before it is used
        var_node = self.symbol_table.symbol_tables.get_symbol(var_name)
        if var_node.children[1] is None:
            print(f"Error: Variable {var_name} has not been initialized")
    
