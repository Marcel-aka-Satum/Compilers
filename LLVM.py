from AST import *

#class that will generate output file with converted c code into LLVM tested with tool godbolt.org
#• Language: C
#• Compiler: x86-64 clang 16.0.0
#• Compiler options: -S -emit-llvm
class LLVM:
    def __init__(self, argv) -> None:
        self.output = ""
        self.argv = argv

    def generate_LLVM(self, table):
        #loop through symbolTable
        for dict1 in table:
            #loop through dicts of table (can have multiple scopes)
            for key in dict1:
                #if the value is a node we need to traverse it to get its value
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
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant i32 {dict1[key][2]}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global i32 {dict1[key][2]}, allign 4\n"
                elif(dict1[key][0] == 'float'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant float {dict1[key][2]}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global float {dict1[key][2]}, allign 4\n"
                elif(dict1[key][0] == 'char'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local consant i8 {ord(dict1[key][2])}, allign 1\n"
                    else:
                        self.output += f"@{key} = dso_local global i8 {ord(dict1[key][2])}, allign 1\n"
        self.print_ll(self.argv)

    def traverse_node(self, node):
        if node.node.getRuleName() == "referenceID":
            parent = value = node.children[1].children[0].node.getRuleName()
        return parent
    
    def print_ll(self, argv):
        argv += ".ll"
        file = open(argv, "w")
        file.write(self.output)
