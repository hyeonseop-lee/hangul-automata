#-*- coding: utf-8 -*-
# HME.py
import ME
import hangul

Jaeum = list(u"ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ")
Moeum = list(u"ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅔㅒㅖ")
MultiJaeum = list(u"ㄲㄸㅃㅆㅉ")
Bksp = list(u"\x7f")

class HME(ME.ME):
    def __init__(self, Chosung=False):
        self.states = list("SVOUAIKNRL")
        self.voca = Jaeum + Moeum + MultiJaeum + Bksp
        self.outp = outp = {}
        self.func = func = {}
        self.init = "S"
        self.stack = [("", [], self.init)]

        for i in self.states:
            func[i] = {}
            outp[i] = {}

        for i in "VOUAIKNRL":
            func[i][u"\x7f"] = "L"
            outp[i][u"\x7f"] = lambda s, v, n: s[1:]

        for i in Jaeum + MultiJaeum:
            func["S"][i] = "V"

        for i in "VKNRL":
            for j in u"ㅗ":
                func[i][j] = "O"
            for j in u"ㅜ":
                func[i][j] = "U"
            for j in u"ㅏㅑㅓㅕㅡ":
                func[i][j] = "A"
            for j in u"ㅛㅠㅣㅐㅒㅔㅖ":
                func[i][j] = "I"
        for i in "KNRL":
            for j in Moeum:
                outp[i][j] = lambda s, v, n: [(s[0][0] + HME.Join(s[0][1][:-1]), [s[0][1][-1], v], n), (s[0][0] + HME.Join(s[0][1][:-1]), [s[0][1][-1]], s[0][2]), (s[0][0] + HME.Join(s[0][1][:-1]), [], "L")] + s[len(s[0][1]):]

        func["O"][u"ㅏ"] = "A"
        func["O"][u"ㅣ"] = "I"
        func["O"][u"ㅐ"] = "I"
        func["U"][u"ㅓ"] = "A"
        func["U"][u"ㅣ"] = "I"
        func["U"][u"ㅔ"] = "I"
        for i in "OUAI":
            for j in u"ㄱㅂ":
                func[i][j] = "K"
            for j in u"ㄴ": 
                func[i][j] = "N"
            for j in u"ㄹ": 
                func[i][j] = "R"
            for j in u"ㄸㅃㅉ":
                func[i][j] = "V"
            for j in Jaeum + MultiJaeum:
                if not j in func[i]:
                    func[i][j] = "L"

        for i in u"ㅅ":
            func["K"][i] = "L"
        for i in u"ㅈㅎ":
            func["N"][i] = "L"
        for i in u"ㄱㅁㅂㅅㅌㅍㅎ":
            func["R"][i] = "L"
        for i in "KNRL":
            for j in Jaeum + MultiJaeum:
                if not j in func[i]:
                    func[i][j] = "V"
                    outp[i][j] = lambda s, v, n: [(s[0][0] + HME.Join(s[0][1]), [v], n)] + [(s[0][0] + HME.Join(s[0][1]), [], "L")] + s[len(s[0][1]):]

        for i in func:
            for j in func[i]:
                if not j in outp[i]:
                    outp[i][j] = lambda s, v, n: [(s[0][0], s[0][1] + [v], n)] + s

        self.now = self.init
        self.inp = []

    def move(self, voca, debug=False):
        self.stack = ME.ME.move(self, voca, debug)(self.stack, voca, self.now)
        self.now = self.stack[0][2]

    @classmethod
    def Join(cls, buf):
        cho, jung, jong = [], [], []
        while len(buf) and hangul.isJaeum(buf[0]):
            cho.append(buf[0])
            buf = buf[1:]
        if len(cho) == 0:
            cho = u""
        elif len(cho) == 1:
            cho = cho[0]
        else:
            for i in hangul.Jaeum.MultiElement:
                if hangul.Jaeum.MultiElement[i] == (cho[0], cho[1]):
                    cho = i
                    break

        while len(buf) and hangul.isMoeum(buf[0]):
            jung.append(buf[0])
            buf = buf[1:]
        if len(jung) == 0:
            jung = u""
        elif len(jung) == 1:
            jung = jung[0]
        else:
            for i in hangul.Moeum.MultiElement:
                if hangul.Moeum.MultiElement[i] == (jung[0], jung[1]):
                    jung = i
                    break

        while len(buf) and hangul.isJaeum(buf[0]):
            jong.append(buf[0])
            buf = buf[1:]
        if len(jong) == 0:
            jong = u""
        elif len(jong) == 1:
            jong = jong[0]
        else:
            for i in hangul.Jaeum.MultiElement:
                if hangul.Jaeum.MultiElement[i] == (jong[0], jong[1]):
                    jong = i
                    break

        return hangul.join((cho, jung, jong))

    def current(self):
        return self.stack[0][0] + self.Join(self.stack[0][1])
