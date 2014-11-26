# AST.py
import NFA

class Node(object):
    def __init__(self):
        super(Node, self).__init__()

    def __repr__(self):
        return "(%s)" % self.__class__.__name__

    def toNFA(self):
        nfa = {}
        nfa["states"] = ["q"]
        nfa["voca"] = []
        nfa["func"] = {"q": {}}
        nfa["init"] = "q"
        nfa["fini"] = ["q"]
        return NFA.NFA(nfa)

class Epsilon(Node):
    pass

class Phi(Node):
    def toNFA(self):
        nfa = {}
        nfa["states"] = ["s", "f"]
        nfa["voca"] = []
        nfa["func"] = {"s": {}, "f": {}}
        nfa["init"] = "s"
        nfa["fini"] = ["f"]
        return NFA.NFA(nfa)

class Symbol(Node):
    def __init__(self, symbol):
        super(Symbol, self).__init__()
        self.symbol = symbol

    def __repr__(self):
        return "(%s %s)" % (self.__class__.__name__, self.symbol)

    def toNFA(self):
        nfa = {}
        nfa["states"] = ["s", "f"]
        nfa["voca"] = [self.symbol]
        nfa["func"] = {"s": {self.symbol: ["f"]}, "f": {}}
        nfa["init"] = "s"
        nfa["fini"] = ["f"]
        return NFA.NFA(nfa)

class Plus(Node):
    def __init__(self, left, right):
        super(Plus, self).__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(%s %s %s)" % (self.__class__.__name__, self.left, self.right)
    
    def toNFA(self):
        left = self.left.toNFA()
        right = self.right.toNFA()
        nfa = {}
        nfa["states"] = ["s", "f"] + ["l" + i for i in left.states] + ["r" + i for i in right.states]
        nfa["voca"] = list(set(left.voca).union(set(right.voca)))
        nfa["func"] = {"s": {"": ["l" + left.init, "r" + right.init]}, "f": {}}
        for n, p in ((left, "l"), (right, "r")):
            for i in n.func:
                nfa["func"][p + i] = {}
                for j in n.func[i]:
                    nfa["func"][p + i][j] = [p + k for k in n.func[i][j]]
            for i in n.fini:
                if not "" in nfa["func"][p + i]:
                    nfa["func"][p + i][""] = []
                nfa["func"][p + i][""].append("f")
        nfa["init"] = "s"
        nfa["fini"] = ["f"]
        return NFA.NFA(nfa)

class Concat(Node):
    def __init__(self, left, right):
        super(Concat, self).__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(%s %s %s)" % (self.__class__.__name__, self.left, self.right)

    def toNFA(self):
        left = self.left.toNFA()
        right = self.right.toNFA()
        nfa = {}
        nfa["states"] = ["l" + i for i in left.states] + ["r" + i for i in right.states]
        nfa["voca"] = list(set(left.voca).union(right.voca))
        nfa["func"] = {}
        for n, p in ((left, "l"), (right, "r")):
            for i in n.func:
                nfa["func"][p + i] = {}
                for j in n.func[i]:
                    nfa["func"][p + i][j] = [p + k for k in n.func[i][j]]
        for i in left.fini:
            if not "" in nfa["func"]["l" + i]:
                nfa["func"]["l" + i][""] = []
            nfa["func"]["l" + i][""].append("r" + right.init)
        nfa["init"] = "l" + left.init
        nfa["fini"] = ["r" + i for i in right.fini]
        return NFA.NFA(nfa)

class Star(Node):
    def __init__(self, expr):
        super(Star, self).__init__()
        self.expr = expr

    def __repr__(self):
        return "(%s %s)" % (self.__class__.__name__, self.expr)

    def toNFA(self):
        e = self.expr.toNFA()
        nfa = {}
        nfa["states"] = ["s", "f"] + ["e" + i for i in e.states]
        nfa["voca"] = e.voca
        nfa["func"] = {"s": {"": ["e" + e.init, "f"]}, "f": {"": ["s"]}}
        for i in e.states:
            nfa["func"]["e" + i] = {}
            for j in e.func[i]:
                nfa["func"]["e" + i][j] = ["e" + k for k in e.func[i][j]]
        for i in e.fini:
            if not "" in nfa["func"]["e" + i]:
                nfa["func"]["e" + i][""] = []
            nfa["func"]["e" + i][""].append("f")
        nfa["init"] = "s"
        nfa["fini"] = ["f"]
        return NFA.NFA(nfa)
