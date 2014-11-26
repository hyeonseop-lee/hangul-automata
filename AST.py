# AST.py

class Node(object):
    def __init__(self):
        super(Node, self).__init__()

    def __repr__(self):
        return "(%s)" % self.__class__.__name__

class Symbol(Node):
    def __init__(self, symbol):
        super(Symbol, self).__init__()
        self.symbol = symbol

    def __repr__(self):
        return "(%s %s)" % (self.__class__.__name__, self.symbol)

class Plus(Node):
    def __init__(self, left, right):
        super(Plus, self).__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(%s %s %s)" % (self.__class__.__name__, self.left, self.right)

class Concat(Node):
    def __init__(self, left, right):
        super(Concat, self).__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(%s %s %s)" % (self.__class__.__name__, self.left, self.right)

class Star(Node):
    def __init__(self, expr):
        super(Star, self).__init__()
        self.expr = expr

    def __repr__(self):
        return "(%s %s)" % (self.__class__.__name__, self.expr)
