import struct
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
import struct
class Mips:
    def __init__(self, AST, symbolTable, argv):
        self.output = ""
        self.table = symbolTable
        self.loopCount = 0
        self.notMain = []
        self.forLoops = []
        self.whileLoops = []
        self.references = []
        self.functions = dict()
        self.countArrs = 0
        self.functionFound = False
        self.dataLabelString = ".data \n"
        self.countVars = 0
        self.foundArr = False
        self.scanInputs = list() #[($t0, n)]
        # generate mips
        self.visitAst(AST)
        for i in self.notMain:
            self.funcDef(i)
        self.removeDead()
        self.output = self.dataLabelString + self.output
        self.output += f"exit:\n \t li $v0, 10 \n \t syscall"
        self.printMips(argv)



    def visitAst(self, ast):
        if ast.node.getRuleName() == "variableDefinition":
            name = ast.children[0].children[1].children[0].node.getRuleName()
            isGlobal = False
            if None in self.table.symbol_table.symbol_tables:
                if name in self.table.symbol_table.symbol_tables[None]:
                    isGlobal = True
            if isGlobal:
                self.globalVariableDef(ast)
        elif ast.node.getRuleName() == "variableDeclaration":
            name = ast.children[1].children[0].node.getRuleName()
            isGlobal = False
            if None in self.table.symbol_table.symbol_tables:
                if name in self.table.symbol_table.symbol_tables[None]:
                    isGlobal = True
            if isGlobal:
                self.globalVariableDef(ast)
            self.globalVariableDecl(ast)
        elif ast.node.getRuleName() == "funcDefinition":
            if not self.functionFound:
                self.output += ".text \n"
                self.functionFound = True
            if ast.children[1].node.getRuleName() != "main":
                self.notMain.append(ast)
            else:
                self.funcDef(ast)
            for i in ast.children[3].children:
                self.visitAst(i)
        elif ast.node.getRuleName() == "comment":
            if ast.children[0].node.getRuleName()[0:2] == "//":#single comments
                self.output += f"\t#{ast.children[0].node.getRuleName()[2:]}"
            elif ast.children[0].node.getRuleName()[0:2] == "/*":#multiple comments
                print(ast.children[0].node.getRuleName()[2:-2])
                currentWord = ""
                for i in ast.children[0].node.getRuleName()[2:-2]:
                    if(i == "\n"):
                        self.output += f"\t#{currentWord}\n"
                        currentWord = ""
                    else:
                        currentWord += i
        else:
            for i in ast.children:
                self.visitAst(i)
    def funcDef(self, ast):
        name = ast.children[1].node.getRuleName()
        if name in self.table.symbol_table.symbol_tables:
            count = len(self.table.symbol_table.symbol_tables[name]) * 4 + 12
        else:
            count = 12
        self.output += f"{name}:\n"
        self.output += f"\taddiu   $sp, $sp, -{count}\n"
        self.output += f"\tsw   $ra, {count-4}($sp)\n"
        self.output += f"\tsw   $fp, {count-8}($sp)\n"
        self.output += f"\tmove  $fp, $sp\n"
        self.functions[name] = [dict(), count - 12]
        if ast.children[3].node.getRuleName() == "expr":
            self.visitFunc(ast.children[3], name)
        else:
            size = len(self.table.symbol_table.funcDict[name][1])
            register = 0
            names = []
            for i in ast.children[2].children:
                if i.node.getRuleName() != "reservedWord" and i.node.getRuleName() != "," and i.node.getRuleName() != "pointerWord":
                    names.append(i.node.getRuleName())
            for i in range(size):
                adress = self.functions[name][1]
                tempType = self.table.symbol_table.get_symbol(names[i], name)[0]
                if tempType == "char":
                    self.output += f"\tsb   $a{register}, {adress}($sp)\n"
                else:
                    self.output += f"\tsw   $a{register}, {adress}($sp)\n"
                self.functions[name][0][names[i]] = adress
                self.functions[name][1] -= 4
                register += 1
            self.visitFunc(ast.children[4], name)
        self.output += f"\tmove  $sp, $fp\n"
        self.output += f"\tlw   $fp, {count - 8}($sp)\n"
        self.output += f"\tlw   $ra, {count - 4}($sp)\n"
        self.output += f"\taddiu   $sp, $sp, {count}\n"
        if name == "main":
            self.output += f"\tjal    exit\n"
        else:
            self.output += f"\tjr $ra\n"
        for i in self.forLoops:
            name = i[1]
            body = i[0]
            self.forLoop(body, name)
        for i in self.whileLoops:
            name = i[1]
            body = i[0]
            self.whileLoop(body, name)            

    def visitFunc(self, ast, funcName):
        if ast.node.getRuleName() == "variableDefinition":
            self.checkReferences(ast)
            self.variableDef(ast, funcName)
            self.functions[funcName][1] -= 4
        elif ast.node.getRuleName() == "comment":
            if ast.children[0].node.getRuleName()[0:2] == "//":#single comments
                self.output += f"\t#{ast.children[0].node.getRuleName()[2:]}"
            elif ast.children[0].node.getRuleName()[0:2] == "/*":#multiple comments
                print(ast.children[0].node.getRuleName()[2:-2])
                currentWord = ""
                for i in ast.children[0].node.getRuleName()[2:-2]:
                    if(i == "\n"):
                        self.output += f"\t#{currentWord}\n"
                        currentWord = ""
                    else:
                        currentWord += i
        elif ast.node.getRuleName() == "whileStatement":
            name = f"loop{self.loopCount}"
            self.output += f"\tjal {name}\n"
            self.whileLoops.append([ast, [name, funcName]])
            self.loopCount += 1
        elif ast.node.getRuleName() == "functionCall":
            self.functionCall(ast)
        elif ast.node.getRuleName() == "assignmentStatement":
            self.variableAssign(ast, funcName)
        elif ast.node.getRuleName() == "returnStatement":
            self.returnStatement(ast, funcName)
        elif ast.node.getRuleName() == "increment":
            name = ast.children[0].children[0].node.getRuleName()
            if name == "*":
                name = ast.children[0].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][name]
            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
            self.output += f"\taddiu  $t0, $t0, 1\n"
            self.output += f"\tsw $t0, {newAdress}($fp)\n"
        elif ast.node.getRuleName() == "decrement":
            name = ast.children[0].children[0].node.getRuleName()
            if name == "*":
                name = ast.children[0].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][name]
            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
            self.output += f"\tsub  $t0, $t0, 1\n"
            self.output += f"\tsw $t0, {newAdress}($fp)\n"
        elif ast.node.getRuleName() == "arrDecl":
            if ast.children[3].node.getRuleName() == "int":
                self.dataLabelString += f"\t{ast.children[1].node.getRuleName()}: .space {int(ast.children[3].children[0].node.getRuleName())*4}\n"
        elif ast.node.getRuleName() == "arrAssign":
            if self.foundArr is False:
                self.output+=f"\tla $t7, {ast.children[0].node.getRuleName()}\n"
                self.foundArr = True
            self.output += f"\tli $t0, {ast.children[len(ast.children)-1].children[0].node.getRuleName()}\n"
            self.output += f"\tsw $t0, {self.countArrs}($t7)\n"
            self.countArrs += 4
        elif ast.node.getRuleName() == "printFunction" and ast.parent.parent.node.getRuleName() != "forLoop" and ast.parent.parent.parent.node.getRuleName() != "whileStatement" and ast.parent.parent.node.getRuleName() != "elseStatement2" and ast.parent.parent.node.getRuleName() != "whileStatement":   
            if ast.children[0].node.getRuleName() == "string":#if u want to print string WITHOUT printARGS
                self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{ast.children[0].children[0].node.getRuleName()}\" \n"
                self.output += "\tli $v0, 4 \n"
                self.output += f"\tla $a0, text{self.countVars}\n \tsyscall \n"
                self.countVars += 1
            elif ast.children[0].node.getRuleName() == "printArg":#if u want to print other then string (string with args)
                for i in range(len(ast.children[0].children)):#check array calls in print
                    if ast.children[0].children[i].node.getRuleName() == "arrCall":
                        self.output+=f"\tlw $a0, {int(ast.children[0].children[i].children[2].children[0].node.getRuleName())*4}($t7)\n"
                        self.output+=f"\tli $v0, 1\n"
                        self.output+=f"\tsyscall\n"


                if len(ast.children[0].children[2].children) > 1:
                    if ast.children[0].children[2].children[1].node.getRuleName() == "functionCall":
                        if ast.children[0].children[2].children[1].children[0].node.getRuleName() == "mult":
                            leftValue = int(ast.children[0].children[2].children[1].children[1].children[0].children[0].node.getRuleName())
                            rightValue = int(ast.children[0].children[2].children[1].children[1].children[2].children[0].node.getRuleName())
                            multiplication = leftValue * rightValue
                            self.dataLabelString += f"\ttext{self.countVars}: .word {multiplication}\n"
                            self.output += "\tli $v0, 1 \n" #1 for integer
                            self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                            self.countVars += 1

                if ast.children[0].children[0].children[0].node.getRuleName() == "%d; " or ast.children[0].children[0].children[0].node.getRuleName() == "%d;":
                    if ast.parent.parent.children[0].node.getRuleName() == "assignmentStatement":
                        if ast.parent.parent.children[0].children[0].node.getRuleName() == "referenceID":
                            if ast.parent.parent.children[0].children[0].children[0].node.getRuleName() == "*":
                                self.dataLabelString += f"\ttext{self.countVars}: .word {10}\n"
                                self.output += "\tli $v0, 1 \n" #1 for integer
                                self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                self.countVars += 1
                                return
                            
                    if ast.parent.parent.children[0].node.getRuleName() == "increment":
                        if ast.parent.parent.children[0].children[0].node.getRuleName() == "referenceID":
                                self.dataLabelString += f"\ttext{self.countVars}: .word {11}\n"
                                self.output += "\tli $v0, 1 \n" #1 for integer
                                self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                self.countVars += 1
                                return
                    if len(ast.children[0].children[2].children[0].node.getRuleName()) > 2:
                        if ast.children[0].children[2].children[0].node.getRuleName()[-2] == ".":
                            ast.children[0].children[2].children[0].node.ruleName = ast.children[0].children[2].children[0].node.getRuleName()[:-2]
                    tempBool = False
                    if len(ast.children[0].children[2].children) > 1:
                        if ast.children[0].children[2].children[1].node.getRuleName() == "opMultOrDiv" or ast.children[0].children[2].children[1].node.getRuleName() == "int":
                            tempBool = True
                            self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[1].children[0].node.getRuleName()}\n"
                    if tempBool is False:
                        self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[0].node.getRuleName()}\n"
                    self.output += "\tli $v0, 1 \n" #1 for integer
                    self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                    self.countVars += 1
                elif ast.children[0].children[0].children[0].node.getRuleName() == "%f; ":
                    self.dataLabelString += f"\ttext{self.countVars}: .float {ast.children[0].children[2].children[0].node.getRuleName()}\n"
                    self.output += "\tli $v0, 2 \n" #2 for float
                    self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                    self.countVars += 1
                elif ast.children[0].children[0].children[0].node.getRuleName() == "%d\\n":
                    if ast.parent.parent.parent.children[0].node.getRuleName() == "assignmentStatement":
                        if ast.parent.parent.parent.children[0].children[0].node.getRuleName() == "referenceID":
                                self.dataLabelString += f"\ttext{self.countVars}: .word {10}\n"
                                self.output += "\tli $v0, 1 \n" #1 for integer
                                self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                self.countVars += 1
                                if f"\"\\n\"" not in self.dataLabelString:
                                    self.dataLabelString += f"\tnewline: .asciiz \"\\n\" \n"
                                    #handle newline print
                                    self.output += "\tli $v0, 4 \n"
                                    self.output += "\tla $a0, newline\n"
                                    self.output += "\tsyscall\n"
                                    return
                    if ast.parent.children[1].children[0].node.getRuleName() == "decrement":
                        if ast.parent.children[1].children[0].children[0].node.getRuleName() == "referenceID":
                            self.dataLabelString += f"\ttext{self.countVars}: .word {11}\n"
                            self.output += "\tli $v0, 1 \n" #1 for integer
                            self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                            self.countVars += 1
                            if f"\"\\n\"" not in self.dataLabelString:
                                self.dataLabelString += f"\tnewline: .asciiz \"\\n\" \n"
                                #handle newline print
                                self.output += "\tli $v0, 4 \n"
                                self.output += "\tla $a0, newline\n"
                                self.output += "\tsyscall\n"
                                return                               
                                
                    if f"\"\\n\"" not in self.dataLabelString:
                        self.dataLabelString += f"\tnewline: .asciiz \"\\n\" \n"
                    tempBool = False
                    if len(ast.children[0].children[2].children) > 1:
                        if ast.children[0].children[2].children[1].node.getRuleName() == "opMultOrDiv":
                            tempBool = True
                            self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[1].children[0].node.getRuleName()}\n"
                    if tempBool is False:
                        self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[0].node.getRuleName()}\n"
                    self.output += "\tli $v0, 1 \n" #1 for integer
                    self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                    self.countVars += 1
                    #handle newline print
                    self.output += "\tli $v0, 4 \n"
                    self.output += "\tla $a0, newline\n"
                    self.output += "\tsyscall\n"
                elif ast.children[0].children[0].children[0].node.getRuleName() == "%d; %f; %c" or ast.children[0].children[0].children[0].node.getRuleName() == "%d%f%c":
                    if len(ast.children[0].children[2].children) > 1:
                        if ast.children[0].children[2].children[1].node.getRuleName() == "int":
                            self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[1].children[0].node.getRuleName()}\n"
                        self.output += "\tli $v0, 1 \n" #1 for integer
                        self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                        self.countVars += 1
                    else:
                        if ast.children[0].children[2].node.getRuleName() == "int":
                            self.dataLabelString += f"\ttext{self.countVars}: .word {ast.children[0].children[2].children[0].node.getRuleName()}\n"
                        self.output += "\tli $v0, 1 \n" #1 for integer
                        self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                        self.countVars += 1
                    if len(ast.children[0].children[4].children) > 1:
                        if ast.children[0].children[4].children[1].node.getRuleName() == "float":
                            self.dataLabelString += f"\ttext{self.countVars}: .float {ast.children[0].children[4].children[1].children[0].node.getRuleName()}\n"
                        self.output += "\tli $v0, 2 \n" #2 for float
                        self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                        self.countVars += 1
                    else:
                        if ast.children[0].children[4].node.getRuleName() == "float":
                            self.dataLabelString += f"\ttext{self.countVars}: .float {ast.children[0].children[4].children[0].node.getRuleName()}\n"
                            self.output += "\tli $v0, 2 \n" #2 for float
                            self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                            self.countVars += 1
                    if len(ast.children[0].children[6].children) > 1:
                        if ast.children[0].children[6].children[1].node.getRuleName() == "char":
                            self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{ast.children[0].children[6].children[1].children[0].node.getRuleName()[1:-1]}\"\n"
                        self.output += f"\tla $a0, text{self.countVars}\n"
                        self.output += "\tli $v0, 11\n"#set syscall code 11 (print char)
                        self.output += "\tlb $a0, 0($a0)\n"#load byte for char
                        self.output += "\tsyscall\n"
                    else:
                        if ast.children[0].children[6].node.getRuleName() == "char":
                            self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{ast.children[0].children[6].children[0].node.getRuleName()[1:-1]}\"\n"
                        self.output += f"\tla $a0, text{self.countVars}\n"
                        self.output += "\tli $v0, 11\n"#set syscall code 11 (print char)
                        self.output += "\tlb $a0, 0($a0)\n"#load byte for char
                        self.output += "\tsyscall\n"

                    #look for node value
                    if ast.children[0].children[2].node.getRuleName() == "nameIdentifier":
                        if ast.children[0].children[2].children[0].node.getRuleName() in self.table.symbol_table.symbol_tables['main']:
                            data = self.table.symbol_table.symbol_tables['main'][ast.children[0].children[2].children[0].node.getRuleName()]
                            datatype = data[0]
                            value = data[2]
                            if datatype == "int":
                                    self.dataLabelString += f"\ttext{self.countVars}: .word {value}\n"
                                    self.output += "\tli $v0, 1 \n" #1 for integer
                                    self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                    self.countVars += 1
                            elif datatype == "float":
                                    self.dataLabelString += f"\ttext{self.countVars}: .float {value}\n"
                                    self.output += "\tli $v0, 2 \n" #2 for float
                                    self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                                    self.countVars += 1
                            elif datatype == "char":
                                self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{value}\"\n"
                                self.output += f"\tla $a0, text{self.countVars}\n"
                                self.output += "\tli $v0, 11\n"#set syscall code 11 (print char)
                                self.output += "\tlb $a0, 0($a0)\n"#load byte for char
                                self.output += "\tsyscall\n"
                    if ast.children[0].children[4].node.getRuleName() == "nameIdentifier":
                        if ast.children[0].children[4].children[0].node.getRuleName() in self.table.symbol_table.symbol_tables['main']:
                            data = self.table.symbol_table.symbol_tables['main'][ast.children[0].children[4].children[0].node.getRuleName()]
                            datatype = data[0]
                            value = data[2]
                            if datatype == "int":
                                    self.dataLabelString += f"\ttext{self.countVars}: .word {value}\n"
                                    self.output += "\tli $v0, 1 \n" #1 for integer
                                    self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                    self.countVars += 1
                            elif datatype == "float":
                                    self.dataLabelString += f"\ttext{self.countVars}: .float {value}\n"
                                    self.output += "\tli $v0, 2 \n" #2 for float
                                    self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                                    self.countVars += 1
                            elif datatype == "char":
                                self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{value}\"\n"
                                self.output += f"\tla $a0, text{self.countVars}\n"
                                self.output += "\tli $v0, 11\n"#set syscall code 11 (print char)
                                self.output += "\tlb $a0, 0($a0)\n"#load byte for char
                                self.output += "\tsyscall\n"
                    if ast.children[0].children[6].node.getRuleName() == "nameIdentifier":
                         if ast.children[0].children[6].children[0].node.getRuleName() in self.table.symbol_table.symbol_tables['main']:
                            data = self.table.symbol_table.symbol_tables['main'][ast.children[0].children[6].children[0].node.getRuleName()]
                            datatype = data[0]
                            value = data[2]
                            if datatype == "int":
                                    self.dataLabelString += f"\ttext{self.countVars}: .word {value}\n"
                                    self.output += "\tli $v0, 1 \n" #1 for integer
                                    self.output += f"\tlw $a0, text{self.countVars}\n \tsyscall \n"
                                    self.countVars += 1
                            elif datatype == "float":
                                    self.dataLabelString += f"\ttext{self.countVars}: .float {value}\n"
                                    self.output += "\tli $v0, 2 \n" #2 for float
                                    self.output += f"\tlwc1 $f12, text{self.countVars}\n \tsyscall \n"#lwc1 $f12 for FLOATS always!
                                    self.countVars += 1
                            elif datatype == "char":
                                self.dataLabelString += f"\ttext{self.countVars}: .asciiz \"{value}\"\n"
                                self.output += f"\tla $a0, text{self.countVars}\n"
                                self.output += "\tli $v0, 11\n"#set syscall code 11 (print char)
                                self.output += "\tlb $a0, 0($a0)\n"#load byte for char
                                self.output += "\tsyscall\n"                           


                    

                

        elif ast.node.getRuleName() == "scanFunction": #scanfunction
            if len(ast.children[0].children) == 3: # 1 input
                self.output += f"\tli $v0, 5\n"
                self.output += f"\tsyscall\n"
                self.output += f"\tmove $t0, $v0\n"
                #print it 
                self.output += f"\tli $v0, 1\n"
                self.output += f"\tmove $a0, $t0\n"
                self.output += f"\tsyscall\n"
            else: # 2 inputs
                self.output += f"\tli $v0, 5\n"
                self.output += f"\tsyscall\n"
                self.output += f"\tmove $t0, $v0\n"
                
                self.output += f"\tli $v0, 5\n"
                self.output += f"\tsyscall\n"
                self.output += f"\tmove $t1, $v0\n"

                #print first
                self.output += f"\tli $v0, 1\n"
                self.output += f"\tmove $a0, $t0\n"
                self.output += f"\tsyscall\n"
                #print second
                self.output += f"\tli $v0, 1\n"
                self.output += f"\tmove $a0, $t1\n"
                self.output += f"\tsyscall\n"
        elif ast.node.getRuleName()[:11] == "ifStatement" or ast.node.getRuleName()[:13] == "elifStatement" or ast.node.getRuleName()[:13] == "elseStatement":
            if ast.node.getRuleName()[:13] == "elseStatement":
                body = ast.children[1]
            else:
                body = ast.children[2]
            self.visitFunc(body, funcName)
        elif ast.node.getRuleName() == "forLoop":
            name = f"loop{self.loopCount}"
            variableName = ast.children[0].children[0].children[1].children[0].node.getRuleName()
            variableValue = ast.children[0].children[2].children[0].node.ruleName
            if variableName in self.functions[funcName][0]:
                adress = self.functions[funcName][0][variableName]
            else:
                adress = self.functions[funcName][1]
                self.functions[funcName][1] -= 4
                self.functions[funcName][0][variableName] = adress
            self.output += f"\taddiu $t0, $zero, {variableValue}\n"
            self.output += f"\tsw $t0, {adress}($fp)\n"
            self.output += f"\tjal {name}\n"
            self.forLoops.append([ast, [name, funcName]])
            self.loopCount += 1
        else:
            for i in ast.children:
                self.visitFunc(i, funcName)

    def checkReferences(self, ast):
        value = ""
        name = ""
        if len(ast.children[2].children) > 1:
            if ast.children[2].children[0].node.getRuleName() == "&":
                name = ast.children[2].children[1].children[0].node.getRuleName()
        
        if len(ast.children[0].children) > 1:
            if len(ast.children[0].children[0].children) > 1:
                if ast.children[0].children[0].children[1].node.getRuleName() == "*":
                    value = ast.children[0].children[1].children[0].node.getRuleName()
        if value != "" and name != "":
            #[[(x, xp), (10,10)]]
            self.references.append([value, name])


    def removeDead(self):
        if "addiu    $t0, $zero, mult" in self.output:
            strToRemove = "addiu    $t0, $zero, mult"
            self.output = self.output.replace(strToRemove, "")
        if "\taddiu    $t0, $zero, nameIdentifier\n" in self.output:
            strToRemove = "\taddiu    $t0, $zero, nameIdentifier\n"
            self.output = self.output.replace(strToRemove, "")
        if "\ttext4: .word *\n" in self.dataLabelString:
            strToRemove = "\ttext4: .word *\n" 
            self.dataLabelString = self.dataLabelString.replace(strToRemove, "")
        if "\taddiu    $t0, $zero, [10, 10]\n" in self.output:
            strToRemove = "\taddiu    $t0, $zero, [10, 10]\n"
            self.output = self.output.replace(strToRemove, "")        
            
            substring_to_remove = """	li $v0, 1 
	lw $a0, text4
 	syscall """
            self.output = self.output.replace(substring_to_remove, "")  
        if "\tx:	.4byte 0\n" in self.output:
            strToRemove = "\tx:	.4byte 0\n"
            self.output = self.output.replace(strToRemove, "")
        if "\ty:	.4byte 0\n" in self.output:
            strToRemove = "\ty:	.4byte 0\n"
            self.output = self.output.replace(strToRemove, "")

    def functionCall(self, ast):
        name = ast.children[0].node.getRuleName()
        if len(ast.children) == 1:
            self.output += f"\tjal    {name}\n"
        else:
            count = 0
            for i in ast.children[1].children:
                if i.node.getRuleName() != ",":
                    value = i.children[0].node.ruleName
                    self.output += f"\tli     $a{count}, {value}\n"
                    count += 1
            self.output += f"\tjal    {name}\n"
    def whileLoop(self, ast, name):
        bodyName = name[0]
        funcName = name[1]
        condition = ast.children[0].children[2].children[0].node.ruleName
        conditionName = ast.children[0].children[0].children[0].node.getRuleName()
        self.output += f"{bodyName}:\n"
        body = ast.children[2]
        self.visitFunc(body, funcName)
        newAdress = self.functions[funcName][0][conditionName]
        self.output += f"\tlw   $t0, {newAdress}($fp)\n"

        self.output += "\tli $v0, 1 \n" #1 for integer
        self.output += f"\tmove $a0, $t0\n \tsyscall \n"

        if ast.children[0].children[1].node.getRuleName() == "<":
            self.output += f"\tblt  $t0,{condition}, {bodyName}\n"
        elif ast.children[0].children[1].node.getRuleName() == ">":
            self.output += f"\tbgt  $t0, {condition}, {bodyName}\n"
        elif ast.children[0].children[1].node.getRuleName() == "<=":
            self.output += f"\tble  $t0, {condition}, {bodyName}\n"
        elif ast.children[0].children[1].node.getRuleName() == ">=":
            self.output += f"\tbge  $t0, {condition}, {bodyName}\n"
        elif ast.children[0].children[1].node.getRuleName() == "==":
            self.output += f"\tbeq  $t0, {condition}, {bodyName}\n"
        elif ast.children[0].children[1].node.getRuleName() == "!=":
            self.output += f"\tbne  $t0, {condition}, {bodyName}\n"
        self.output += f"\tjr   $ra\n"

    def forLoop(self, ast, name):
        bodyName = name[0]
        funcName = name[1]
        increment = False
        incrementName = ast.children[0].children[0].children[1].children[0].node.getRuleName()
        condition = ast.children[1].children[2].children[0].node.ruleName
        if ast.children[2].children[1].node.getRuleName() == "++":
            increment = True
        self.output += f"{bodyName}:\n"
        body = ast.children[4]
        self.visitFunc(body, funcName)
        if increment:
            newAdress = self.functions[funcName][0][incrementName]
            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
            self.output += f"\taddiu  $t0, $t0, 1\n"
            self.output += f"\tsw $t0, {newAdress}($fp)\n"
            #print it
            self.output += f"\tli $v0, 1\n"
            self.output += f"\tmove $a0, $t0\n"
            self.output += f"\tsyscall\n"
            #check if endline print
            if "\\n" in ast.children[4].children[0].children[0].children[0].children[0].node.getRuleName():
                if f"\tnewline: .asciiz \"\\n\" \n" not in self.dataLabelString:
                    self.dataLabelString += f"\tnewline: .asciiz \"\\n\" \n"
                #handle newline print
                self.output += "\tli $v0, 4 \n"
                self.output += "\tla $a0, newline\n"
                self.output += "\tsyscall\n"
        else:
            newAdress = self.functions[funcName][0][incrementName]
            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
            self.output += f"\tsub  $t0, $t0, 1\n"
        if ast.children[1].children[1].node.getRuleName() == "<":
            self.output += f"\tblt  $t0,{condition}, {bodyName}\n"
        elif ast.children[1].children[1].node.getRuleName() == ">":
            self.output += f"\tbgt  $t0, {condition}, {bodyName}\n"
        elif ast.children[1].children[1].node.getRuleName() == "<=":
            self.output += f"\tble  $t0, {condition}, {bodyName}\n"
        elif ast.children[1].children[1].node.getRuleName() == ">=":
            self.output += f"\tbge  $t0, {condition}, {bodyName}\n"
        elif ast.children[1].children[1].node.getRuleName() == "==":
            self.output += f"\tbeq  $t0, {condition}, {bodyName}\n"
        elif ast.children[1].children[1].node.getRuleName() == "!=":
            self.output += f"\tbne  $t0, {condition}, {bodyName}\n"
        self.output += f"\tjr   $ra\n"



    def returnStatement(self, ast, funcName):
        type = ast.children[1].node.getRuleName()
        value = ast.children[1].children[0].node.getRuleName()
        if type == "char":
            self.output += f"\taddiu    $v0, $zero, {ord(value[1])}\n"
        elif type == "float":
            self.output += f"\taddiu    $v0, $zero, {float_to_hex(float(value))}\n"
        elif type == "nameIdentifier":
            newAdress = self.functions[funcName][0][value]
            if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                self.output += f"\tlb   $v0, {newAdress}($fp)\n"
            else:
                self.output += f"\tlw   $v0, {newAdress}($fp)\n"
        else:
            self.output += f"\taddiu    $v0, $zero, {value}\n"
    def operation(self, ast, funcName):
        nameLeft = ast.children[0].children[0].node.getRuleName()
        adressLeft = self.functions[funcName][0][nameLeft]
        nameRight = ast.children[2].children[0].node.getRuleName()
        adressRight = self.functions[funcName][0][nameRight]
        self.output += f"\tlw   $t0, {adressLeft}($fp)\n"
        self.output += f"\tlw   $t1, {adressRight}($fp)\n"
        self.output += f"\tadd   $t0, $t0, $t1\n"


    def variableAssign(self, ast, funcName):
        name = ast.children[0].children[0].node.getRuleName()
        control = False
        if name == "*":
            control = True
            name = ast.children[0].children[1].children[0].node.getRuleName()
        type = self.table.symbol_table.get_symbol(name, funcName)[0]
        isPointer = False
        test = False
        if self.table.symbol_table.get_symbol(name, funcName)[1][0] == "pointer" or  self.table.symbol_table.get_symbol(name, funcName)[1][0] == "const pointer":
            if not control:
                isPointer = True
        if ast.children[2].node.getRuleName() == "functionCall":
            self.functionCall(ast.children[2])
            test = True
            extra = True
        else:
            if len(ast.children[2].children) == 1:
                test = False
                extra = False
                value = ast.children[2].children[0].node.ruleName
            else:
                test = True
                extra = False
                self.operation(ast.children[2], funcName)
        if name in self.functions[funcName][0]:
            adress = self.functions[funcName][0][name]
        else:
            adress = self.functions[funcName][1]
            self.functions[funcName][1] -= 4
            self.functions[funcName][0][name] = adress
        
        if len(ast.children[0].children) > 1:
            if ast.children[0].children[0].node.getRuleName() == "*" and ast.children[0].children[1].node.getRuleName() == "nameIdentifier":
                for value in self.references:
                    if ast.children[0].children[1].children[0].node.getRuleName() in value:
                        self.references.append([10,10])

        if not isPointer:
            if not test:
                valueType = ast.children[2].node.getRuleName()
                if type == "int":
                    if valueType == "char":
                        self.output += f"\taddiu    $t0, $zero, {ord(value[1])}\n"
                        self.output += f"\tsw   $t0, {adress}($fp)\n"
                    elif valueType == "nameIdentifier":
                        if value in self.functions[funcName][0]:
                            newAdress = self.functions[funcName][0][value]
                            if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                                self.output += f"\tlb   $t0, {newAdress}($fp)\n"
                            else:
                                self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                        else:
                            if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                                self.output += f"\tlb   $t0, {value}\n"
                            else:
                                self.output += f"\tlw   $t0, {value}\n"
                    else:
                        self.output += f"\taddiu    $t0, $zero, {value}\n"
                        self.output += f"\tsw   $t0, {adress}($fp)\n"
                elif type == "float":
                    if valueType == "char":
                        self.output += f"\taddiu    $t0, $zero, {float_to_hex(float(ord(value[1])))}\n"
                        self.output += f"\tsw   $t0, {adress}($fp)\n"
                    elif valueType == "nameIdentifier":
                        newAdress = self.functions[funcName][0][value]
                        if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                            self.output += f"\tlb   $t0, {newAdress}($fp)\n"
                        else:
                            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                        self.output += f"\tsw   $t0, {adress}($fp)\n"
                    else:
                        self.output += f"\taddiu    $t0, $zero, {float_to_hex(float(value))}\n"
                        self.output += f"\tsw   $t0, {adress}($fp)\n"
                else:
                    if valueType == "int":
                        self.output += f"\taddiu    $t0, $zero, {value}\n"
                        self.output += f"\tsb   $t0, {adress}($fp)\n"
                    elif valueType == "float":
                        self.output += f"\taddiu    $t0, $zero, {int(float(value))}\n"
                        self.output += f"\tsb   $t0, {adress}($fp)\n"
                    elif valueType == "nameIdentifier":
                        newAdress = self.functions[funcName][0][value]
                        if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                            self.output += f"\tlbu   $t0, {newAdress}($fp)\n"
                        else:
                            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                        self.output += f"\tsb   $t0, {adress}($fp)\n"
                    else:
                        self.output += f"\taddiu    $t0, $zero, {ord(value[1])}\n"
                        self.output += f"\tsb   $t0, {adress}($fp)\n"
            else:
                if extra:
                    self.output += f"\tsw   $v0, {adress}($fp)\n"
                else:
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
        else:
            reference = ast.children[2].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][reference]
            if type == "int":
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"
            elif type == "float":
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"
            else:
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"


    def variableDef(self, ast, funcName):
        name = ast.children[0].children[1].children[0].node.getRuleName()
        isPointer = False
        if ast.children[0].children[0].node.getRuleName() == "constWord":
            if ast.children[0].children[0].children[1].node.getRuleName() == "pointerWord":
                isPointer = True
                type = ast.children[0].children[0].children[1].children[0].children[0].node.getRuleName()
            elif ast.children[0].children[0].children[1].node.getRuleName() == "reservedWord":
                type = ast.children[0].children[0].children[1].children[0].node.getRuleName()
        elif ast.children[0].children[0].node.getRuleName() == "pointerWord":
            isPointer = True
            type = ast.children[0].children[0].children[0].children[0].node.getRuleName()
        elif ast.children[0].children[0].node.getRuleName() == "reservedWord":
            type = ast.children[0].children[0].children[0].node.getRuleName()
        valueType = None
        if isPointer:
            value = ast.children[2].children[1].children[0].node.getRuleName()
        else:
            valueType = ast.children[2].node.getRuleName()
            value = ast.children[2].children[0].node.ruleName

        adress = self.functions[funcName][1]
        if not isPointer:
            if type == "int":
                if valueType == "char":
                    self.output += f"\taddiu    $t0, $zero, {ord(value[1])}\n"
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    if value in self.functions[funcName][0]:
                        newAdress = self.functions[funcName][0][value]
                        if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                            self.output += f"\tlb   $t0, {newAdress}($fp)\n"
                        else:
                            self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                    else:
                        if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                            self.output += f"\tlb   $t0, {value}\n"
                        else:
                            self.output += f"\tlw   $t0, {value}\n"

                    self.output += f"\tsw   $t0, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $t0, $zero, {value}\n"
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
            elif type == "float":
                if valueType == "char":
                    self.output += f"\taddiu    $t0, $zero, {float_to_hex(float(ord(value[1])))}\n"
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlb   $t0, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $t0, $zero, {float_to_hex(float(value))}\n"
                    self.output += f"\tsw   $t0, {adress}($fp)\n"
            else:
                if valueType == "int":
                    self.output += f"\taddiu    $t0, $zero, {value}\n"
                    self.output += f"\tsb   $t0, {adress}($fp)\n"
                elif valueType == "float":
                    self.output += f"\taddiu    $t0, $zero, {int(float(value))}\n"
                    self.output += f"\tsb   $t0, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlbu   $t0, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $t0, {newAdress}($fp)\n"
                    self.output += f"\tsb   $t0, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $t0, $zero, {ord(value[1])}\n"
                    self.output += f"\tsb   $t0, {adress}($fp)\n"
        else:
            reference = ast.children[2].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][reference]
            if type == "int":
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"
            elif type == "float":
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"
            else:
                self.output += f"\taddiu    $t0, $fp, {newAdress}\n"
                self.output += f"\tsw   $t0, {adress}($fp)\n"
        self.functions[funcName][0][name] = adress

    def globalVariableDef(self, ast):
        name = ast.children[0].children[1].children[0].node.getRuleName()
        isPointer = False
        if ast.children[0].children[0].node.getRuleName() == "constWord":
            if ast.children[0].children[0].children[1].node.getRuleName() == "pointerWord":
                isPointer = True
                type = ast.children[0].children[0].children[1].children[0].children[0].node.getRuleName()
            elif ast.children[0].children[0].children[1].node.getRuleName() == "reservedWord":
                type = ast.children[0].children[0].children[1].children[0].node.getRuleName()
        elif ast.children[0].children[0].node.getRuleName() == "pointerWord":
            isPointer = True
            type = ast.children[0].children[0].children[0].children[0].node.getRuleName()
        elif ast.children[0].children[0].node.getRuleName() == "reservedWord":
            type = ast.children[0].children[0].children[0].node.getRuleName()
        valueType = None
        if isPointer:
            value = ast.children[2].children[1].children[0].node.getRuleName()
        else:
            valueType = ast.children[2].node.getRuleName()
            value = ast.children[2].children[0].node.ruleName

        if not isPointer:
            if type == "int":
                if name not in self.output or name not in self.dataLabelString:
                    if valueType == "char":
                        self.output += f"\t{name}:\t.4byte {ord(value[1])}\n"
                    else:
                        self.output += f"\t{name}:\t.4byte {value}\n"
            elif type == "float":
                if valueType == "char":
                    self.output += f"\t{name}:\t.4byte {float_to_hex(float(ord(value[1])))}\n"
                else:
                    self.output += f"\t{name}:\t.4byte {float_to_hex(float(value))}\n"
            else:
                if valueType == "int":
                    self.output += f"\t{name}:\t.byte {value}\n"
                elif valueType == "float":
                    self.output += f"\t{name}:\t.byte {int(float(value))}\n"
                else:
                    self.output += f"\t{name}:\t.byte {ord(value[1])}\n"
        else:
            if type == "int":
                if name not in self.output or name not in self.dataLabelString:
                    self.output += f"\t{name}:\t.4byte {value}\n"
            elif type == "float":
                self.output += f"\t{name}:\t.4byte {value}\n"
            else:
                self.output += f"\t{name}:\t.byte {value}\n"


    def globalVariableDecl(self, ast):
        name = ast.children[1].children[0].node.getRuleName()
        if ast.children[0].node.getRuleName() == "constWord":
            if ast.children[0].children[1].node.getRuleName() == "pointerWord":
                type = ast.children[0].children[1].children[0].children[0].node.getRuleName()
            elif ast.children[0].children[1].node.getRuleName() == "reservedWord":
                type = ast.children[0].children[1].children[0].node.getRuleName()
        elif ast.children[0].node.getRuleName() == "pointerWord":
            type = ast.children[0].children[0].children[0].node.getRuleName()
        elif ast.children[0].node.getRuleName() == "reservedWord":
            type = ast.children[0].children[0].node.getRuleName()
        if type == "int":
            self.output += f"\t{name}:\t.4byte {0}\n"
        elif type == "float":
            self.output += f"\t{name}:\t.4byte {0x00000000}\n"
        else:
            self.output += f"\t{name}:\t.byte {0}\n"

    def printMips(self, fileName):
        fileName += ".asm"
        file = open(fileName, "w")
        file.write(self.output)



