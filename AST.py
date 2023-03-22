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

    def printInDot(self):
        graph = "graph ast { \n" + self.addNodes() + self.addConnections() + "}"
        file = open("ast.dot", "w")
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

    def constantPropagation(self, dict, dict2):
        if self.node.getRuleName() == "expr":
            for i in dict2:
                dict2[i] = dict2[i] - 1
            for i in self.children:
                i.constantPropagation(dict, dict2)
        elif self.node.getRuleName() == "variableDefinition":
            rightSide = self.children[2]
            if self.children[0].children[0].node.getRuleName() == "constWord":
                name = self.children[0].children[1].children[0].node.getRuleName()
                dict[name] = self.children[2]
            else:
                name = self.children[0].children[1].children[0].node.getRuleName()
                dict[name] = self.children[2]
                dict2[name] = 2
            rightSide.constantPropagation(dict, dict2)
        elif self.node.getRuleName() == "nameIdentifier":
            tempName = self.children[0].node.getRuleName()
            if tempName in dict and self.parent.node.getRuleName() != "variableDefinition" and self.parent.node.getRuleName() != "variableDeclaration" and self.parent.node.getRuleName() != "assignmentStatement":
                if tempName in dict2:
                    if dict2[tempName] <= 0:
                        del dict2[tempName]
                        del dict[tempName]
                    else:
                        self.children[0] = copy.deepcopy(dict[tempName])
                        index = self.parent.children.index(self)
                        self.children[0].parent = self.parent
                        self.parent.children[index] = self.children[0]
                else:
                    self.children[0] = copy.deepcopy(dict[tempName])
                    index = self.parent.children.index(self)
                    self.children[0].parent = self.parent
                    self.parent.children[index] = self.children[0]
        else:
            for i in self.children:
                i.constantPropagation(dict, dict2)







    def constantFolding(self):
        if self.node.getRuleName() == "opAddOrSub" or self.node.getRuleName() == "opMultOrDiv":
            leftValue = self.children[0]
            rightValue = self.children[2]
            possible = True
            if leftValue.node.getRuleName() == "int":
                leftValue = int(leftValue.children[0].node.getRuleName())
            elif leftValue.node.getRuleName() == "float":
                leftValue = float(leftValue.children[0].node.getRuleName())
            elif leftValue.node.getRuleName() == "char" or leftValue.node.getRuleName() == "nameIdentifier":
                possible = False
            else:
                leftValue.constantFolding()
                if len(leftValue.children) == 1:
                    try:
                        leftValue = int(leftValue.children[0].node.getRuleName())
                    except ValueError:
                        leftValue = float(leftValue.children[0].node.getRuleName())
                else:
                    possible = False

            if rightValue.node.getRuleName() == "int":
                rightValue = int(rightValue.children[0].node.getRuleName())
            elif rightValue.node.getRuleName() == "float":
                rightValue = float(rightValue.children[0].node.getRuleName())
            elif rightValue.node.getRuleName() == "char" or rightValue.node.getRuleName() == "nameIdentifier":
                possible = False
            else:
                rightValue.constantFolding()
                if len(rightValue.children) == 1:
                    try:
                        rightValue = int(rightValue.children[0].node.getRuleName())
                    except ValueError:
                        rightValue = float(rightValue.children[0].node.getRuleName())
                else:
                    possible = False

            if possible:
                if self.children[1].node.getRuleName() == "+":
                    self.children[0].node.ruleName = leftValue + rightValue
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "-":
                    self.children[0].node.ruleName = leftValue - rightValue
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "*":
                    self.children[0].node.ruleName = leftValue * rightValue
                    self.children.pop()
                    self.children.pop()
                    self.children[0].children.clear()
                elif self.children[1].node.getRuleName() == "/":
                    self.children[0].node.ruleName = leftValue / rightValue
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
                value.constantFolding()
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
        else:
            for i in self.children:
                i.constantFolding()












