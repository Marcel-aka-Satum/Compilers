from SymbolTable import *


class SemanticAnalysisVisitor:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.line = 0
        self.collom = 0;
        self.error = False
        self.currScope = None
        self.funcScope = None
        self.ret = None
        self.lib = False

    def visit(self, node):
        self.line = node.node.getLine()
        self.collom = node.node.getCollom()
        if node.node.getRuleName() == "variableDefinition":
            self.visit_variable_definition(node)
        elif node.node.getRuleName() == "variableDeclaration":
            self.visit_variable_declaration(node)
        elif node.node.getRuleName() == "nameIdentifier":
            self.visit_name_identifier(node)
        elif node.node.getRuleName() == "assignmentStatement":
            self.visit_assignment_statement(node)
        elif node.node.getRuleName() == "funcDefinition":
            self.visitFuncDef(node)
        elif node.node.getRuleName() == "funcDeclaration":
            self.visitFuncDecl(node)
        elif node.node.getRuleName() == "functionCall":
            self.visitFuncCall(node)
        elif node.node.getRuleName() == "arrDef":
            self.visitArrDef(node)
        elif node.node.getRuleName() == "arrDecl":
            self.visitArrDecl(node)
        elif node.node.getRuleName() == "arrAssign":
            self.visitArrAssign(node)
        elif node.node.getRuleName() == "arrCall":
            self.visitArrCall(node)
        elif node.node.getRuleName() == "returnStatement":
            self.visitReturn(node)
        elif node.node.getRuleName() == "opCompare":
            left = node.children[0]
            right = node.children[2]
            temp = False
            if left.node.getRuleName() == "nameIdentifier":
                check = self.symbol_table.get_symbol(left.children[0].node.getRuleName(), self.currScope)
                if check != None:
                    if len(check) == 4:
                        temp = True
                        print(f"[ Error ] at line {self.line} at position {self.collom}: cannot compare an array")
                        self.error = True
            if right.node.getRuleName() == "nameIdentifier":
                check = self.symbol_table.get_symbol(right.children[0].node.getRuleName(), self.currScope)
                if check != None:
                    if len(check) == 4 and not temp:
                        print(f"[ Error ] at line {self.line} at position {self.collom}: cannot compare an array")
                        self.error = True
            for child in node.children:
                self.visit(child)
        elif node.node.getRuleName() == "lib":
            self.lib = True
            for child in node.children:
                self.visit(child)
        elif node.node.getRuleName() == "printFunction" or node.node.getRuleName() == "scanFunction":
            self.visitPrintOrScan(node)
        elif node.node.getRuleName()[:12] == "unNamedScope" or node.node.getRuleName()[:11] == "ifStatement" or node.node.getRuleName()[:13] == "elifStatement" or node.node.getRuleName()[:13] == "elseStatement" or node.node.getRuleName()[:14] == "whileStatement" or node.node.getRuleName()[:7] == "forLoop":
            if self.currScope != None:
                self.symbol_table.scopes[node.node.getRuleName()] = [None, self.currScope]
                arr = self.symbol_table.scopes[self.currScope]
                if arr != None:
                    for i in arr:
                        if i not in self.symbol_table.scopes[node.node.getRuleName()]:
                            self.symbol_table.scopes[node.node.getRuleName()].append(i)
            self.addScope(node)
        elif node.node.getRuleName() == "}":
            if self.currScope != None:
                if self.currScope[:12] != "unNamedScope" and self.currScope[:11] != "ifStatement" and self.currScope[:13] != "elifStatement" and self.currScope[:13] != "elseStatement" and self.currScope[:14] != "whileStatement" and self.currScope[:7] != "forLoop":
                    name = self.funcScope
                    if len(self.symbol_table.funcDict[name]) == 2:
                        type = self.symbol_table.funcDict[name][1][0]
                    else:
                        type = self.symbol_table.funcDict[name][0]
                    if type != "void":
                        if self.ret == None and self.currScope != "main":
                            print(f"[ Error ] at line {self.line} at position {self.collom}: non-void function {name} needs to return a {type}")
                            self.error = True
                    self.funcScope = None
                    self.ret = None

            if self.currScope in self.symbol_table.scopes:
                if self.symbol_table.scopes[self.currScope] == [None] or self.symbol_table.scopes[self.currScope] == None:
                    self.currScope = None
                else:
                    self.currScope = self.symbol_table.scopes[self.currScope][1]

            else:
                self.currScope = None
            self.line += 1
        else:
            for child in node.children:
                self.visit(child)

    def visitArrCall(self, node):
        name = node.children[0].children[0].node.getRuleName()
        if node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
            print(f"[ Error ] at line {self.line} at position {self.collom}: size of array {name} has to be an int")
            self.error = True
        check = self.symbol_table.get_symbol(name, self.currScope)
        if check != None:
            if len(check) != 4:
                print(f"[ Error ] at line {self.line} at position {self.collom}: {name} is not an array, can not acces the given index")
                self.error = True
        for child in node.children:
            self.visit(child)

    def visitArrDecl(self, node):
        name = node.children[1].node.getRuleName()
        check = self.symbol_table.get_symbol(name, self.currScope)
        if check is not None:
            print(f"[ Error ] at line {self.line} at position {self.collom}: array {name} has already been defined or declared")
            self.error = True
        type = None
        const = False
        pointer = False
        size = None
        if node.children[3].node.getRuleName() == "float" or node.children[3].node.getRuleName() == "char":
            print(f"[ Error ] at line {self.line} at position {self.collom}: size of array {name} has to be an int")
            self.error = True
        try:
            sizeArr = int(node.children[3].children[0].node.getRuleName())
        except:
            sizeArr = node.children[3].children[0].node.getRuleName()
        if node.children[0].node.getRuleName() == "constWord":
            const = True
            if node.children[0].children[1].node.getRuleName() == "pointerWord":
                pointer = True
                type = node.children[0].children[1].children[0].children[0].node.getRuleName()
                size = len(node.children[0].children[1].children[1].node.getRuleName())
            else:
                type = node.children[0].children[1].children[0].node.getRuleName()
        elif node.children[0].node.getRuleName() == "pointerWord":
            pointer = True
            type = node.children[0].children[0].children[0].node.getRuleName()
            size = len(node.children[0].children[1].node.getRuleName())
        elif node.children[0].node.getRuleName() == "reservedWord":
            type = node.children[0].children[0].node.getRuleName()
        if const and pointer:
            tempArr = [type, ["const pointer", size], None, sizeArr]
        elif const and not pointer:
            tempArr = [type, ["const", size], None, sizeArr]
        elif pointer and not const:
            tempArr = [type, ["pointer", size], None, sizeArr]
        elif not pointer and not const:
            tempArr = [type, [None, size], None, sizeArr]
        self.symbol_table.insert_symbol(name, tempArr, self.currScope)
        for child in node.children:
            self.visit(child)

    def visitPrintOrScan(self, node):
        if not self.lib:
            print(f"[ Error ] at line {self.line} at position {self.collom}: cannot use function without including stdio.h")
            self.error = True
        arg = node.children[0].children[0].children[0].node.getRuleName()
        count = arg.count("%")
        tempCount = 0
        for i in node.children[0].children:
            if i.node.getRuleName() != "," and i.node.getRuleName() != "string":
                tempCount += 1
        if tempCount != count:
            print(f"[ Error ] at line {self.line} at position {self.collom}: function expected {count} arguments but {tempCount} were given")
            self.error = True

        for child in node.children:
            self.visit(child)

    def visitReturn(self, node):
        self.ret = True
        name = self.funcScope
        if len(self.symbol_table.funcDict[name]) == 2:
            type = self.symbol_table.funcDict[name][1][0]
        else:
            type = self.symbol_table.funcDict[name][0]
        if type == "void":
            if len(node.children) != 1:
                print(f"[ Error ] at line {self.line} at position {self.collom}: void function {name} cannot return a type")
                self.error = True
        else:
            varType = node.children[1].node.getRuleName()
            if varType == "int" or varType == "float" or varType == "char":
                if type != varType:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} returned a {varType} but expected an {type}")
                    self.error = True
            elif varType == "nameIdentifier":
                varName = node.children[1].children[0].node.getRuleName()
                varType = self.symbol_table.get_symbol(varName, name)[0]
                if type != varType:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} returned a {varType} but expected an {type}")
                    self.error = True
        for child in node.children:
            self.visit(child)

    def visitArrAssign(self, node):
        name = node.children[0].node.getRuleName()
        arr = self.symbol_table.get_symbol(name, self.currScope)
        if node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
            print(f"[ Error ] at line {self.line} at position {self.collom}: size of array {name} has to be an int")
            self.error = True
        if arr == None:
            print(f"[ Error ] at line {self.line} at position {self.collom}: Array {name} has not been initialized or declared")
            self.error = True
        else:
            isConst = False
            if arr[1][0] == "const" or arr[1][0] == "const pointer":
                print(f"[ Error ] at line {self.line} at position {self.collom}: {name} is a const array, wich can not be reassigned")
                self.error = True
            else:
                type = arr[0]
                i = node.children[5]
                if i.node.getRuleName() == "int":
                    if type == "float":
                        new = float(i.children[0].node.getRuleName())
                        i.node.ruleName = "float"
                        i.children[0].node.ruleName = new
                    elif type == "char":
                        new = chr(int(i.children[0].node.getRuleName()))
                        i.node.ruleName = "char"
                        i.children[0].node.ruleName = new
                elif i.node.getRuleName() == "float":
                    if type == "int":
                        temp = float(i.children[0].node.getRuleName())
                        new = int(temp)
                        i.node.ruleName = "int"
                        i.children[0].node.ruleName = new
                    elif type == "char":
                        temp = float(i.children[0].node.getRuleName())
                        new = chr(int(temp))
                        i.node.ruleName = "char"
                        i.children[0].node.ruleName = new
                elif i.node.getRuleName() == "char":
                    if type == "int":
                        temp = i.children[0].node.getRuleName()[1]
                        new = ord(temp)
                        i.node.ruleName = "int"
                        i.children[0].node.ruleName = new
                    elif type == "float":
                        temp = ord(i.children[0].node.getRuleName()[1])
                        new = float(temp)
                        i.node.ruleName = "float"
                        i.children[0].node.ruleName = new
        for child in node.children:
            self.visit(child)

    def visitArrDef(self, node):
        name = node.children[1].node.getRuleName()
        check = self.symbol_table.get_symbol(name, self.currScope)
        if check is not None:
            print(f"[ Error ] at line {self.line} at position {self.collom}: array {name} has already been defined or declared")
            self.error = True
        type = None
        const = False
        pointer = False
        size = None
        rightSide = node.children[6]
        if node.children[3].node.getRuleName() == "float" or node.children[3].node.getRuleName() == "char":
            print(f"[ Error ] at line {self.line} at position {self.collom}: size of array {name} has to be an int")
            self.error = True
        try:
            sizeArr = int(node.children[3].children[0].node.getRuleName())
        except:
            sizeArr = node.children[3].children[0].node.getRuleName()
        if node.children[0].node.getRuleName() == "constWord":
            const = True
            if node.children[0].children[1].node.getRuleName() == "pointerWord":
                pointer = True
                type = node.children[0].children[1].children[0].children[0].node.getRuleName()
                size = len(node.children[0].children[1].children[1].node.getRuleName())
            else:
                type = node.children[0].children[1].children[0].node.getRuleName()
        elif node.children[0].node.getRuleName() == "pointerWord":
            pointer = True
            type = node.children[0].children[0].children[0].node.getRuleName()
            size = len(node.children[0].children[1].node.getRuleName())
        elif node.children[0].node.getRuleName() == "reservedWord":
            type = node.children[0].children[0].node.getRuleName()
        if const and pointer:
            tempArr = [type, ["const pointer", size], rightSide, sizeArr]
        elif const and not pointer:
            tempArr = [type, ["const", size], rightSide, sizeArr]
        elif pointer and not const:
            tempArr = [type, ["pointer", size], rightSide, sizeArr]
        elif not pointer and not const:
            tempArr = [type, [None, size], rightSide, sizeArr]
        for i in rightSide.children:
            if i.node.getRuleName() == "int":
                if type == "float":
                    new = float(i.children[0].node.getRuleName())
                    i.node.ruleName = "float"
                    i.children[0].node.ruleName = new
                elif type == "char":
                    new = chr(int(i.children[0].node.getRuleName()))
                    i.node.ruleName = "char"
                    i.children[0].node.ruleName = new
            elif i.node.getRuleName() == "float":
                if type == "int":
                    temp = float(i.children[0].node.getRuleName())
                    new = int(temp)
                    i.node.ruleName = "int"
                    i.children[0].node.ruleName = new
                elif type == "char":
                    temp = float(i.children[0].node.getRuleName())
                    new = chr(int(temp))
                    i.node.ruleName = "char"
                    i.children[0].node.ruleName = new
            elif i.node.getRuleName() == "char":
                if type == "int":
                    temp = i.children[0].node.getRuleName()[1]
                    new = ord(temp)
                    i.node.ruleName = "int"
                    i.children[0].node.ruleName = new
                elif type == "float":
                    temp = ord(i.children[0].node.getRuleName()[1])
                    new = float(temp)
                    i.node.ruleName = "float"
                    i.children[0].node.ruleName = new
        self.symbol_table.insert_symbol(name, tempArr, self.currScope)
        for child in node.children:
            self.visit(child)
    def addScope(self, node):
        self.currScope = node.node.getRuleName()
        if self.currScope not in self.symbol_table.scopes:
            self.symbol_table.scopes[self.currScope] = None
        for child in node.children:
            self.visit(child)

    def findReturn(self, node):
        if node.node.getRuleName() == "returnStatement":
            return [True, node]
        else:
            temp = [False, None]
            for i in node.children:
                temp = self.findReturn(i)
            return temp

    def visitFuncDef(self, node):
        name = node.children[1].node.getRuleName()
        check = False
        temp = node
        while not check:
            if temp.parent.node.getRuleName() == "conditionStatement" or temp.parent.node.getRuleName() == "funcDefinition" or temp.parent.node.getRuleName()[:12] == "unNamedScope" or temp.parent.node.getRuleName()[:11] == "ifStatement" or temp.parent.node.getRuleName()[:13] == "elifStatement" or temp.parent.node.getRuleName()[:13] == "elseStatement" or temp.parent.node.getRuleName()[:14] == "whileStatement" or temp.parent.node.getRuleName()[:7] == "forLoop":
                check = True
            elif temp.parent.node.getRuleName() == "prog":
                break
            else:
                 temp = temp.parent
        if check:
            print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} cannot be defined in a local scope")
            self.error = True
        if node.children[0].node.getRuleName() == "reservedWord":
            type = node.children[0].children[0].node.getRuleName()
            typeValue = [False, None]
        elif node.children[0].node.getRuleName():
            type = node.children[0].children[0].children[0].node.getRuleName()
            size = len(node.children[0].children[1].node.getRuleName())
            typeValue = [True, size]
        if name in self.symbol_table.funcDict:
            if len(self.symbol_table.funcDict[name]) == 3:
                print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} has already been defined")
                self.error = True
        self.currScope = name
        self.funcScope = name
        self.addScope(node.children[1])
        arguments = dict()
        temp = node.children[2]
        count = 0
        if temp.node.getRuleName() == "{":
            arguments = None
        else:
            for i in range(len(temp.children)):
                if temp.children[i].node.getRuleName() == "reservedWord":
                    argName = temp.children[i + 1].node.getRuleName()
                    argType = temp.children[i].children[0].node.getRuleName()
                    arguments[count] = [[False, None], argType]
                    input = [argType, [None, None], None]
                    self.symbol_table.insert_symbol(argName, input, name)
                    count += 1
                elif temp.children[i].node.getRuleName() == "constWord":
                    argName = temp.children[i + 1].node.getRuleName()
                    if temp.children[i].children[1].node.getRuleName() == "pointerWord":
                        argType = temp.children[i].children[1].children[0].children[0].node.getRuleName()
                        size = len(temp.children[i].children[1].children[1].node.getRuleName())
                        arguments[count] = [[True, size], argType]
                        input = [argType, ["const pointer", size], None]
                        self.symbol_table.insert_symbol(argName, input, name)
                    else:
                        argType = temp.children[i].children[1].children[0].node.getRuleName()
                        arguments[count] = [[False, None], argType]
                        input = [argType, ["const", None], None]
                        self.symbol_table.insert_symbol(argName, input, name)
                    count += 1
                elif temp.children[i].node.getRuleName() == "pointerWord":
                    argName = temp.children[i + 1].node.getRuleName()
                    argType = temp.children[i].children[0].children[0].node.getRuleName()
                    size = len(temp.children[i].children[1].node.getRuleName())
                    arguments[count] = [[True, size], argType]
                    input = [argType, ["pointer", size], None]
                    self.symbol_table.insert_symbol(argName, input, name)
                    count += 1
        value = [type, arguments, typeValue]
        if name in self.symbol_table.funcDict:
            if len(self.symbol_table.funcDict[name]) == 2:
                arr = self.symbol_table.funcDict[name][1]
            else:
                arr = self.symbol_table.funcDict[name]
            if arr != value:
                print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} has not been declared correctly")
                self.error = True
        else:
            self.symbol_table.funcDict[name] = value

        for child in node.children:
            self.visit(child)

    def visitFuncDecl(self, node):
        name = node.children[1].node.getRuleName()
        if node.children[0].node.getRuleName() == "reservedWord":
            type = node.children[0].children[0].node.getRuleName()
            typeValue = [False, None]
        elif node.children[0].node.getRuleName():
            type = node.children[0].children[0].children[0].node.getRuleName()
            size = len(node.children[0].children[1].node.getRuleName())
            typeValue = [True, size]
        if name in self.symbol_table.funcDict:
            arguments = dict()
            temp = node.children[2]
            count = 0
            if len(node.children) == 2:
                arguments = None
            else:
                for i in range(len(temp.children)):
                    if temp.children[i].node.getRuleName() == "reservedWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        argType = temp.children[i].children[0].node.getRuleName()
                        arguments[count] = [[False, None], argType]
                        count += 1
                    elif temp.children[i].node.getRuleName() == "constWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        if temp.children[i].children[1].node.getRuleName() == "pointerWord":
                            argType = temp.children[i].children[1].children[0].children[0].node.getRuleName()
                            size = len(temp.children[i].children[1].children[1].node.getRuleName())
                            arguments[count] = [[True, size], argType]
                        else:
                            argType = temp.children[i].children[1].children[0].node.getRuleName()
                            arguments[count] = [[False, None], argType]
                        count += 1
                    elif temp.children[i].node.getRuleName() == "pointerWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        argType = temp.children[i].children[0].children[0].node.getRuleName()
                        size = len(temp.children[i].children[1].node.getRuleName())
                        arguments[count] = [[True, size], argType]
                        count += 1
            if len(self.symbol_table.funcDict[name]) == 2:
                arr1 = self.symbol_table.funcDict[name][1]
                arr2 = [type, arguments, typeValue]
                if arr1 != arr2:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} has not been declared correctly")
                    self.error = True
            else:
                arr1 = self.symbol_table.funcDict[name]
                arr2 = [type, arguments, typeValue]
                if arr1 != arr2:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} has not been declared correctly")
                    self.error = True


        else:
            arguments = dict()
            temp = node.children[2]
            count = 0
            if len(node.children) == 2:
                arguments = None
            else:
                for i in range(len(temp.children)):
                    if temp.children[i].node.getRuleName() == "reservedWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        argType = temp.children[i].children[0].node.getRuleName()
                        arguments[count] = [[False, None], argType]
                        count += 1
                    elif temp.children[i].node.getRuleName() == "constWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        if temp.children[i].children[1].node.getRuleName() == "pointerWord":
                            argType = temp.children[i].children[1].children[0].children[0].node.getRuleName()
                            size = len(temp.children[i].children[1].children[1].node.getRuleName())
                            arguments[count] = [[True, size], argType]
                        else:
                            argType = temp.children[i].children[1].children[0].node.getRuleName()
                            arguments[count] = [[False, None], argType]
                        count += 1
                    elif temp.children[i].node.getRuleName() == "pointerWord":
                        argName = temp.children[i + 1].node.getRuleName()
                        argType = temp.children[i].children[0].children[0].node.getRuleName()
                        size = len(temp.children[i].children[1].node.getRuleName())
                        arguments[count] = [[True, size], argType]
                        count += 1
            value = [type, arguments, typeValue]
            self.symbol_table.funcDict[name] = [None, value]

    def visitFuncCall(self, node):
        name = node.children[0].node.getRuleName()
        if name not in self.symbol_table.funcDict:
            print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} has not been declared or defined")
            self.error = True
        else:
            if len(self.symbol_table.funcDict[name]) == 2:
                arr = self.symbol_table.funcDict[name][1]
            else:
                arr = self.symbol_table.funcDict[name]
            if arr[1] != None:
                size = len(arr[1])
                count = 0
                temp = False
                for i in node.children[1].children:
                    type = None
                    extra = None
                    if i.node.getRuleName() != ",":
                        if count > size - 1:
                            print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} expects {size} arguments but more were given")
                            self.error = True
                            temp = True
                        if i.node.getRuleName() == "int" or i.node.getRuleName() == "float" or i.node.getRuleName() == "char":
                            type = [[False, None], i.node.getRuleName()]
                        elif i.node.getRuleName() == "referenceID":
                            varName = i.children[1].children[0].node.getRuleName()
                            varType = self.symbol_table.get_symbol(varName, self.currScope)[0]
                            if i.children[0].node.getRuleName() == "&":
                                type = [[True, None], varType]
                                extra = True
                            else:
                                varSize = len(i.children[0].node.getRuleName())
                                checkSize = self.symbol_table.get_symbol(varName, self.currScope)[1][1]
                                if varSize != checkSize:
                                    print(f"[ Error ] at line {self.line} at position {self.collom}: {varName} expects {checkSize} pointer but got {varSize} instead")
                                    self.error = True
                                type = [[False, None], varType]
                        else:
                            if len(i.children) != 0:
                                left = i.children[0]
                                right = i.children[2]
                                if left.node.getRuleName() == "nameIdentifier":
                                    temp1 = self.symbol_table.get_symbol(left.children[0].node.getRuleName(), self.currScope)[0]
                                else:
                                    temp1 = left.node.getRuleName()

                                if right.node.getRuleName() == "nameIdentifier":
                                    temp2 = self.symbol_table.get_symbol(right.children[0].node.getRuleName(), self.currScope)[0]
                                else:
                                    temp2 = right.node.getRuleName()

                                if temp1 == temp2:
                                    type = [[False, None], temp1]
                                else:
                                    if temp1 == "int" and temp2 == "float":
                                        type = [[False, None], temp2]
                                    elif temp1 == "float" and temp2 == "int":
                                        type = [[False, None], temp1]
                                    elif temp1 == "float" and temp2 == "char":
                                        type = [[False, None], temp1]
                                    elif temp1 == "char" and temp2 == "float":
                                        type = [[False, None], temp2]
                                    elif temp1 == "int" and temp2 == "char":
                                        type = [[False, None], temp1]
                                    elif temp1 == "char" and temp2 == "int":
                                        type = [[False, None], temp2]
                            else:
                                varName = i.node.getRuleName()
                                varType = self.symbol_table.get_symbol(varName, self.currScope)[0]
                                varPointer = self.symbol_table.get_symbol(varName, self.currScope)[1][0]
                                if varPointer == "const pointer" or varPointer == "pointer":
                                    varSize = self.symbol_table.get_symbol(varName, self.currScope)[1][1]
                                    type = [[True, varSize], varType]
                                else:
                                    type = [[False, None], varType]
                        checkValue = arr[1][count]
                        if checkValue[1] != type[1]:
                            print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} argument {count} expects a {checkValue[1]} but got an {type[1]} instead")
                            self.error = True
                        if checkValue[0][0] == True:
                            if type[0][0] != True:
                                print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} argument {count} expects an adress but got an value instead")
                                self.error = True
                            elif checkValue[0][1] != type[0][1] and not extra:
                                print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} argument {count} expects an {checkValue[0][1]} pointer but got {type[0][1]} instead")
                                self.error = True
                        if checkValue[0][0] == False and checkValue[0][1] == None:
                            if type[0][0] != False:
                                print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} argument {count} expects a value but got an adress instead")
                                self.error = True
                        count += 1
                if count != size and not temp:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: function {name} expects {size} arguments but less were given")
                    self.error = True






    def visit_assignment_statement(self, node):
        possible = True
        if node.children[0].node.getRuleName() != "nameIdentifier" and node.children[0].node.getRuleName() != "referenceID":
            print(f"[ Error ] at line {self.line} at position {self.collom}: assignment to an rvalue")
            self.error = True
        if node.children[0].node.getRuleName() == "nameIdentifier":
            var_name = node.children[0].children[0].node.getRuleName()
        else:
            var_name = node.children[0].children[1].children[0].node.getRuleName()
            if node.children[0].children[0].node.getRuleName() == "&":
                print(f"[ Error ] at line {self.line} at position {self.collom}: assignment to rvalue, cannot assign an address")
                self.error = True
        check = None
        if self.symbol_table.get_symbol(var_name, self.currScope) != None:
            check = self.symbol_table.get_symbol(var_name, self.currScope)[1][0]
            if check == "const" or check == "const pointer":
                if check == "const pointer" and node.children[2].node.getRuleName() == "referenceID":
                    if node.children[0].node.getRuleName() == "referenceID":
                        if node.children[0].children[0].node.getRuleName() == "*":
                            print(f"[ Error ] at line {self.line} at position {self.collom}: Can not assign variable {var_name} with type const")
                            self.error = True
                else:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: Can not assign variable {var_name} with type const")
                    self.error = True
        else:
            print(f"[ Error ] at line {self.line} at position {self.collom}: Can not assign the undeclared variable {var_name}")
            self.error = True
        if check == "pointer":
            if node.children[2].node.getRuleName() != "referenceID":
                if node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName()[0] != '*':
                        print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an address")
                        self.error = True
                    else:
                        size = self.symbol_table.get_symbol(var_name, self.currScope)[1][1]
                        if len(node.children[0].children[0].node.getRuleName()) != size:
                            print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects a {size} pointer")
                            self.error = True
                else:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an address")
                    self.error = True
            if node.children[0].node.getRuleName() == "referenceID":
                type = self.symbol_table.get_symbol(var_name, self.currScope)[0]
                if node.children[0].children[0].node.getRuleName()[0] == '*':
                    possible = False
                    if node.children[2].node.getRuleName() == "nameIdentifier":
                        if type != "int" and type != "float" and type != "char":
                            print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            self.error = True
                    elif node.children[2].node.getRuleName() == "referenceID":
                        print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                        self.error = True

        type = self.symbol_table.get_symbol(var_name, self.currScope)[0]
        if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID" and node.children[2].children[0].node.getRuleName()[0] != '*':
            if check != "pointer" and check != "const pointer":
                print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expects a value but an adress was given")
                self.error = True
        elif (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID" and node.children[2].children[0].node.getRuleName()[0] == '*':
            varName = node.children[2].children[1].children[0].node.getRuleName()
            varType = self.symbol_table.get_symbol(varName, self.currScope)[1][0]
            count = self.symbol_table.get_symbol(varName, self.currScope)[1][1]
            if varType == "pointer" or varType == 'const pointer':
                if count == len(node.children[2].children[0].node.getRuleName()):
                    pass
                else:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects a {count} pointer")
                    self.error = True
            else:
                print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: {varName} is not a pointer")
                self.error = True

        if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
            if type == "int":
                if node.children[2].node.getRuleName() == "char":
                    rightSide = ord(node.children[2].children[0].node.getRuleName()[1])
                else:
                    try:
                        rightSide = int(node.children[2].children[0].node.getRuleName())
                    except ValueError:
                        rightSide = float(node.children[2].children[0].node.getRuleName())
                        rightSide = int(rightSide)
            elif type == "float":
                if node.children[2].node.getRuleName() == "char":
                    rightSide = ord(node.children[2].children[0].node.getRuleName()[1])
                else:
                    rightSide = float(node.children[2].children[0].node.getRuleName())
            else:
                if node.children[2].node.getRuleName() == "int":
                    temp = self.symbol_table.get_symbol(var_name, self.currScope)
                    newArr = ["int", temp[1], temp[2]]
                    self.symbol_table.symbol_tables[-1][var_name] = newArr
                    rightSide = int(node.children[2].children[0].node.getRuleName())
                elif node.children[2].node.getRuleName() == "float":
                    temp = self.symbol_table.get_symbol(var_name, self.currScope)
                    newArr = ["int", temp[1], temp[2]]
                    self.symbol_table.symbol_tables[-1][var_name] = newArr
                    temp2 = float(node.children[2].children[0].node.getRuleName())
                    temp2 = int(temp2)
                    rightSide = temp2
                else:
                    rightSide = node.children[2].children[0].node.getRuleName()[1]
        elif node.children[2].node.getRuleName() == "nameIdentifier":
            type2 = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName(), self.currScope)[0]
            if (type == "int" or type == "float") and type2 == "char":
                print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expected int or float")
                self.error = True
            elif type == "char" and (type2 == "int" or type2 == "float"):
                print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expected char")
                self.error = True
            varType = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName(), self.currScope)[1][0]
            if varType == "pointer" or varType == "const pointer":
                print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expected char but got assigned an pointer")
                self.error = True
            rightSide = self.symbol_table.get_symbol(node.children[2].children[0].node.getRuleName(), self.currScope)[2]
        else:
            rightSide = node.children[2]
        if possible:
            self.symbol_table.insert_value(var_name, rightSide, self.currScope)

        for child in node.children:
            self.visit(child)
    def visit_variable_declaration(self, node):
        if node.parent.node.getRuleName() != "variableDefinition":
            var_name = node.children[1].children[0].node.getRuleName()
            # Check if the variable has already been defined in the current scope
            if self.symbol_table.get_symbol(var_name, self.currScope) is not None:
                print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} has already been defined in the current scope")
                self.error = True
            # Check if the variable is not declared const
            extra = None
            size = None
            if node.children[0].node.getRuleName() == "constWord":
                print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} needs to be initialised because it is declared const")
                self.error = True
            elif node.children[0].node.getRuleName() == "pointerWord":
                extra = "pointer"
                size = len(node.children[0].children[1].node.getRuleName())


            # Add the variable to the symbol table
            if extra == "pointer":
                type = node.children[0].children[0].children[0].node.getRuleName()
            else:
                type = node.children[0].children[0].node.getRuleName()
            tempArray = [type, [extra, size], None]
            self.symbol_table.insert_symbol(var_name, tempArray, self.currScope)

        # Visit its children
        for child in node.children:
            self.visit(child)




    def visit_variable_definition(self, node):
        # Check if the variable has already been defined in the current scope
        var_name = node.children[0].children[1].children[0].node.getRuleName()
        test1 = False
        test2 = False
        if self.currScope in self.symbol_table.symbol_tables:
            test1 = True
        if test1:
            if var_name in self.symbol_table.symbol_tables[self.currScope]:
                test2 = True
        if test1 and test2:
            print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} has already been defined in the current scope")
            self.error = True
        else:
            # Add the variable to the symbol table
            extra = None
            size = None
            if node.children[0].children[0].node.getRuleName() == "constWord":
                extra = "const"
            if node.children[0].children[0].node.getRuleName() != "reservedWord":
                if node.children[0].children[0].children[1].node.getRuleName() == "pointerWord":
                    extra = "const pointer"
                    size = len(node.children[0].children[0].children[1].children[1].node.getRuleName())
                if node.children[0].children[0].node.getRuleName() == "pointerWord":
                    extra = "pointer"
                    size = len(node.children[0].children[0].children[1].node.getRuleName())
            if extra == "const":
                type = node.children[0].children[0].children[1].children[0].node.getRuleName()
            elif extra == "pointer":
                type = node.children[0].children[0].children[0].children[0].node.getRuleName()
            elif extra == "const pointer":
                type = node.children[0].children[0].children[1].children[0].children[0].node.getRuleName()
            else:
                type = node.children[0].children[0].children[0].node.getRuleName()
            if extra == "pointer" or extra == "const pointer":
                if node.children[2].node.getRuleName() != "referenceID":
                    newName = node.children[2].children[0].node.getRuleName()
                    newSize = self.symbol_table.get_symbol(newName, self.currScope)[1][1]
                    if newSize == None or size != newSize:
                        print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an address")
                        self.error = True
                elif node.children[0].node.getRuleName() == "referenceID":
                    if node.children[0].children[0].node.getRuleName() == "*":
                        if node.children[2].node.getRuleName() == "nameIdentifier":
                            if type != "int" and type != "float" and type != "char":
                                print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                                self.error = True
                        elif node.children[2].node.getRuleName() == "referenceID":
                            print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects an int or float or char")
                            self.error = True

            if (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "referenceID":
                if extra != "pointer" and extra != "const pointer":
                    if node.children[2].children[0].node.getRuleName()[0] == '*':
                        varName = node.children[2].children[1].children[0].node.getRuleName()
                        varType = self.symbol_table.get_symbol(varName, self.currScope)[1][0]
                        count = self.symbol_table.get_symbol(varName, self.currScope)[1][1]
                        if varType == "pointer" or varType == 'const pointer':
                            if count == len(node.children[2].children[0].node.getRuleName()):
                                pass
                            else:
                                print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} can't assign incompatible type: expects a {count} pointer")
                                self.error = True
                        else:
                            print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: {varName} is not a pointer")
                            self.error = True
                    else:
                        print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expects a value but got an adress instead")
                        self.error = True
                else:
                    if node.children[2].children[0].node.getRuleName() != "&":
                        print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type")
                        self.error = True
            elif (type == "int" or type == "float" or type == "char") and node.children[2].node.getRuleName() == "nameIdentifier":
                nodeName = node.children[2].children[0].node.getRuleName()
                if self.symbol_table.get_symbol(nodeName, self.currScope) == None:
                    print(f"[ Error ] at line {self.line} at position {self.collom}: variable {nodeName} has not been initialised or declared")
                    self.error = True
                type3 = self.symbol_table.get_symbol(nodeName, self.currScope)[1][0]
                corrType = self.symbol_table.get_symbol(nodeName, self.currScope)[0]
                if type3 == "pointer" or type3 == "const pointer":
                    if extra != "pointer" and extra != "const pointer":
                        print(f"[ Error ] at line {self.line} at position {self.collom}: {var_name} got assigned an incompatible type: expected value but got assigned an pointer instead ")
                        self.error = True
                if type == "int" and corrType == "float":
                    print(f"[ Warning ] at line {self.line} at position {self.collom}: variable {var_name} has loss of information (float to int)")

            if node.children[2].node.getRuleName() == "int" or node.children[2].node.getRuleName() == "float" or node.children[2].node.getRuleName() == "char":
                if type == "int":
                    if node.children[2].node.getRuleName() == "char":
                        rightSide = ord(node.children[2].children[0].node.getRuleName()[1])
                    else:
                        try:
                            rightSide = int(node.children[2].children[0].node.getRuleName())
                        except ValueError:
                            rightSide = float(node.children[2].children[0].node.getRuleName())
                            rightSide = int(rightSide)
                            print(f"[ Warning ] at line {self.line} at position {self.collom}: variable {var_name} has loss of information (float to int)")
                        node.children[2].node.ruleName = "int"
                        node.children[2].children[0].node.ruleName = rightSide
                elif type == "float":
                    if node.children[2].node.getRuleName() == "char":
                        rightSide = ord(node.children[2].children[0].node.getRuleName()[1])
                    else:
                        rightSide = float(node.children[2].children[0].node.getRuleName())
                else:
                    if node.children[2].node.getRuleName() == "int":
                        type = "int"
                        rightSide = int(node.children[2].children[0].node.getRuleName())
                    elif node.children[2].node.getRuleName() == "float":
                        temp = float(node.children[2].children[0].node.getRuleName())
                        temp = int(temp)
                        rightSide = temp
                        type = "int"
                    else:
                        rightSide = node.children[2].children[0].node.getRuleName()[1]
                        if rightSide == '\\':
                            rightSide = node.children[2].children[0].node.getRuleName()[1:3]
                            if rightSide == "\\n":
                                rightSide = ord('\n')
                            elif rightSide == "\\t":
                                rightSide = ord('\t')
                            elif rightSide == "\\r":
                                rightSide = ord('\r')
                            node.children[2].node.ruleName = "int"
                            node.children[2].children[0].node.ruleName = rightSide

            else:
                if node.children[2].node.getRuleName() == "referenceID":
                    if node.children[2].children[0].node.getRuleName()[0] == '*':
                        rightSide = node.children[2]
                    else:
                        rightSide = node.children[2].children[1].children[0].node.getRuleName()
                else:
                    rightSide = node.children[2]

            tempArray = [type, [extra, size], rightSide]
            self.symbol_table.insert_symbol(var_name, tempArray, self.currScope)

        # Visit its children
        for child in node.children:
            self.visit(child)

    def visit_name_identifier(self, node):
        # Check if the variable has been declared or initialised before it is used
        var_name = node.children[0].node.getRuleName()
        var_node = self.symbol_table.get_symbol(var_name, self.currScope)
        if var_node is None:
            print(f"[ Error ] at line {self.line} at position {self.collom}: Variable {var_name} has not been initialized or declared")
            self.error = True

        # Visit its children
        for child in node.children:
            self.visit(child)
