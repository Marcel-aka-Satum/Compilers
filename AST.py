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
        else: self.ruleName = syntaxTree.getText()

    def getRuleName(self): return str(self.ruleName)

    def getLine(self): return self.line

    def getCollom(self): return self.collom
class AST:
    def __init__(self, syntaxTree):
        self.parent = None
        self.children = list()
        self.node = Node(syntaxTree)

        if syntaxTree.getChildCount() == 0 : return
        newChild = ParserRuleContext()
        for newChild in syntaxTree.getChildren():
            temp = AST(newChild)
            temp.parent = self
            if temp.node.getRuleName() != "(" and temp.node.getRuleName() != ")" and temp.node.getRuleName() != ";" and temp.node.getRuleName() != "":
                self.children.append(temp)

    def addNodes(self):
        string = str(self)
        if len(self.node.getRuleName()) > 1:
            if self.parent is not None:
                if self.parent.node.getRuleName() == "string":
                    a = self.node.getRuleName()
                    newStr = a[1:len(a)-1]
                    self.node.ruleName = newStr
                elif self.parent.node.getRuleName() == "comment":
                    a = self.node.getRuleName()
                    b = a.translate({ord("\"") : None})
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
                if self.children[0].children[0].node.getRuleName() == "0":
                    self.parent.children.remove(self)
        else:
            for i in self.children:
                i.removeDeadCode()
    def optimize(self, dict):
        if self.node.getRuleName() == "prog" or self.node.getRuleName() == "expr" or self.node.getRuleName() == "conditionStatement" or self.node.getRuleName() == "printFunction" or self.node.getRuleName() == "argumentCall" or self.node.getRuleName() == "arrArg":
            if self.node.getRuleName() == "printFunction" and len(self.children) == 2:
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

            elif self.node.getRuleName() == "printFunction" and len(self.children) == 2:
                self.children.pop(0)
            elif self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement" or self.node.getRuleName()[:13] == "elseStatement":
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
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[2].node.getRuleName() == "opMultOrDiv":
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
                    symbolTable.insert_symbol(varName, self.children[2], scope)
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or self.children[2].node.getRuleName() == "char":
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
                    else:
                        value = float(self.children[2].children[1].children[0].node.getRuleName())
                    symbolTable.insert_value(name, value, scope)


        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[2].node.getRuleName() == "opMultOrDiv" or self.children[2].node.getRuleName() == "opUnary" or self.children[2].node.getRuleName() == "opCompare" or self.children[2].node.getRuleName() == "opOr" or self.children[2].node.getRuleName() == "opAnd":
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
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or self.children[2].node.getRuleName() == "char":
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
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement" or self.node.getRuleName()[:13] == "elseStatement" or self.node.getRuleName()[:14] == "whileStatement" or self.node.getRuleName()[:7] == "forLoop":
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



    def constantPropagation(self, dict, arr,  symbolTable, scope):
        if self.node.getRuleName() == "expr":
            for i in arr:
                if i in dict:
                    dict.pop(i)
            arr.clear()
            for i in self.children:
                i.constantPropagation(dict,arr, symbolTable, scope)
        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[0].node.getRuleName() == "nameIdentifier":
                varName = self.children[0].children[0].node.getRuleName()
            else:
                varName = self.children[0].children[1].children[0].node.getRuleName()
            if varName in dict:
                arr.append(varName)
            rightSide = self.children[2]
            rightSide.constantPropagation(dict, arr,  symbolTable, scope)

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
                        self.children.append(copy.deepcopy(dict[tempName]))
                elif tempName in dict and (self.parent.node.getRuleName() == "assignmentStatement" or self.parent.node.getRuleName() == "variableDefinition"):
                    self.children.append(copy.deepcopy(dict[tempName]))
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement" or self.node.getRuleName()[:13] == "elseStatement" or self.node.getRuleName()[:14] == "whileStatement" or self.node.getRuleName()[:7] == "forLoop":
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
                leftValue.constantFolding(symbolTable,scope)
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
                rightValue.constantFolding(symbolTable,scope)
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
                rightValue.constantFolding(symbolTable,scope)
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
                value.constantFolding(symbolTable,scope)
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
        elif self.node.getRuleName()[:12] == "unNamedScope" or self.node.getRuleName()[:11] == "ifStatement" or self.node.getRuleName()[:13] == "elifStatement" or self.node.getRuleName()[:13] == "elseStatement" or self.node.getRuleName()[:14] == "whileStatement" or self.node.getRuleName()[:7] == "forLoop":
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