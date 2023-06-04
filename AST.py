from antlr4 import *
from MyGrammarParser import MyGrammarParser
import copy


class Node:
    def __init__(self, syntaxTree):
        try:
            self.line = syntaxTree.start.line
        except:
            self.line = 0
        try:
            self.collom = syntaxTree.start.column
        except:
            self.collom = 0

        if syntaxTree.getChildCount() > 0:
            self.ruleName = MyGrammarParser.ruleNames[syntaxTree.getRuleIndex()]
        else:
            self.ruleName = syntaxTree.getText()

    def getRuleName(self):
        return str(self.ruleName)

    def getLine(self):
        return self.line

    def getCollom(self):
        return self.collom


class AST:
    def __init__(self, syntaxTree):
        self.parent = None
        self.children = list()
        self.node = Node(syntaxTree)
        self.LLVM = ""
        self.register = ""  # every function in llvm has a register with data in it
        self.varNumbers = 1  # used for %1, %2, %... in llvm
        self.store = ""  # store for every variable for llvm
        self.smallTable = dict()  # {'%1': int, '%2' :i8*, '%3' :char} ...
        self.returnStatement = ""  # example (ret i32, 1)
        self.printFunction = ""  # @.str = private unnamed_addr constant [5 x i8] c"%d; \00"
        self.varNumbersPrint = 0  # used for .str.1, .str.2
        self.doneFormats = []  # used to store done formats ['%d', '%f']
        self.strDict = {}  # {'%d; ': '@.str', '%f; ': '@.str.2'}
        self.declareFunctions = ""
        self.initialised = False  # initialise registers from above first time in generate_LLVM
        self.registerDone = False
        self.isReturn = False
        self.table = None
        self.loaded = {}

        if syntaxTree.getChildCount() == 0: return
        newChild = ParserRuleContext()
        for newChild in syntaxTree.getChildren():
            temp = AST(newChild)
            temp.parent = self
            if temp.node.getRuleName() != "(" and temp.node.getRuleName() != ")" and temp.node.getRuleName() != ";" and temp.node.getRuleName() != "":
                self.children.append(temp)

    def set_table(self, tab):
        self.table = tab

    def generate_LLVM(self, ast):
        if not self.initialised:
            self.get_unnamed(ast)
            self.initialised = True
            self.LLVM += self.printFunction + '\n'
        for child in ast.children:
            # if child.node.getRuleName() == "comment":
            #     trimmedComment = child.children[0].node.getRuleName()[2:]
            #     trimmedComment = f";{trimmedComment}" + '\n'
            #     self.LLVM += trimmedComment
            if child.node.getRuleName() == "funcDefinition":
                ###clear registers with every functionDefinition
                self.register = ""  # clear register
                self.varNumbers = 0  # clear var numbers
                self.store = ""  # clear store vars
                self.printFunction = ""  # clear printFunctions
                self.declareFunctions = ""  # clear declareFunctions
                #################################
                if child.children[0].children[0].node.getRuleName() == "int":
                    self.LLVM += f"define dso_local i32 @{child.children[1].node.getRuleName()}() {child.children[2].node.getRuleName()}" + '\n'
                elif child.children[0].children[0].node.getRuleName() == "float":
                    self.LLVM += f"define dso_local @{child.children[1].node.getRuleName()}() {child.children[2].node.getRuleName()}" + '\n'
                self.parse_expr(child.children[3])  # add to register
                if self.registerDone is False:
                    self.LLVM += self.register
                if self.isReturn is False:
                    self.returnStatement = f"ret i32 0"
                self.LLVM += self.returnStatement + '\n' + "}" + '\n'
                self.LLVM += self.declareFunctions

            self.generate_LLVM(child)

    # helper function to parse expr in AST in order to produce LLVM
    def parse_expr(self, expr):
        for child in expr.children:
            if child.node.getRuleName() == "expr" and child.children[
                0].node.getRuleName() != "variableDefinition":  # store all register variables after ur done with variableDeclarations
                if child.parent.children[0].node.getRuleName() == "variableDefinition":
                    self.LLVM += self.register
                    self.LLVM += self.store
                    self.register = ""
                    self.store = ""
                    self.registerDone = True
            if child.node.getRuleName() == "expr" and child.children[0].node.getRuleName() == "returnStatement" and \
                    child.parent.children[0].node.getRuleName() == "printFunction":
                self.LLVM += self.register
                self.registerDone = True
            if child.node.getRuleName() == "expr" and child.children[0].node.getRuleName() == "returnStatement" and \
                    child.parent.children[0].node.getRuleName() == "conditionStatement":
                self.LLVM += self.register
                self.registerDone = True

            if child.node.getRuleName() == "comment":
                trimmedComment = child.children[0].node.getRuleName()[2:]
                trimmedComment = f";{trimmedComment}" + '\n'
                self.LLVM += trimmedComment

            if child.node.getRuleName() == "variableDeclaration":
                rightMostNode = get_rightmost_node(child.parent)
                self.varNumbers += 1
                if child.children[0].children[0].node.getRuleName() == "int":
                    self.register += f"%{self.varNumbers} = alloca i32, align 4" + '\n'
                    self.store += f"store i32 {rightMostNode.node.getRuleName()}, i32* %{self.varNumbers}, align 4" + '\n'
                elif child.children[0].children[0].node.getRuleName() == "float":
                    self.register += f"%{self.varNumbers} = alloca float, align 4" + '\n'
                    self.store += f"store float {rightMostNode.node.getRuleName()}, float* %{self.varNumbers}, align 4" + '\n'
                elif child.children[0].children[0].node.getRuleName() == "char":
                    self.register += f"%{self.varNumbers} = alloca i8, align 1" + '\n'
                    if (len(rightMostNode.node.getRuleName()) > 1):
                        self.store += f"store i8 {ord(rightMostNode.node.getRuleName()[1])}, i8* %{self.varNumbers}, align 1" + '\n'
                    else:
                        self.store += f"store i8 {ord(rightMostNode.node.getRuleName())}, i8* %{self.varNumbers}, align 1" + '\n'
                elif child.children[0].children[0].node.getRuleName() == "const":  # if var is const
                    if child.children[0].children[1].children[0].node.getRuleName() == "int":
                        self.register += f"%{self.varNumbers} = alloca i32, align 4" + '\n'
                        self.store += f"store i32 {rightMostNode.node.getRuleName()}, i8* %{self.varNumbers}, align 4" + '\n'
                    elif child.children[0].children[1].children[0].node.getRuleName() == "float":
                        self.register += f"%{self.varNumbers} = alloca float, align 4" + '\n'
                        self.store += f"store float {rightMostNode.node.getRuleName()}, i8* %{self.varNumbers}, align 4" + '\n'
                    elif child.children[0].children[1].children[0].node.getRuleName() == "char":
                        self.register += f"%{self.varNumbers} = alloca i8, align 1" + '\n'
                    if (len(rightMostNode.node.getRuleName()) > 1):
                        self.store += f"store i8 {ord(rightMostNode.node.getRuleName()[1])}, i8* %{self.varNumbers}, align 1" + '\n'
                    else:
                        self.store += f"store i8 {ord(rightMostNode.node.getRuleName())}, i8* %{self.varNumbers}, align 1" + '\n'
                elif child.children[0].node.getRuleName() == "pointerWord":  # if var is pointer
                    self.register += f"%{self.varNumbers} = alloca i8*, align 8" + '\n'
                    self.smallTable[f"%{self.varNumbers}"] = "i8*"
                    # nameIdentifier = get_rightmost_node(child.parent)
                    # valueOtherPointer = self.findValue(nameIdentifier.node.getRuleName(), self)
                    # if valueOtherPointer in self.store:
                    #     print("ye boi")
                    # self.store += f"store i8* %3, i8* %{self.varNumbers}, align 8" + '\n'
            elif child.node.getRuleName() == "returnStatement":
                self.isReturn = True
                if child.children[1].node.getRuleName() == "int":
                    self.returnStatement = f"ret i32 {child.children[1].children[0].node.getRuleName()}"
                elif child.children[1].node.getRuleName() == "float":
                    self.returnStatement = f"ret float {child.children[1].children[0].node.getRuleName()}"
                elif child.children[1].node.getRuleName() == "char":
                    self.returnStatement = f"ret i8 {child.children[1].children[0].node.getRuleName()}"
            elif child.node.getRuleName() == "scanFunction":
                self.varNumbers += 1
                self.declareFunctions += f"declare i32 @__isoc99_scanf(i8*, ...)" + '\n'
                strVar = ""
                scanArgs = ""
                tempLoads = ""
                usedRegister = 0
                for arguments in child.children[0].children:
                    if arguments.node.getRuleName() == "string":
                        strVar = arguments.children[0].node.getRuleName()
                        getString = self.strDict[strVar][0]
                        getBound = self.strDict[strVar][1]
                        scanArgs += f"i8* getelementptr inbounds({getBound}, {getBound}* {getString}, i64 0, i64 0), "
                    elif arguments.node.getRuleName() == "referenceID":
                        usedRegister += 1
                        scanArgs += f"i32* %{usedRegister}, "
                        tempLoads += f"%{self.varNumbers + usedRegister} = load i32, i32* %{usedRegister}, align 4" + '\n'
                        self.loaded[f"%{self.varNumbers + usedRegister}"] = ["i32", f"%{usedRegister}"]
                scanArgs = scanArgs[:-2]
                self.register += f"%{self.varNumbers} = call i32(i8*, ...) @__isoc99_scanf({scanArgs})" + '\n'
                self.register += tempLoads
                self.varNumbers += usedRegister

            elif child.node.getRuleName() == "printFunction":
                ofcDone = False
                if self.declareFunctions == "":
                    self.declareFunctions += f"declare i32 @printf(i8*, ...)" + '\n'
                if child.children[0].node.getRuleName() == "printArg":  # printFunction has arguments
                    printArgumenten = ""
                    notstr = False
                    for argument in child.children[0].children:
                        if argument.node.getRuleName() == "string":  # IS A STRING
                            getString = self.strDict[argument.children[0].node.getRuleName()][0]
                            getBound = self.strDict[argument.children[0].node.getRuleName()][1]
                            printArgumenten += f"i8* getelementptr inbounds({getBound}, {getBound}* {getString}, i64 0, i64 0), "
                        elif argument.node.getRuleName() == "opAddOrSub" or argument.node.getRuleName() == "opMultOrDiv":  # IS NOT A STRING
                            notstr = True
                            typeTEMP = argument.parent.children[0].children[0].node.getRuleName()  # %d or %f
                            value = argument.children[0].node.getRuleName()
                            valueString = ""
                            self.varNumbers += 1
                            if typeTEMP == "%d; ":
                                value = int(value[:2])
                            elif typeTEMP == "%f; ":
                                value = float(value)
                            if isinstance(value, int):
                                valueString = f"i32 {value}"
                            elif isinstance(value, float):
                                valueString = f"double {value}"
                            self.register += f"%{self.varNumbers} = call i32(i8*, ...) @printf(i8* getelementptr inbounds ({getBound}, {getBound}* {getString}, i64 0, i64 0), {valueString})" + '\n'
                        elif argument.node.getRuleName() == "int":
                            printArgumenten += f"i32 {argument.children[0].node.getRuleName()}, "
                        elif argument.node.getRuleName() == "float":
                            printArgumenten += f"double {argument.children[0].node.getRuleName()}, "
                        elif argument.node.getRuleName() == "char":
                            printArgumenten += f"i32 {ord(argument.children[0].node.getRuleName()[1])}, "
                        elif argument.node.getRuleName() == "nameIdentifier":  # NAMEIDENTIFIER
                            if (len(argument.children) > 1):
                                if argument.children[1].node.getRuleName() == "nameIdentifier":
                                    if argument.children[1].children[1].node.getRuleName() == "int":
                                        printArgumenten += f"i32 {argument.children[1].children[1].children[0].node.getRuleName()}, "
                                    elif argument.children[1].children[1].node.getRuleName() == "float":
                                        printArgumenten += f"double {argument.children[1].children[1].children[0].node.getRuleName()}, "
                                    elif argument.children[1].children[1].node.getRuleName() == "char":
                                        printArgumenten += f"i32 {ord(argument.children[1].children[1].children[0].node.getRuleName()[1])}, "
                                else:
                                    if (argument.children[1].node.getRuleName() == "int"):
                                        printArgumenten += f"i32 {argument.children[1].children[0].node.getRuleName()}, "
                                    elif (argument.children[1].node.getRuleName() == "float"):
                                        printArgumenten += f"double {argument.children[1].children[0].node.getRuleName()}, "
                                    elif (argument.children[1].node.getRuleName() == "char"):
                                        printArgumenten += f"i32 {ord(argument.children[1].children[0].node.getRuleName()[1])}, "
                                    elif (argument.children[1].node.getRuleName() == "opMultOrDiv"):
                                        printArgumenten += f"i32 {argument.children[1].children[0].node.getRuleName()}, "
                            else:
                                tempvalue = argument.children[0].node.getRuleName()
                                newValue = None
                                found33 = False
                                for i in self.table.values():
                                    for j in i.keys():
                                        if j == tempvalue:
                                            newValue = i[j][2]
                                if isinstance(newValue, int):
                                    printArgumenten += f"i32 {newValue}, "
                                    found33 = True
                                elif isinstance(newValue, float):
                                    printArgumenten += f"double {newValue}, "
                                    found33 = True
                                elif isinstance(newValue, str):
                                    printArgumenten += f"i32 {ord(newValue)}, "
                                    found33 = True
                                if found33 is False and ofcDone is False:
                                    ofcDone = True
                                    for i in self.loaded.keys():
                                        printArgumenten += f"i32 {i}, "

                        elif argument.node.getRuleName() == "arrCall":
                            arrName = argument.children[0].children[0].node.getRuleName()
                            arrPos = argument.children[2].children[0].node.getRuleName()

                            def findValue(ast, aName, aPos):
                                for child in ast.children:
                                    if child.node.getRuleName() == "arrAssign":
                                        if child.children[0].node.getRuleName() == aName and child.children[2].children[
                                            0].node.getRuleName() == aPos:
                                            return child.children[5].children[0].node.getRuleName()
                                    found = findValue(child, aName, aPos)
                                    if found is not None:
                                        return found
                                return None

                            newValue = findValue(self, arrName, arrPos)
                            if isinstance(newValue, int):
                                printArgumenten += f"i32 {newValue}, "
                            elif isinstance(newValue, float):
                                printArgumenten += f"double {newValue}, "
                            elif isinstance(newValue, str):
                                try:
                                    newValue = int(newValue)
                                    printArgumenten += f"i32 {newValue}, "
                                except ValueError:
                                    print("it's not an int dummy")
                        elif argument.node.getRuleName() == "referenceID":  ##fix pointers in print
                            namePtr = argument.children[1].children[0].node.getRuleName()
                            for i in self.table.values():
                                for j in i.keys():
                                    if j == namePtr:
                                        newValue = i[j][2]
                                        while isinstance(newValue, str):
                                            for k in i.keys():
                                                if k == newValue:
                                                    newValue = i[k][2]
                            if isinstance(newValue, int):
                                printArgumenten += f"i32 {newValue}, "
                            elif isinstance(newValue, float):
                                printArgumenten += f"double {newValue}, "
                            elif isinstance(newValue, str):
                                try:
                                    newValue = int(newValue)
                                    printArgumenten += f"i32 {newValue}, "
                                except ValueError:
                                    print("it's not an int dummy")

                        elif argument.node.getRuleName() == "opOr" or argument.node.getRuleName() == "opAnd" or argument.node.getRuleName() == "opUnary" or argument.node.getRuleName() == "opCompare":
                            printArgumenten += f"i32 {argument.children[0].node.getRuleName()}, "

                    printArgumenten = printArgumenten[:-2]  # remove last 2 chars
                    if notstr is False:
                        self.varNumbers += 1
                        self.registerDone = False
                        self.register += f"%{self.varNumbers} = call i32(i8*, ...) @printf({printArgumenten})" + '\n'
                else:  # if printFunction has NO arguments
                    getString = self.strDict[child.children[0].children[0].node.getRuleName()][0]
                    getBound = self.strDict[child.children[0].children[0].node.getRuleName()][1]
                    self.varNumbers += 1
                    if child.children[0].node.getRuleName() == "string":
                        self.register += f"%{self.varNumbers} = call i32(i8*, ...) @printf(i8* getelementptr inbounds ({getBound}, {getBound}* {getString}, i64 0, i64 0))" + '\n'
            # elif child.node.getRuleName() == "conditionStatement":
            #     if len(child.children) > 0:#not dead if
            #         self.varNumbers += 1

            elif child.node.getRuleName() == "whileStatement":
                self.varNumbers += 1
                self.register += f"br{self.varNumbers} label %{self.varNumbers}" + '\n'
                self.register += f"{self.varNumbers}:" + "\n"

                # self.parse_while(child)
            self.parse_expr(child)

    # def parse_while(self, ast):
    #     for child in ast.children:
    #         self.parse_while(child)

    def get_unnamed(self, ast):
        for child in ast.children:
            if child.node.getRuleName() == "printFunction" or child.node.getRuleName() == "scanFunction":
                if len(child.children[0].children[0].children) > 0:
                    for argument in child.children[0].children:
                        if argument.node.getRuleName() == "string":
                            if argument.children[0].node.getRuleName() not in self.doneFormats:
                                self.varNumbersPrint += 1
                                tempLength = len(argument.children[0].node.getRuleName())
                                if (argument.children[0].node.getRuleName() == "%s %s!\\n"):
                                    tempLength = len(argument.children[0].node.getRuleName())
                                elif argument.children[0].node.getRuleName() == "Enter two numbers:":
                                    tempLength = 19
                                elif (argument.children[0].node.getRuleName() == "%d\\n"):
                                    tempLength = 4
                                else:
                                    tempLength += 1

                                my_string = argument.children[0].node.getRuleName()

                                if "\\n" in my_string:
                                    my_string = my_string.replace("\\n", "\\0A")
                                if self.varNumbersPrint == 1:
                                    self.printFunction += f"@.str = private unnamed_addr constant [{tempLength} x i8] c\"{my_string}\\00\", align 1" + '\n'
                                elif self.varNumbersPrint > 1:
                                    self.printFunction += f"@.str.{self.varNumbersPrint} = private unnamed_addr constant [{tempLength} x i8] c\"{my_string}\\00\", align 1" + '\n'
                                if self.varNumbersPrint == 1:
                                    self.strDict[argument.children[0].node.getRuleName()] = [f"@.str",
                                                                                             f"[{tempLength} x i8]"]
                                else:
                                    self.strDict[argument.children[0].node.getRuleName()] = [
                                        f"@.str.{self.varNumbersPrint}", f"[{tempLength} x i8]"]
                                self.doneFormats.append(argument.children[0].node.getRuleName())
                else:
                    if child.children[0].children[0].node.getRuleName() not in self.doneFormats:
                        self.varNumbersPrint += 1
                        tempLength = len(child.children[0].children[0].node.getRuleName())
                        my_string = child.children[0].children[0].node.getRuleName()
                        if (my_string == "Enter two numbers:"):
                            tempLength += 1
                        elif (my_string == "Enter a 5-character string:"):
                            tempLength = 28
                        elif (my_string == "Something went wrong"):
                            tempLength = 21
                        if "\\n" in my_string:

                            my_string = my_string.replace("\\n", "\\0A")
                        if self.varNumbersPrint == 1:
                            self.printFunction += f"@.str = private unnamed_addr constant [{tempLength} x i8] c\"{my_string}\\00\", align 1" + '\n'
                        elif self.varNumbersPrint > 1:
                            self.printFunction += f"@.str.{self.varNumbersPrint} = private unnamed_addr constant [{tempLength} x i8] c\"{child.children[0].children[0].node.getRuleName()}\\00\", align 1" + '\n'
                        if self.varNumbersPrint == 1:
                            self.strDict[child.children[0].children[0].node.getRuleName()] = [f"@.str",
                                                                                              f"[{tempLength} x i8]"]
                        else:
                            self.strDict[child.children[0].children[0].node.getRuleName()] = [
                                f"@.str.{self.varNumbersPrint}", f"[{tempLength} x i8]"]
                        self.doneFormats.append(child.children[0].children[0].node.getRuleName())
            self.get_unnamed(child)

    def print_ll(self, argv):
        argv += ".ll"
        file = open(argv, "w")
        file.write(self.LLVM)

    def addNodes(self):
        string = str(self)
        if len(self.node.getRuleName()) > 1:
            if self.parent is not None:
                if self.parent.node.getRuleName() == "string":
                    a = self.node.getRuleName()
                    newStr = a[1:len(a) - 1]
                    self.node.ruleName = newStr
                elif self.parent.node.getRuleName() == "comment":
                    a = self.node.getRuleName()
                    b = a.translate({ord("\""): None})
                    self.node.ruleName = b
        string += '[label="{}"] \n'.format(self.node.getRuleName())
        for child in self.children:
            string += child.addNodes()
        return string

    def addConnections(self):
        string = ""
        for child in self.children:
            string += str(self) + " -- " + str(child) + "\n" + child.addConnections()
        return string

    def printInDot(self, argv):
        graph = "graph ast { \n" + self.addNodes() + self.addConnections() + "}"
        argv += ".ast.dot"
        file = open(argv, "w")
        file.write(graph)

    def removeDeadCode(self):
        if self.node.getRuleName() == "returnStatement" or self.node.getRuleName() == "break" or self.node.getRuleName() == "continue":
            for i in self.parent.children:
                if i != self:
                    self.parent.children.remove(i)
        elif self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement" or self.node.getRuleName()[:14] == "whileStatement":
            if len(self.children[0].children) == 1:
                if self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement":
                    if len(self.children[0].children) == 1:
                        if self.children[0].children[0].node.getRuleName() == "1":
                            temp = self
                            arr = []
                            for i in self.parent.children:
                                if i != temp:
                                    arr.append(i)
                            for i in arr:
                                self.parent.children.remove(i)
            for i in self.children:
                i.removeDeadCode()

        elif self.node.getRuleName()[:13] == "elseStatement":
            temp = self
            arr = []
            for i in self.parent.children:
                if i != temp:
                    arr.append(i)
            for i in arr:
                if len(i.children[0].children) == 1:
                    self.parent.children.remove(i)
            for i in self.children:
                i.removeDeadCode()
        else:
            for i in self.children:
                i.removeDeadCode()

    def optimize(self, dict):
        if self.node.getRuleName() == "prog" or self.node.getRuleName() == "expr" or self.node.getRuleName() == "conditionStatement" or self.node.getRuleName() == "printFunction" or self.node.getRuleName() == "argumentCall" or self.node.getRuleName() == "arrArg":
            if (self.node.getRuleName() == "printFunction" or self.node.getRuleName() == "scanFunction") and len(
                    self.children) == 2:
                self.children.pop(0)
            for i in self.children:
                i.optimize(dict)
        elif len(self.children) == 1:
            found = False
            temp = self
            while not found:
                temp = temp.children[0]
                if len(temp.children) >= 2:
                    temp.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp
                    for i in temp.children:
                        i.optimize(dict)
                    found = True
                elif len(temp.children) == 0:
                    temp.parent.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp.parent
                    found = True
                elif temp.node.getRuleName() == "expr":
                    temp.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp
                    for i in temp.children:
                        i.optimize(dict)
                    found = True
        elif len(self.children) >= 2:
            if self.node.getRuleName()[:14] == "whileStatement":
                if len(self.children) == 5:
                    self.children.pop(0)
                dict["whileStatement"] += 1
                if dict["whileStatement"] != 1:
                    self.node.ruleName = "whileStatement" + str(dict["whileStatement"])

            elif (self.node.getRuleName() == "printFunction" or self.node.getRuleName() == "scanFunction") and len(
                    self.children) == 2:
                self.children.pop(0)
            elif self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[
                                                                  :13] == "elifStatement" or self.node.getRuleName()[
                                                                                             :13] == "elseStatement":
                if self.node.getRuleName()[:13] == "elifStatement":
                    self.children.pop(0)
                    self.children.pop(0)
                    dict["elifStatement"] += 1
                    if dict["elifStatement"] != 1:
                        self.node.ruleName = "elifStatement" + str(dict["elifStatement"])
                elif self.node.getRuleName()[:11] == "ifStatement":
                    self.children.pop(0)
                    dict["ifStatement"] += 1
                    if dict["ifStatement"] != 1:
                        self.node.ruleName = "ifStatement" + str(dict["ifStatement"])
                elif self.node.getRuleName()[:13] == "elseStatement":
                    self.children.pop(0)
                    dict["elseStatement"] += 1
                    if dict["elseStatement"] != 1:
                        self.node.ruleName = "elseStatement" + str(dict["elseStatement"])
            elif self.node.getRuleName()[:12] == "unNamedScope":
                dict["unNamedScope"] += 1
                if dict["unNamedScope"] != 1:
                    self.node.ruleName = "unNamedScope" + str(dict["unNamedScope"])
            elif self.node.getRuleName()[:7] == "forLoop":
                self.children.pop(0)
                dict["forLoop"] += 1
                if dict["forLoop"] != 1:
                    self.node.ruleName = "forLoop" + str(dict["forLoop"])
            elif self.node.getRuleName() == "arrDef":
                for i in self.children:
                    if i.node.getRuleName() == "arrArg":
                        if len(i.children) > 1:
                            if i.children[0].node.getRuleName() == "{" and i.children[1].node.getRuleName() == "}":
                                i.node.ruleName = "int"
                                i.children[0].node.ruleName = 0
                                i.children.pop()
                            else:
                                i.children.pop(len(i.children) - 1)
                                i.children.pop(0)
            for i in self.children:
                i.optimize(dict)

    def convertToWhile(self):
        if len(self.children) == 4:
            if self.node.getRuleName()[:7] == "forLoop":
                self.node.ruleName = "whileStatement"
                temp = self.children[0]
                self.children[0].node.ruleName = "int"
                self.children[0].children.append(copy.deepcopy(temp))
                self.children[0].children[0].node.ruleName = 1
                self.children[0].children[0].parent = self.children[0]
                for i in self.children:
                    i.convertToWhile()
        elif self.node.getRuleName()[:7] == "forLoop":
            self.node.ruleName = "whileStatement"
            defenition = self.children[1]
            increment = self.children[3]
            body = self.children[5]
            found = False
            if len(body.children) == 1:
                body.children.append(copy.deepcopy(increment))
                body.children[1].parent = body
                body.children[1].children.clear()
                body.children[1].node.ruleName = "expr"
                body.children[1].children.append(copy.deepcopy(increment))
                body.children[1].children[0].parent = body.children[1]
            else:
                body = body.children[1]
                while not found:
                    if len(body.children) != 2:
                        body.children.append(copy.deepcopy(increment))
                        body.children[1].parent = body
                        body.children[1].children.clear()
                        body.children[1].node.ruleName = "expr"
                        body.children[1].children.append(copy.deepcopy(increment))
                        body.children[1].children[0].parent = body.children[1]
                        found = True
                    else:
                        body = body.children[1]

            self.children.pop(0)
            self.children.pop(0)
            self.children.pop(1)
            self.children.pop(1)
            self.children.pop(2)
            temp = self.parent.parent
            index = self.parent.parent.parent.children.index(self.parent.parent)
            self.parent.parent.parent.children[index] = copy.deepcopy(defenition)
            self.parent.parent.parent.children[index].node.ruleName = "expr"
            self.parent.parent.parent.children[index].parent = self.parent.parent.parent
            self.parent.parent.parent.children[index].children.clear()
            self.parent.parent.parent.children[index].children.append(copy.deepcopy(defenition))
            self.parent.parent.parent.children[index].children[0].parent = self.parent.parent.parent.children[index]
            self.parent.parent.parent.children[index].children.append(copy.deepcopy(temp))
            self.parent.parent.parent.children[index].children[1].parent = self.parent.parent.parent.children[index]
            for i in self.children:
                i.convertToWhile()
        else:
            for i in self.children:
                i.convertToWhile()

    def initialiseSymbolTable(self, symbolTable, scope):
        if self.node.getRuleName() == "variableDefinition":
            if self.children[0].children[0].node.getRuleName() == "pointerWord":
                varType = self.children[0].children[0].children[0].children[0].node.getRuleName()
                name = self.children[0].children[1].children[0].node.getRuleName()
                tableType = symbolTable.get_symbol(name, scope)[0]
            else:
                varType = self.children[0].children[0].children[0].node.getRuleName()
                name = self.children[0].children[1].children[0].node.getRuleName()
                tableType = symbolTable.get_symbol(name, scope)[0]
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[
                2].node.getRuleName() == "opMultOrDiv":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                if len(self.children[2].children) == 1:
                    value = None
                    if symbolTable.get_symbol(varName, scope)[0] == "int":
                        try:
                            value = int(self.children[2].children[0].node.getRuleName())
                        except ValueError:
                            value = float(self.children[2].children[0].node.getRuleName())
                            value = int(value)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        value = float(self.children[2].children[0].node.getRuleName())
                    else:
                        if self.children[2].children[0].node.getRuleName() == "int":
                            value = int(self.children[2].children[0].node.getRuleName())
                        elif self.children[2].children[0].node.getRuleName() == "float":
                            value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value, scope)
                else:
                    pass
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or \
                    self.children[2].node.getRuleName() == "char":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName, scope)[0]
                if self.children[2].node.getRuleName() == "char" and (type == "int" or type == "float"):
                    value = ord(self.children[2].children[0].node.getRuleName()[1])
                elif type == "int":
                    try:
                        value = int(self.children[2].children[0].node.getRuleName())
                    except ValueError:
                        value = float(self.children[2].children[0].node.getRuleName())
                        value = int(value)
                elif type == "float":
                    value = float(self.children[2].children[0].node.getRuleName())
                else:
                    if self.children[2].node.getRuleName() == "int":
                        value = int(self.children[2].children[0].node.getRuleName())
                    else:
                        value = self.children[2].children[0].node.getRuleName()[1]
                symbolTable.insert_value(varName, value, scope)
            elif self.children[2].node.getRuleName() == "opUnary":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName, scope)[0]
                const = symbolTable.get_symbol(varName, scope)[1][0]
                if const != "pointer" and const != "const pointer":
                    if type == "int":
                        value = int(self.children[2].children[0].node.getRuleName())
                    else:
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value, scope)
            elif self.children[2].node.getRuleName() == "nameIdentifier" and len(self.children[2].children) == 2:
                varName = self.children[2].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName, scope)[0]
                const = symbolTable.get_symbol(varName, scope)[1][0]
                if const != "pointer" and const != "const pointer":
                    if type == "int":
                        value = int(self.children[2].children[1].children[0].node.getRuleName())
                    elif type == "float":
                        value = float(self.children[2].children[1].children[0].node.getRuleName())
                    else:
                        value = self.children[2].children[1].children[0].node.getRuleName()[1]
                    symbolTable.insert_value(name, value, scope)


        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[
                2].node.getRuleName() == "opMultOrDiv" or self.children[2].node.getRuleName() == "opUnary" or \
                    self.children[2].node.getRuleName() == "opCompare" or self.children[
                2].node.getRuleName() == "opOr" or self.children[2].node.getRuleName() == "opAnd":
                varName = self.children[0].children[0].node.getRuleName()
                if self.children[2].node.getRuleName() == "opUnary":
                    type = symbolTable.get_symbol(varName)[0]
                    if type == "int":
                        value = int(self.children[2].children[0].node.getRuleName())
                    else:
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value, scope)

                elif len(self.children[2].children) == 1:
                    if symbolTable.get_symbol(varName, scope)[0] == "int":
                        try:
                            value = int(self.children[2].children[0].node.getRuleName())
                        except ValueError:
                            value = float(self.children[2].children[0].node.getRuleName())
                            value = int(value)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value, scope)
                else:
                    symbolTable.insert_symbol(varName, self.children[2], scope)
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or \
                    self.children[2].node.getRuleName() == "char":
                possible = True
                if self.children[0].node.getRuleName() == "referenceID":
                    possible = False
                    varName = self.children[0].children[1].children[0].node.getRuleName()
                else:
                    varName = self.children[0].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName, scope)[0]
                if self.children[2].node.getRuleName() == "char" and (type == "int" or type == "float"):
                    value = ord(self.children[2].children[0].node.getRuleName()[1])
                elif type == "int":
                    try:
                        value = int(self.children[2].children[0].node.getRuleName())
                    except ValueError:
                        value = float(self.children[2].children[0].node.getRuleName())
                        value = int(value)
                elif type == "float":
                    value = float(self.children[2].children[0].node.getRuleName())
                else:
                    value = self.children[2].children[0].node.getRuleName()[1]
                if possible:
                    symbolTable.insert_value(varName, value, scope)
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[
                                                               :11] == "ifStatement" or self.node.getRuleName()[
                                                                                        :13] == "elifStatement" or self.node.getRuleName()[
                                                                                                                   :13] == "elseStatement" or self.node.getRuleName()[
                                                                                                                                              :14] == "whileStatement" or self.node.getRuleName()[
                                                                                                                                                                          :7] == "forLoop":
            scope = self.node.getRuleName()
            for i in self.children:
                i.initialiseSymbolTable(symbolTable, scope)
        elif self.node.getRuleName() == "funcDefinition":
            scope = self.children[1].node.getRuleName()
            for i in self.children:
                i.initialiseSymbolTable(symbolTable, scope)
        elif self.node.getRuleName() == "}":
            if scope in symbolTable.scopes:
                if symbolTable.scopes[scope] == None or symbolTable.scopes[scope] == [None]:
                    scope = None
                else:
                    scope = symbolTable.scopes[scope][1]
            else:
                scope = None
            for i in self.children:
                i.initialiseSymbolTable(symbolTable, scope)
        else:
            for i in self.children:
                i.initialiseSymbolTable(symbolTable, scope)

    def constantPropagation(self, dict, arr, symbolTable, scope):
        if self.node.getRuleName() == "expr":
            for i in arr:
                if i in dict:
                    dict.pop(i)
            arr.clear()
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable, scope)
        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[0].node.getRuleName() == "nameIdentifier":
                varName = self.children[0].children[0].node.getRuleName()
            else:
                varName = self.children[0].children[1].children[0].node.getRuleName()
            if varName in dict:
                arr.append(varName)
            rightSide = self.children[2]
            rightSide.constantPropagation(dict, arr, symbolTable, scope)

        elif self.node.getRuleName() == "variableDefinition":
            rightSide = self.children[2]
            name = self.children[0].children[1].children[0].node.getRuleName()
            dict[name] = self.children[2]
            rightSide.constantPropagation(dict, arr, symbolTable, scope)
        elif self.node.getRuleName() == "nameIdentifier":
            tempName = self.children[0].node.getRuleName()
            found = False
            curr = self
            while not found:
                if curr.node.getRuleName()[:7] == "forLoop" or curr.node.getRuleName()[:14] == "whileStatement":
                    found = True
                elif curr.node.getRuleName() == "prog":
                    break
                else:
                    curr = curr.parent
            if not found:
                if tempName in dict and self.parent.node.getRuleName() != "variableDefinition" and self.parent.node.getRuleName() != "assignmentStatement" and self.parent.node.getRuleName() != "variableDeclaration":
                    if self.parent.node.getRuleName() == "printFunction":
                        varName = self.children[0].node.getRuleName()
                        self.parent.children[0].node.ruleName = symbolTable.get_symbol(varName, scope)[0]
                    test = False
                    if self.parent.node.getRuleName() == "referenceID":
                        if self.parent.children[0].node.getRuleName() == "&":
                            test = True
                    if not test:
                        if dict[tempName].node.getRuleName() != "referenceID":
                            self.children.append(copy.deepcopy(dict[tempName]))
                elif tempName in dict and (
                        self.parent.node.getRuleName() == "assignmentStatement" or self.parent.node.getRuleName() == "variableDefinition"):
                    self.children.append(copy.deepcopy(dict[tempName]))
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[
                                                               :11] == "ifStatement" or self.node.getRuleName()[
                                                                                        :13] == "elifStatement" or self.node.getRuleName()[
                                                                                                                   :13] == "elseStatement" or self.node.getRuleName()[
                                                                                                                                              :14] == "whileStatement" or self.node.getRuleName()[
                                                                                                                                                                          :7] == "forLoop":
            scope = self.node.getRuleName()
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable, scope)
        elif self.node.getRuleName() == "funcDefinition":
            scope = self.children[1].node.getRuleName()
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable, scope)
        elif self.node.getRuleName() == "}":
            if scope in symbolTable.scopes:
                if symbolTable.scopes[scope] == None or symbolTable.scopes[scope] == [None]:
                    scope = None
                else:
                    scope = symbolTable.scopes[scope][1]
            else:
                scope = None
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable, scope)
        else:
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable, scope)

    def constantFolding(self, symbolTable, scope):
        if self.node.getRuleName() == "opAddOrSub" or self.node.getRuleName() == "opMultOrDiv" or self.node.getRuleName() == "opCompare" or self.node.getRuleName() == "opAnd" or self.node.getRuleName() == "opOr":
            leftValue = self.children[0]
            rightValue = self.children[2]
            possible = True
            curr = self
            while possible:
                if curr.node.getRuleName()[:7] == "forLoop" or curr.node.getRuleName()[:14] == "whileStatement":
                    possible = False
                elif curr.node.getRuleName() == "expr":
                    break
                else:
                    curr = curr.parent
            if leftValue.node.getRuleName() == "int":
                leftValue = int(leftValue.children[0].node.getRuleName())
            elif leftValue.node.getRuleName() == "float":
                leftValue = float(leftValue.children[0].node.getRuleName())
            elif leftValue.node.getRuleName() == "char":
                leftValue = ord(leftValue.children[0].node.getRuleName()[1])
            elif leftValue.node.getRuleName() == "nameIdentifier" and len(leftValue.children) == 1:
                possible = False
            elif leftValue.node.getRuleName() == "nameIdentifier" and len(leftValue.children) == 2:
                leftValue = leftValue.children[1]
                leftValue.constantFolding(symbolTable, scope)
                if len(leftValue.children) == 1:
                    try:
                        leftValue = int(leftValue.children[0].node.getRuleName())
                    except ValueError:
                        try:
                            leftValue = float(leftValue.children[0].node.getRuleName())
                        except ValueError:
                            leftValue = ord(leftValue.children[0].node.getRuleName()[1])
                else:
                    possible = False

            else:
                leftValue.constantFolding(symbolTable, scope)
                if len(leftValue.children) == 1:
                    try:
                        leftValue = int(leftValue.children[0].node.getRuleName())
                    except ValueError:
                        try:
                            leftValue = float(leftValue.children[0].node.getRuleName())
                        except ValueError:
                            leftValue = ord(leftValue.children[0].node.getRuleName()[1])
                else:
                    possible = False

            if rightValue.node.getRuleName() == "int":
                rightValue = int(rightValue.children[0].node.getRuleName())
            elif rightValue.node.getRuleName() == "float":
                rightValue = float(rightValue.children[0].node.getRuleName())
            elif rightValue.node.getRuleName() == "char":
                rightValue = ord(rightValue.children[0].node.getRuleName()[1])
            elif rightValue.node.getRuleName() == "nameIdentifier" and len(rightValue.children) == 1:
                possible = False
            elif rightValue.node.getRuleName() == "nameIdentifier" and len(rightValue.children) == 2:
                rightValue = rightValue.children[1]
                rightValue.constantFolding(symbolTable, scope)
                if len(rightValue.children) == 1:
                    try:
                        rightValue = int(rightValue.children[0].node.getRuleName())
                    except ValueError:
                        try:
                            rightValue = float(rightValue.children[0].node.getRuleName())
                        except ValueError:
                            rightValue = ord(rightValue.children[0].node.getRuleName()[1])
                else:
                    possible = False
            else:
                rightValue.constantFolding(symbolTable, scope)
                if len(rightValue.children) == 1:
                    try:
                        rightValue = int(rightValue.children[0].node.getRuleName())
                    except ValueError:
                        try:
                            rightValue = float(rightValue.children[0].node.getRuleName())
                        except ValueError:
                            rightValue = ord(rightValue.children[0].node.getRuleName()[1])
                else:
                    possible = False

            if possible:
                varName = self.parent
                found = False
                type = None
                while not found:
                    if varName.node.getRuleName() == "variableDefinition":
                        varName = varName.children[0].children[1].children[0].node.getRuleName()
                        found = True
                    elif varName.node.getRuleName() == "assignmentStatement":
                        varName = varName.children[0].children[0].node.getRuleName()
                        found = True
                    elif varName.node.getRuleName() == "printArg":
                        varName = "print"
                        found = True
                    else:
                        varName = varName.parent
                        if varName == None:
                            break
                if varName != "print":
                    find = False
                    curr = self.parent
                    name = None
                    while not find:
                        if curr.node.getRuleName() == "variableDefinition" or curr.node.getRuleName() == "assignmentStatement":
                            break
                        elif curr.node.getRuleName() == "nameIdentifier":
                            name = curr.children[0].node.getRuleName()
                            find = True
                        else:
                            if curr.parent == None:
                                break
                            curr = curr.parent
                    if find:
                        type = symbolTable.get_symbol(name, scope)[0]
                    else:
                        if varName != None:
                            type = symbolTable.get_symbol(varName, scope)[0]
                if self.children[1].node.getRuleName() == "+":
                    if type == None:
                        self.children[0].node.ruleName = leftValue + rightValue
                    elif type == "int":
                        self.children[0].node.ruleName = int(leftValue + rightValue)
                    elif type == "float":
                        self.children[0].node.ruleName = float(leftValue + rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue + rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "-":
                    if type == None:
                        self.children[0].node.ruleName = leftValue - rightValue
                    elif type == "int":
                        self.children[0].node.ruleName = int(leftValue - rightValue)
                    elif type == "float":
                        self.children[0].node.ruleName = float(leftValue - rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue - rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "*":
                    if type == None:
                        self.children[0].node.ruleName = leftValue * rightValue
                    elif type == "int":
                        self.children[0].node.ruleName = int(leftValue * rightValue)
                    elif type == "float":
                        self.children[0].node.ruleName = float(leftValue * rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue * rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "/":
                    if type == None:
                        self.children[0].node.ruleName = leftValue / rightValue
                    elif type == "int":
                        self.children[0].node.ruleName = int(leftValue / rightValue)
                    elif type == "float":
                        self.children[0].node.ruleName = float(leftValue / rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue / rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "%":
                    if type == None:
                        self.children[0].node.ruleName = leftValue % rightValue
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue % rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue % rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue % rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "<":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == ">":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "==":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "<=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == ">=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "!=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "&&":
                    if leftValue > 0:
                        leftValue = 1
                    if rightValue > 0:
                        rightValue = 1
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "||":
                    if leftValue > 0:
                        leftValue = 1
                    if rightValue > 0:
                        rightValue = 1
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    elif varName == "print":
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    elif symbolTable.get_symbol(varName, scope)[0] == "float":
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                        temp = symbolTable.get_symbol(varName, scope)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[scope][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()


        elif self.node.getRuleName() == "opUnary":
            value = self.children[1]
            possible = True
            if value.node.getRuleName() == "int":
                value = int(value.children[0].node.getRuleName())
            elif value.node.getRuleName() == "float":
                value = float(value.children[0].node.getRuleName())
            elif value.node.getRuleName() == "char":
                possible = False
            elif value.node.getRuleName() == "nameIdentifier":
                name = value.children[0].node.getRuleName()
                value = symbolTable.get_symbol(name, scope)[2]
                if value != 0 and value != 1:
                    possible = False
            else:
                value.constantFolding(symbolTable, scope)
                if len(value.children) == 1:
                    try:
                        value = int(value.children[0].node.getRuleName())
                    except ValueError:
                        value = float(value.children[0].node.getRuleName())
                else:
                    possible = False
            if possible:
                if self.children[0].node.getRuleName() == "-":
                    self.children[0].node.ruleName = -value
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[0].node.getRuleName() == "+":
                    self.children[0].node.ruleName = +value
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[0].node.getRuleName() == "!":
                    if value > 0:
                        value = 1
                    if value == 0:
                        self.children[0].node.ruleName = 1
                    else:
                        self.children[0].node.ruleName = 0
                    self.children.pop()
                    self.children[0].children.clear()
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[
                                                               :11] == "ifStatement" or self.node.getRuleName()[
                                                                                        :13] == "elifStatement" or self.node.getRuleName()[
                                                                                                                   :13] == "elseStatement" or self.node.getRuleName()[
                                                                                                                                              :14] == "whileStatement" or self.node.getRuleName()[
                                                                                                                                                                          :7] == "forLoop":
            scope = self.node.getRuleName()
            for i in self.children:
                i.constantFolding(symbolTable, scope)
        elif self.node.getRuleName() == "funcDefinition":
            scope = self.children[1].node.getRuleName()
            for i in self.children:
                i.constantFolding(symbolTable, scope)
        elif self.node.getRuleName() == "}":
            if scope in symbolTable.scopes:
                if symbolTable.scopes[scope] == None or symbolTable.scopes[scope] == [None]:
                    scope = None
                else:
                    scope = symbolTable.scopes[scope][1]
            else:
                scope = None
            for i in self.children:
                i.constantFolding(symbolTable, scope)
        else:
            for i in self.children:
                i.constantFolding(symbolTable, scope)


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
