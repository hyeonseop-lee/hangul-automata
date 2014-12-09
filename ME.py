# ME.py
import json
import DFA

class ME(DFA.DFA):
    def __init__(self, obj):
        self.states = obj["states"]
        self.voca = obj["voca"]
        self.outp = obj["outp"]
        self.func = obj["func"]
        self.init = obj["init"]

        assert self.init in self.states
        for s in self.func:
            assert s in self.states
            for v in self.func[s]:
                assert self.func[s][v] in self.states

    def query(self, inp, debug=False):
        t = s = self.init
        r = []
        for v in inp:
            assert v in self.voca
            try:
                s = self.func[s][v]
                r.append(self.outp[t][v])
            except KeyError:
                return r
            else:
                if debug:
                    print "%s: %s -> %s" % (repr(v), repr(t), repr(s))
                    t = s
        if debug:
            print "%s : %s" % (repr(inp), repr(r))
        return r
