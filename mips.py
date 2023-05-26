import struct
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
class Mips:
    def __init__(self, AST, symbolTable, argv):
        self.output = ""
        self.table = symbolTable
        self.functions = dict()
        # generate mips
        self.visitAst(AST)
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
            self.funcDef(ast)
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
            register = 4
            names = []
            for i in ast.children[2].children:
                if i.node.getRuleName() != "reservedWord" and i.node.getRuleName() != "," and i.node.getRuleName() != "pointerWord":
                    names.append(i.node.getRuleName())
            for i in range(size):
                adress = self.functions[name][1]
                tempType = self.table.symbol_table.get_symbol(names[i], name)[0]
                if tempType == "char":
                    self.output += f"\tsb   ${register}, {adress}($sp)\n"
                else:
                    self.output += f"\tsw   ${register}, {adress}($sp)\n"
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
    def visitFunc(self, ast, funcName):
        if ast.node.getRuleName() == "variableDefinition":
            self.variableDef(ast, funcName)
            self.functions[funcName][1] -= 4
        elif ast.node.getRuleName() == "assignmentStatement":
            self.variableAssign(ast, funcName)
        elif ast.node.getRuleName() == "returnStatement":
            self.returnStatement(ast, funcName)
        else:
            for i in ast.children:
                self.visitFunc(i, funcName)
    def returnStatement(self, ast, funcName):
        type = ast.children[1].node.getRuleName()
        value = ast.children[1].children[0].node.getRuleName()
        if type == "char":
            self.output += f"\taddiu    $2, $zero, {ord(value[1])}\n"
        elif type == "float":
            self.output += f"\taddiu    $2, $zero, {float.hex(float(value))}\n"
        elif type == "nameIdentifier":
            newAdress = self.functions[funcName][0][value]
            if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                self.output += f"\tlb   $2, {newAdress}($fp)\n"
            else:
                self.output += f"\tlw   $2, {newAdress}($fp)\n"

        else:
            self.output += f"\taddiu    $2, $zero, {value}\n"
    def variableAssign(self, ast, funcName):
        name = ast.children[0].children[0].node.getRuleName()
        type = self.table.symbol_table.get_symbol(name, funcName)[0]
        isPointer = False
        if self.table.symbol_table.get_symbol(name, funcName)[1][0] == "pointer" or  self.table.symbol_table.get_symbol(name, funcName)[1][0] == "const pointer":
            isPointer = True
        value = ast.children[2].children[0].node.ruleName
        if name in self.functions[funcName][0]:
            adress = self.functions[funcName][0][name]
        else:
            adress = self.functions[funcName][1]
            self.functions[funcName][1] -= 4
            self.functions[funcName][0][name] = adress
        if not isPointer:
            valueType = ast.children[2].node.getRuleName()
            if type == "int":
                if valueType == "char":
                    self.output += f"\taddiu    $1, $zero, {ord(value[1])}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlb   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {value}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
            elif type == "float":
                if valueType == "char":
                    self.output += f"\taddiu    $1, $zero, {float.hex(float(ord(value[1])))}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlb   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {float.hex(float(value))}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
            else:
                if valueType == "int":
                    self.output += f"\taddiu    $1, $zero, {value}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                elif valueType == "float":
                    self.output += f"\taddiu    $1, $zero, {int(float(value))}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlbu   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {ord(value[1])}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
        else:
            reference = ast.children[2].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][reference]
            if type == "int":
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"
            elif type == "float":
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"
            else:
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"

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
                    self.output += f"\taddiu    $1, $zero, {ord(value[1])}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlb   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {value}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
            elif type == "float":
                if valueType == "char":
                    self.output += f"\taddiu    $1, $zero, {float.hex(float(ord(value[1])))}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlb   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {float.hex(float(value))}\n"
                    self.output += f"\tsw   $1, {adress}($fp)\n"
            else:
                if valueType == "int":
                    self.output += f"\taddiu    $1, $zero, {value}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                elif valueType == "float":
                    self.output += f"\taddiu    $1, $zero, {int(float(value))}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                elif valueType == "nameIdentifier":
                    newAdress = self.functions[funcName][0][value]
                    if self.table.symbol_table.get_symbol(value, funcName)[0] == "char":
                        self.output += f"\tlbu   $1, {newAdress}($fp)\n"
                    else:
                        self.output += f"\tlw   $1, {newAdress}($fp)\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
                else:
                    self.output += f"\taddiu    $1, $zero, {ord(value[1])}\n"
                    self.output += f"\tsb   $1, {adress}($fp)\n"
        else:
            reference = ast.children[2].children[1].children[0].node.getRuleName()
            newAdress = self.functions[funcName][0][reference]
            if type == "int":
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"
            elif type == "float":
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"
            else:
                self.output += f"\taddiu    $1, $fp, {newAdress}\n"
                self.output += f"\tsw   $1, {adress}($fp)\n"
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
                if valueType == "char":
                    self.output += f"{name}:\n\t.4byte {ord(value[1])}\n"
                else:
                    self.output += f"{name}:\n\t.4byte {value}\n"
            elif type == "float":
                if valueType == "char":
                    self.output += f"{name}:\n\t.4byte {float.hex(float(ord(value[1])))}\n"
                else:
                    self.output += f"{name}:\n\t.4byte {float.hex(float(value))}\n"
            else:
                if valueType == "int":
                    self.output += f"{name}:\n\t.byte {value}\n"
                elif valueType == "float":
                    self.output += f"{name}:\n\t.byte {int(float(value))}\n"
                else:
                    self.output += f"{name}:\n\t.byte {ord(value[1])}\n"
        else:
            if type == "int":
                self.output += f"{name}:\n\t.4byte {value}\n"
            elif type == "float":
                self.output += f"{name}:\n\t.4byte {value}\n"
            else:
                self.output += f"{name}:\n\t.byte {value}\n"


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
            self.output += f"{name}:\n\t.4byte {0}\n"
        elif type == "float":
            self.output += f"{name}:\n\t.4byte {0x00000000}\n"
        else:
            self.output += f"{name}:\n\t.byte {0}\n"

    def printMips(self, fileName):
        fileName += ".asm"
        file = open(fileName, "w")
        file.write(self.output)



