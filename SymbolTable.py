class SymbolTable:
    def __init__(self):
        self.symbol_tables = dict()
        self.scopes = dict()

    def insert_symbol(self, symbol_name, symbol_node, scope):
        set = {symbol_name: symbol_node}
        if scope in self.symbol_tables:
            self.symbol_tables[scope].update(set)
        else:
            self.symbol_tables[scope] = set
        if scope not in self.scopes:
            self.scopes[scope] = [None]

    def insert_value(self, symbol_name, value, scope):
        if scope in self.symbol_tables:
            if symbol_name in self.symbol_tables[scope]:
                self.symbol_tables[scope][symbol_name][2] = value
            else:
                arr = self.scopes[scope]
                for i in arr:
                    if i in self.symbol_tables:
                        if symbol_name in self.symbol_tables[i]:
                            self.symbol_tables[i][symbol_name][2] = value

        else:
            arr = self.scopes[scope]
            for i in arr:
                if i in self.symbol_tables:
                    if symbol_name in self.symbol_tables[i]:
                        self.symbol_tables[i][symbol_name][2] = value



    def get_symbol(self, symbol_name, scope):
        if scope in self.symbol_tables:
            if symbol_name in self.symbol_tables[scope]:
                return self.symbol_tables[scope][symbol_name]
            else:
                arr = self.scopes[scope]
                if arr != None:
                    for i in arr:
                        if i in self.symbol_tables:
                            if symbol_name in self.symbol_tables[i]:
                                return self.symbol_tables[i][symbol_name]
                else:
                    if None in self.symbol_tables:
                        if symbol_name in self.symbol_tables[None]:
                            return self.symbol_tables[None][symbol_name]
            return None
        else:
            if scope in self.scopes:
                arr = self.scopes[scope]
                if arr != None:
                    for i in arr:
                        if i in self.symbol_tables:
                            if symbol_name in self.symbol_tables[i]:
                                return self.symbol_tables[i][symbol_name]
                else:
                    if None in self.symbol_tables:
                        if symbol_name in self.symbol_tables[None]:
                            return self.symbol_tables[None][symbol_name]
            return None
