# ME.py
import json
import DFA

class ME(DFA.DFA):
# Init ME with ME object
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

        self.now = self.init
        self.inp = []

# Move state with a vocabulary
    def move(self, voca, debug=False):
        last = self.now
        assert voca in self.voca
        try:
            now = self.func[last][voca]
            res = self.outp[last][voca]
        except KeyError:
            if debug:
                print "%s: %s -> ?" % (repr(voca), repr(self.now))
            return False
        else:
            if debug:
                print "%s: %s -> %s : %s" % (repr(voca), repr(self.now), repr(now), repr(res))
            self.now = now
        return res

# Query with iterable of vocabularies
    def query(self, inp, debug=False):
        self.now = self.init
        return [self.move(v, debug) for v in inp]
