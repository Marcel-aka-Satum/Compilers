from AST import *

#class that will generate output file with converted c code into LLVM tested with tool godbolt.org
#• Language: C
#• Compiler: x86-64 clang 16.0.0
#• Compiler options: -S -emit-llvm
class LLVM:
    def __init__(self) -> None:
        self.output = ""

    def generate_LLVM(self, table):
        #loop through symbolTable
        for dict1 in table:
            #loop through dicts of table (can have multiple scopes)
            for key in dict1:
                if(dict1[key][0] == 'int'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant i32 {dict1[key][2]}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global i32 {dict1[key][2]}, allign 4\n"
                elif(dict1[key][0] == 'float'):
                    self.output += f"@{key} = dso_local global float {dict1[key][2]}, allign 4\n"
                elif(dict1[key][0] == 'char'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local consant i8 {ord(value)}, allign 1\n"
                    else:
                        try:
                            self.output += f"@{key} = dso_local global i8 {ord(value)}, allign 1\n"
                        except TypeError:
                            pass
        self.print_ll(self.argv)

    def traverse_node(self, node):
        parent = None
        if node.node.getRuleName() == "referenceID":
            parent = value = node.children[1].children[0].node.getRuleName()
        return parent
    
    #look in symbol table if AST nodes needs to be replaced by value this function will do it ... hopefully
    def look_for_value(self, ast):
        self.get_all_comments(ast)
        for child in ast.children:
            self.look_for_value(child)
            if(ast.node.getRuleName() == 'expr'):
                if(ast.children[0].node.getRuleName() == 'variableDefinition'):
                    varName = get_rightmost_node(ast.children[0].children[0])
                    varName = varName.node.getRuleName()
                    
                    #third child
                    temp_node = ast.children[0].children[2]
                    if(temp_node.node.getRuleName() == "nameIdentifier"):
                            value = get_leftmost_node(temp_node)
                    elif(temp_node.node.getRuleName() == "referenceID"):
                        value = get_rightmost_node(temp_node)
                    else:
                        value = get_leftmost_node(temp_node)
                    value = value.node.getRuleName()

                    const1 = getConst(ast.children[0].children[0])
                    typeVar = getType(ast.children[0].children[0])
                    #update symbol table
                    for dict1 in self.table.symbol_table.symbol_tables:
                        #wil aanpassing doen
                        if varName in dict1:
                            if(isinstance(dict1[varName], list)):
                                if dict1[varName][1][0] == "pointer" or dict1[varName][1][0] == "const pointer":
                                    continue
                            if(isinstance(dict1[varName],AST)):
                                if(isinstance(dict1[varName], list)):
                                    dict1[varName][2] = value
                                else:
                                    dict1[varName] = [typeVar, [const1, None], value]
                            elif(isinstance(dict1[varName], list)):
                                if(isinstance(dict1[varName][2], AST)):
                                    if(isinstance(dict1[varName], list)):
                                        dict1[varName][2] = value
                                    else:
                                        dict1[varName] = [typeVar, [const1, None], value]



    def print_ll(self, argv):
        argv += ".ll"
        file = open(argv, "w")
        file.write(self.output)

    def get_all_comments(self, node):
        if node.node.getRuleName() == "comment":
            self.traverse_child(node)
        for child in node.children:
            self.get_all_comments(child)

    def traverse_child(self, node):
        for child in node.children:
            if child.node.getRuleName() not in self.comments:
                self.comments.append(child.node.getRuleName())
            self.traverse_child(child)


def get_leftmost_node(node):
    if not node:  # base case for empty tree or leaf node
        return None
    if not node.children:  # base case for node without children
        return node
    return get_leftmost_node(node.children[0])  # recursive call to leftmost child

def get_rightmost_node(node):
    if not node:  # base case for empty tree or leaf node
        return None
    if not node.children:  # base case for node without children
        return node
    return get_rightmost_node(node.children[-1])  # recursive call to rightmost child

def getType(node):
    if node.node.getRuleName() == 'reservedWord':
        return node.children[0].node.getRuleName()
    elif node.children:
        for child in node.children:
            result = getType(child)
            if result is not None:
                return result
    return None

def getConst(node):
    if node.node.getRuleName() == 'constWord':
        return node.children[0].node.getRuleName()
    elif node.children:
        for child in node.children:
            result = getConst(child)
            if result is not None:
                return result
    return None
