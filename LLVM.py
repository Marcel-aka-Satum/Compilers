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
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local constant float {dict1[key][2]}, allign 4\n"
                    else:
                        self.output += f"@{key} = dso_local global float {dict1[key][2]}, allign 4\n"
                elif(dict1[key][0] == 'char'):
                    if(dict1[key][1] == 'const'):
                        self.output += f"@{key} = dso_local consant i8 {ord(dict1[key][2])}, allign 1\n"
                    else:
                        self.output += f"@{key} = dso_local global i8 {ord(dict1[key][2])}, allign 1\n"
        print(self.output)
                
