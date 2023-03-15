from antlr4 import *
from MyGrammarParser import MyGrammarParser

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
        elif self.node.getRuleName() == "opUnary" and len(self.children) == 2:
            self.children[1].optimize()

        elif len(self.children) == 1:
            found = False
            temp = self
            while not found:
                temp = temp.children[0]
                if len(temp.children) == 3:
                    temp.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp
                    for i in temp.children:
                        i.optimize()
                    found = True
                elif temp.node.getRuleName() == "opUnary" and len(temp.children) == 2:
                    temp.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp
                    temp.children[1].optimize()
                    found = True
                elif temp.node.getRuleName() == "int" or temp.node.getRuleName() == "float":
                    temp.parent = self.parent
                    index = self.parent.children.index(self)
                    self.parent.children[index] = temp
                    found = True
        elif len(self.children) == 3:
            for i in self.children:
                i.optimize()





    def constantFolding(self):
        if self.node.getRuleName() == "prog" or self.node.getRuleName() == "expr":
            for i in self.children:
                i.constantFolding()
        elif self.node.getRuleName() == "opAddOrSub":
            if self.children[0].node.getRuleName() == "int" or self.children[0].node.getRuleName() == "float":
                try:
                    leftValue = int(self.children[0].children[0].node.getRuleName())
                except ValueError:
                    leftValue = float(self.children[0].children[0].node.getRuleName())
            else:
                self.children[0].constantFolding()
                try:
                    leftValue = int(self.children[0].children[0].node.getRuleName())
                except ValueError:
                    leftValue = float(self.children[0].children[0].node.getRuleName())

            if self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float":
                try:
                    rightValue = int(self.children[2].children[0].node.getRuleName())
                except ValueError:
                    rightValue = float(self.children[2].children[0].node.getRuleName())
            else:
                self.children[2].constantFolding()
                try:
                    rightValue = int(self.children[2].children[0].node.getRuleName())
                except ValueError:
                    rightValue = float(self.children[2].children[0].node.getRuleName())

            if self.children[1].node.getRuleName() == "+":
                value = leftValue + rightValue
            else:
                value = leftValue - rightValue
            self.children[0].node.ruleName = value
            self.children[0].children.clear()
            self.children.pop()
            self.children.pop()

        elif self.node.getRuleName() == "opMultOrDiv":
            if self.children[0].node.getRuleName() == "int" or self.children[0].node.getRuleName() == "float":
                try:
                    leftValue = int(self.children[0].children[0].node.getRuleName())
                except ValueError:
                    leftValue = float(self.children[0].children[0].node.getRuleName())
            else:
                self.children[0].constantFolding()
                try:
                    leftValue = int(self.children[0].children[0].node.getRuleName())
                except ValueError:
                    leftValue = float(self.children[0].children[0].node.getRuleName())

            if self.children[2].node.getRuleName() == "int" or self.children[2].node.getRuleName() == "float":
                try:
                    rightValue = int(self.children[2].children[0].node.getRuleName())
                except ValueError:
                    rightValue = float(self.children[2].children[0].node.getRuleName())
            else:
                self.children[2].constantFolding()
                try:
                    rightValue = int(self.children[2].children[0].node.getRuleName())
                except ValueError:
                    rightValue = float(self.children[2].children[0].node.getRuleName())

            if self.children[1].node.getRuleName() == "*":
                value = leftValue * rightValue
            elif self.children[1].node.getRuleName() == "/":
                value = leftValue / rightValue
            else:
                value = leftValue % rightValue
            self.children[0].node.ruleName = value
            self.children[0].children.clear()
            self.children.pop()
            self.children.pop()

        elif self.node.getRuleName() == "opUnary":
            leftValue = self.children[0].node.getRuleName()
            if leftValue == "!":
                self.children[1].constantFolding()
            else:
                if self.children[1].node.getRuleName() == "int" or self.children[1].node.getRuleName() == "float":
                    try:
                        rightValue = int(self.children[1].children[0].node.getRuleName())
                    except ValueError:
                        rightValue = float(self.children[1].children[0].node.getRuleName())
                else:
                    self.children[1].constantFolding()
                    try:
                        rightValue = int(self.children[1].children[0].node.getRuleName())
                    except ValueError:
                        rightValue = float(self.children[1].children[0].node.getRuleName())

                if leftValue == "-":
                    value = -rightValue
                elif leftValue == "+":
                    value = +rightValue
                self.children[0].node.ruleName = value
                self.children[0].children.clear()
                self.children.pop()






