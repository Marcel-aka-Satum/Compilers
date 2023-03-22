class SymbolTable:
    def __init__(self):
        self.symbol_tables = [{}]
    
    def enter_scope(self):
        # Add a new empty symbol table for the new scope level
        self.symbol_tables.append({})
    
    def exit_scope(self):
        # Remove the current symbol table for the current scope level
        self.symbol_tables.pop()
    
    def declare(self, identifier, value=None):
        # Add a new identifier to the current symbol table
        current_table = self.symbol_tables[-1]
        if identifier in current_table:
            raise Exception("Error: identifier '{}' already declared in this scope".format(identifier))
        current_table[identifier] = value
    
    def assign(self, identifier, value):
        # Update the value of an existing identifier in the current or parent symbol tables
        for table in reversed(self.symbol_tables):
            if identifier in table:
                table[identifier] = value
                return
        raise Exception("Error: identifier '{}' not declared".format(identifier))
    
    def lookup(self, identifier):
        # Look up the value of an identifier in the current or parent symbol tables
        for table in reversed(self.symbol_tables):
            if identifier in table:
                return table[identifier]
        raise Exception("Error: identifier '{}' not declared".format(identifier))
