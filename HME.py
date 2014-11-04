#-*- coding: utf-8 -*-
# HME.py
import ME
import hangul

Jaeum = list(u"ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ")
Moeum = list(u"ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅔㅒㅖ")
MultiJaeum = list(u"ㄲㄸㅃㅆㅉ")

class HME(ME.ME):
    def __init__(self, Chosung=False):
        self.states = list("SVOUAIKNRL")
        self.voca = Jaeum + Moeum + MultiJaeum
        self.outp = outp = {}
        self.func = func = {}
        self.init = "S"
        self.stack = [("", [], self.init)]

        for i in self.states:
            func[i] = {}
            outp[i] = {}

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
                outp[i][j] = lambda s, v, n: [(s[0][0] + HME.join(s[0][1][:-1]), s[0][1][-1:] + [v], n)] + s

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
                    outp[i][j] = lambda s, v, n: [(s[0][0] + HME.join(s[0][1]), [v], n)] + s

        for i in func:
            for j in func[i]:
                if not j in outp[i]:
                    outp[i][j] = lambda s, v, n: [(s[0][0], s[0][1] + [v], n)] + s
