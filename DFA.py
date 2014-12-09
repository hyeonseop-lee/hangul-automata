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

    def minimized(self):
        def dst(v1, v2, log):
            if (v2, v1) in log:
                v1, v2 = v2, v1
            if (v1, v2) in log:
                return log[(v1, v2)]
            if (v1 in self.fini) != (v2 in self.fini):
                return True
            log[(v1, v2)] = False
            for i in self.voca:
                if i in self.func[v1] and i in self.func[v2]:
                    if dst(self.func[v1][i], self.func[v2][i], log):
                        log[(v1, v2)] = True
                        break
                elif i in self.func[v1] or i in self.func[v2]:
                    log[(v1, v2)] = True
                    break
            return log[(v1, v2)]
        def dfs(now, chk):
            chk.add(now)
            for i in self.func[now]:
                if not self.func[now][i] in chk:
                    dfs(self.func[now][i], chk)
        chk = set()
        log = {}
        dfs(self.init, chk)
        dfa = {}
        eqv = {}
        dfa["states"] = []
        for i in chk:
            for j in dfa["states"]:
                if not dst(i, j, log):
                    eqv[i] = j
                    break
            else:
                dfa["states"].append(i)
                eqv[i] = i
        dfa["voca"] = self.voca
        dfa["func"] = {i: {j: eqv[self.func[i][j]] for j in self.func[i]} for i in dfa["states"]}
        dfa["init"] = eqv[self.init]
        dfa["fini"] = list(set([eqv[i] for i in self.fini]))
        return DFA(dfa)

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
