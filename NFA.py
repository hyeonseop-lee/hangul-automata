# NFA.py
import DFA

class NFA(DFA.DFA):
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
                for n in self.func[s][v]:
                    assert n in self.states

    def toDFA(self):
        emove = {}
        def dfs(now, emove):
            emove[now] = set([now])
            if "" in self.func[now]:
                for i in self.func[now][""]:
                    if not i in emove:
                        dfs(i, emove)
                    emove[now] |= emove[i]
        for i in self.states:
            if not i in emove:
                dfs(i, emove)
        init = frozenset(emove[self.init])
        states = set([init])
        func = {init: {}}
        que = [init]
        while que:
            now = que[0]
            for i in self.voca:
                if i == "":
                    continue
                move = set()
                for j in now:
                    if not i in self.func[j]:
                        continue
                    for k in self.func[j][i]:
                        move |= emove[k]
                if not move:
                    continue
                move = frozenset(move)
                func[now][i] = move
                if not move in states:
                    states.add(move)
                    func[move] = {}
                    que.append(move)
            que = que[1:]
        dfa = {}
        dfa["states"] = list(states)
        dfa["voca"] = self.voca
        dfa["func"] = func
        dfa["init"] = init
        dfa["fini"] = []
        for i in states:
            for j in self.fini:
                if j in i:
                    dfa["fini"].append(i)
                    break
        return DFA.DFA(dfa)
