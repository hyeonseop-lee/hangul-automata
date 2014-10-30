# DFA.py
import json

class DFA:
# Init DFA with DFA object
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

        self.now = self.init
        self.inp = []

# Move state with a vocabulary
    def move(self, voca, debug=False):
        assert voca in self.voca
        try:
            now = self.func[self.now][voca]
        except KeyError:
            if debug:
                print "%s: %s -> ?" % (repr(voca), repr(self.now))
            return False
        else:
            if debug:
                print "%s: %s -> %s" % (repr(voca), repr(self.now), repr(now))
            self.now = now
            self.inp.append(voca)
        return True

# Query if DFA is in Final State
    def final(self, debug=False):
        r = self.now in self.fini
        if debug:
            print "%s: %s" % (repr(self.inp), repr(r))
        return r

# Query with iterable of vocabularies
    def query(self, inp, debug=False):
        self.now = self.init
        for v in inp:
            if not self.move(v, debug):
                return False
        return self.final(debug)

# Load DFA from JSON string
    @classmethod
    def FromJson(cls, obj):
        return cls(json.loads(obj))

# Load DFA from JSON file
    @classmethod
    def FromFile(cls, path):
        with open(path, "r") as f:
            return cls.FromJson(f.read())
