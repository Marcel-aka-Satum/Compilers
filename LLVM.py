from AST import *
from SemanticAnalysisVisitor import *
#class that will generate output file with converted c code into LLVM tested with tool godbolt.org
#• Language: C
#• Compiler: x86-64 clang 16.0.0
#• Compiler options: -S -emit-llvm
class LLVM:
    def __init__(self, argv, symbolTable: SemanticAnalysisVisitor) -> None:
        self.output = ""
        self.argv = argv
        self.values2 = []
        self.table = symbolTable

    def generate_LLVM(self):
        #loop through symbolTable
        for dict1 in self.table.symbol_table.symbol_tables:
            #loop through dicts of table (can have multiple scopes)
            for key in dict1:
                #check if there is a value
                value = dict1[key][2]
                if value is None:
                    value = 0
                #fix pointers
                if(isinstance(dict1[key][2], AST)):
                    if((dict1[key][1][0] == 'pointer' or dict1[key][1][0] == 'const pointer') and dict1[key][0] == 'int'):
                        parent = self.traverse_node(dict1[key][2])
                        self.output += f"@{key} = dso_local global ptr @{parent}, allign 8 \n"
                        continue
                    elif((dict1[key][1][0] == 'pointer' or dict1[key][1][0] == 'const pointer') and dict1[key][0] == 'float'):
                        parent = self.traverse_node(dict1[key][2])
                        self.output += f"@{key} = dso_local global ptr @{parent}, allign 8 \n"
                        continue
                    elif((dict1[key][1][0] == 'pointer' or dict1[key][1][0] == 'const pointer') and dict1[key][0] == 'char'):
                        parent = self.traverse_node(dict1[key][2])
                        self.output += f"@{key} = dso_local global ptr @{parent}, allign 8 \n"
                        continue
                    
                if(dict1[key][0] == 'int'):
                    value = dict1[key][2]
                    if value is None:
                        value = 0
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant i32 {value}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global i32 {value}, allign 4\n"
                elif(dict1[key][0] == 'float'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant float {value}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global float {value}, allign 4\n"
                elif(dict1[key][0] == 'char'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local consant i8 {ord(value)}, allign 1\n"
                    else:
                        self.output += f"@{key} = dso_local global i8 {ord(value)}, allign 1\n"
        self.print_ll(self.argv)

    def traverse_node(self, node):
        if node.node.getRuleName() == "referenceID":
            parent = value = node.children[1].children[0].node.getRuleName()
        return parent
    
    #look in symbol table if AST nodes needs to be replaced by value this function will do it ... hopefully
    def look_for_value(self, ast):
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
                # elif (ast.children[0].node.getRuleName() == 'assignmentStatement'):
                #     #ptr assigment
                #     rightMostNode = get_rightmost_node(ast.children[0])
                #     leftMostNode = get_leftmost_node(ast.children[0])
                #     for dict1 in self.table.symbol_table.symbol_tables:
                #         if rightMostNode.node.getRuleName() in dict1:
                #             dict1[leftMostNode.node.getRuleName()] = dict1[rightMostNode.node.getRuleName()]



    def print_ll(self, argv):
        argv += ".ll"
        file = open(argv, "w")
        file.write(self.output)

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