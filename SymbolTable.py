class SymbolTable:
    def __init__(self):
        self.symbol_tables = [{}]

    def insert_symbol(self, symbol_name, symbol_node):
        self.symbol_tables[-1][symbol_name] = symbol_node

    def get_symbol(self, symbol_name):
        for symbol_table in reversed(self.symbol_tables):
            if symbol_name in symbol_table:
                return symbol_table[symbol_name]
        return None

    def enter_scope(self):
        self.symbol_tables.append({})

    def exit_scope(self):
        self.symbol_tables.pop()