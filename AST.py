from antlr4 import *
from MyGrammarParser import MyGrammarParser
import copy

class Node:
    def __init__(self, syntaxTree):
        if syntaxTree.getChildCount() > 0:
            self.ruleName = MyGrammarParser.ruleNames[syntaxTree.getRuleIndex()]
        else: self.ruleName = syntaxTree.getText()

    def getRuleName(self): return str(self.ruleName)

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
            if temp.node.getRuleName() != "(" and temp.node.getRuleName() != ")" and temp.node.getRuleName() != ";":
                self.children.append(temp)

    def addNodes(self):
        string = str(self)
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

    def optimize(self):
        if self.node.getRuleName() == "prog" or self.node.getRuleName() == "expr":
            for i in self.children:
                i.optimize()
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
                        i.optimize()
                    found = True
                elif len(temp.children) == 0:
                    temp.parent.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp.parent
                    found = True
        elif len(self.children) >= 2:
            for i in self.children:
                i.optimize()

    def initialiseSymbolTable(self, symbolTable):
        if self.node.getRuleName() == "variableDefinition":
            if self.children[0].children[0].node.getRuleName() == "pointerWord":
                varType = self.children[0].children[0].children[0].children[0].node.getRuleName()
                name = self.children[0].children[1].children[0].node.getRuleName()
                tableType = symbolTable.get_symbol(name)[0]
                if varType == "char" and tableType == "int":
                    self.children[0].children[0].children[0].children[0].node.ruleName = "int"
            else:
                varType = self.children[0].children[0].children[0].node.getRuleName()
                name = self.children[0].children[1].children[0].node.getRuleName()
                tableType = symbolTable.get_symbol(name)[0]
                if varType == "char" and tableType == "int":
                    self.children[0].children[0].children[0].node.ruleName = "int"
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[2].node.getRuleName() == "opMultOrDiv":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                if len(self.children[2].children) == 1:
                    value = None
                    if symbolTable.get_symbol(varName)[0] == "int":
                        try:
                            value = int(self.children[2].children[0].node.getRuleName())
                        except ValueError:
                            value = float(self.children[2].children[0].node.getRuleName())
                            value = int(value)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        value = float(self.children[2].children[0].node.getRuleName())
                    else:
                        if self.children[2].children[0].node.getRuleName() == "int":
                            value = int(self.children[2].children[0].node.getRuleName())
                        elif self.children[2].children[0].node.getRuleName() == "float":
                            value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value)
                else:
                    symbolTable.insert_symbol(varName, self.children[2])
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or self.children[2].node.getRuleName() == "char":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName)[0]
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
                symbolTable.insert_value(varName, value)
            elif self.children[2].node.getRuleName() == "opUnary":
                varName = self.children[0].children[1].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName)[0]
                const = symbolTable.get_symbol(varName)[1][0]
                if const != "pointer" and const != "const pointer":
                    if type == "int":
                        value = int(self.children[2].children[0].node.getRuleName())
                    else:
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value)
            elif self.children[2].node.getRuleName() == "nameIdentifier" and len(self.children[2].children) == 2:
                varName = self.children[2].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName)[0]
                const = symbolTable.get_symbol(varName)[1][0]
                if const != "pointer" and const != "const pointer":
                    if type == "int":
                        value = int(self.children[2].children[1].children[0].node.getRuleName())
                    else:
                        value = float(self.children[2].children[1].children[0].node.getRuleName())
                    symbolTable.insert_value(name, value)


        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[2].node.getRuleName() == "opAddOrSub" or self.children[2].node.getRuleName() == "opMultOrDiv" or self.children[2].node.getRuleName() == "opUnary" or self.children[2].node.getRuleName() == "opCompare" or self.children[2].node.getRuleName() == "opOr" or self.children[2].node.getRuleName() == "opAnd":
                varName = self.children[0].children[0].node.getRuleName()
                if self.children[2].node.getRuleName() == "opUnary":
                    type = symbolTable.get_symbol(varName)[0]
                    if type == "int":
                        value = int(self.children[2].children[0].node.getRuleName())
                    else:
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value)

                elif len(self.children[2].children) == 1:
                    if symbolTable.get_symbol(varName)[0] == "int":
                        try:
                            value = int(self.children[2].children[0].node.getRuleName())
                        except ValueError:
                            value = float(self.children[2].children[0].node.getRuleName())
                            value = int(value)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        value = float(self.children[2].children[0].node.getRuleName())
                    symbolTable.insert_value(varName, value)
                else:
                    symbolTable.insert_symbol(varName, self.children[2])
            elif self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float" or self.children[2].node.getRuleName() == "char":
                possible = True
                if self.children[0].node.getRuleName() == "referenceID":
                    possible = False
                    varName = self.children[0].children[1].children[0].node.getRuleName()
                else:
                    varName = self.children[0].children[0].node.getRuleName()
                type = symbolTable.get_symbol(varName)[0]
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
                    symbolTable.insert_value(varName, value)

        else:
            for i in self.children:
                i.initialiseSymbolTable(symbolTable)



    def constantPropagation(self, dict, arr,  symbolTable):
        if self.node.getRuleName() == "expr":
            for i in arr:
                if i in dict:
                    dict.pop(i)
            arr.clear()
            for i in self.children:
                i.constantPropagation(dict,arr, symbolTable)
        elif self.node.getRuleName() == "assignmentStatement":
            if self.children[0].node.getRuleName() == "nameIdentifier":
                varName = self.children[0].children[0].node.getRuleName()
            else:
                varName = self.children[0].children[1].children[0].node.getRuleName()
            if varName in dict:
                arr.append(varName)
            rightSide = self.children[2]
            rightSide.constantPropagation(dict, arr,  symbolTable)

        elif self.node.getRuleName() == "variableDefinition":
            rightSide = self.children[2]
            name = self.children[0].children[1].children[0].node.getRuleName()
            dict[name] = self.children[2]
            rightSide.constantPropagation(dict, arr, symbolTable)
        elif self.node.getRuleName() == "nameIdentifier":
            tempName = self.children[0].node.getRuleName()
            if tempName in dict and self.parent.node.getRuleName() != "variableDefinition" and self.parent.node.getRuleName() != "assignmentStatement" and self.parent.node.getRuleName() != "variableDeclaration":
                if self.parent.node.getRuleName() == "printFunction":
                    varName = self.children[0].node.getRuleName()
                    self.parent.children[0].node.ruleName = symbolTable.get_symbol(varName)[0]
                self.children.append(copy.deepcopy(dict[tempName]))
            elif tempName in dict and (self.parent.node.getRuleName() == "assignmentStatement" or self.parent.node.getRuleName() == "variableDefinition"):
                self.children.append(copy.deepcopy(dict[tempName]))

        else:
            for i in self.children:
                i.constantPropagation(dict, arr, symbolTable)


    def constantFolding(self, symbolTable):
        if self.node.getRuleName() == "opAddOrSub" or self.node.getRuleName() == "opMultOrDiv" or self.node.getRuleName() == "opCompare" or self.node.getRuleName() == "opAnd" or self.node.getRuleName() == "opOr":
            leftValue = self.children[0]
            rightValue = self.children[2]
            possible = True
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
                leftValue.constantFolding(symbolTable)
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
                leftValue.constantFolding(symbolTable)
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
                rightValue.constantFolding(symbolTable)
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
                rightValue.constantFolding(symbolTable)
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
                    elif varName.node.getRuleName() == "printFunction":
                        type = varName.children[0].node.getRuleName()
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
                        type = symbolTable.get_symbol(name)[0]
                    else:
                        if varName != None:
                            type = symbolTable.get_symbol(varName)[0]
                if self.children[1].node.getRuleName() == "+":
                    if type == None:
                        self.children[0].node.ruleName = leftValue + rightValue
                    elif type == "int":
                        self.children[0].node.ruleName = int(leftValue + rightValue)
                    elif type == "float":
                        self.children[0].node.ruleName = float(leftValue + rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue + rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
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
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
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
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
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
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "%":
                    if type == None:
                        self.children[0].node.ruleName = leftValue % rightValue
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue % rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue % rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue % rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "<":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue < rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue < rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == ">":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue > rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue > rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "==":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue == rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue == rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "<=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue <= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue <= rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == ">=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue >= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue >= rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "!=":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue >= rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue != rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "&&":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue and rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue and rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "||":
                    if varName == None:
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "int":
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                    elif symbolTable.get_symbol(varName)[0] == "float":
                        self.children[0].node.ruleName = float(leftValue or rightValue)
                    else:
                        self.children[0].node.ruleName = int(leftValue or rightValue)
                        temp = symbolTable.get_symbol(varName)
                        newArr = ["int", temp[1], temp[2]]
                        symbolTable.symbol_tables[-1][varName] = newArr
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
            else:
                value.constantFolding(symbolTable)
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
                    if value == "0":
                        self.children[0].node.ruleName = 1
                    else:
                        self.children[0].node.ruleName = 0
                    self.children.pop()
                    self.children[0].children.clear()
        else:
            for i in self.children:
                i.constantFolding(symbolTable)












