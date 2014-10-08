# DFA.py
import json

def FromJson(obj):
    return DFA(json.loads(obj))

def FromFile(path):
    with open(path, "r") as f:
        return FromJson(f.read())

class DFA:
    def __init__(self, obj):
        self.states = obj["states"]
        self.voca = obj["voca"]
        self.func = obj["func"]
        self.init = obj["init"]
        self.fini = obj["fini"]

        assert self.init in self.states
        for s in self.fini:
            assert s in self.states
        for s in self.func:
            assert s in self.states
            for v in self.func[s]:
                assert self.func[s][v] in self.states

    def query(self, inp, debug=False):
        t = s = self.init
        for v in inp:
            assert v in self.voca
            try:
                s = self.func[s][v]
            except KeyError:
                return false
            else:
                if debug:
                    print "%s: %s -> %s" % (repr(v), repr(t), repr(s))
                    t = s
        r = s in self.fini
        if debug:
            print "%s : %s" % (repr(inp), r)
        return r
