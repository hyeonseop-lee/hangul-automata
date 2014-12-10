#-*- coding: utf-8 -*-
# HME.py
import DFA
import ME
import hangul
from reyacc import parser

Bksp = list(u"\x7f")

Pad = {}
Pad[u"ㄱ"], Pad[u"ㅋ"], Pad[u"ㄲ"] = "1", "1z", "1c"
Pad[u"ㄴ"], Pad[u"ㄷ"], Pad[u"ㅌ"], Pad[u"ㄸ"] = "2", "2z", "2zz", "2zc"
Pad[u"ㄹ"] = "q"
Pad[u"ㅁ"], Pad[u"ㅂ"], Pad[u"ㅍ"], Pad[u"ㅃ"] = "w", "wz", "wzz", "wzc"
Pad[u"ㅅ"], Pad[u"ㅈ"], Pad[u"ㅊ"], Pad[u"ㅉ"], Pad[u"ㅆ"] = "a", "az", "azz", "azc", "ac"
Pad[u"ㅇ"], Pad[u"ㅎ"] = "s", "sz"
Pad[u"ㅏ"], Pad[u"ㅑ"] = "3", "3z"
Pad[u"ㅓ"], Pad[u"ㅕ"] = "33", "33z"
Pad[u"ㅗ"], Pad[u"ㅛ"] = "e", "ez"
Pad[u"ㅜ"], Pad[u"ㅠ"] = "ee", "eez"
Pad[u"ㅣ"] = "d"
Pad[u"ㅡ"] = "x"

def pad(v):
    if v == u"":
        return "\\e"
    if v in Pad:
        return Pad[v]
    if v in hangul.Jaeum.MultiElement:
        return ''.join([pad(i) for i in hangul.Jaeum.MultiElement[v]])
    if v in hangul.Moeum.MultiElement:
        return ''.join([pad(i) for i in hangul.Moeum.MultiElement[v]])

Hangul = "((%s)(%s)(%s))*" % ( \
        "+".join([pad(i) for i in hangul.Choseong]), \
        "+".join([pad(i) for i in hangul.Jungseong]), \
        "+".join([pad(i) for i in hangul.Jongseong]))

class HME(ME.ME):
    def __init__(self, Choseong = False):
        dfa = parser.parse(Hangul).toNFA().toDFA().minimized()
        self.states = dfa.states
        self.voca = dfa.voca
        self.func = dfa.func
        self.init = dfa.init
        self.Choseong = Choseong

        out = {
            "1": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㄱ"], n)] + s,
            "2": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㄴ"], n)] + s,
            "3": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅏ"], n)] + s if s[0][1][-1] != u"ㅏ" else [(s[0][0], s[0][1][:-1] + [u"ㅓ"], n)] + s[1:],
            "q": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㄹ"], n)] + s,
            "w": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅁ"], n)] + s,
            "e": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅗ"], n)] + s if s[0][1][-1] != u"ㅗ" else [(s[0][0], s[0][1][:-1] + [u"ㅜ"], n)] + s[1:],
            "a": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅅ"], n)] + s,
            "s": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅇ"], n)] + s,
            "d": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅣ"], n)] + s,
            "z": lambda s, v, n: [(s[0][0], s[0][1][:-1] + [{u"ㄱ": u"ㅋ", u"ㄴ": u"ㄷ", u"ㄷ": u"ㅌ", u"ㅁ": u"ㅂ", u"ㅂ": u"ㅍ", u"ㅅ": u"ㅈ", u"ㅈ": u"ㅊ", u"ㅇ": u"ㅎ", u"ㅏ": u"ㅑ", u"ㅓ": u"ㅕ", u"ㅗ": u"ㅛ", u"ㅜ": u"ㅠ"}[s[0][1][-1]]], n)] + s[1:],
            "x": lambda s, v, n: [(s[0][0], s[0][1] + [u"ㅡ"], n)] + s,
            "c": lambda s, v, n: [(s[0][0], s[0][1][:-1] + [{u"ㄱ": u"ㄲ", u"ㄷ": u"ㄸ", u"ㅂ": u"ㅃ", u"ㅅ": u"ㅆ", u"ㅈ": u"ㅉ"}[s[0][1][-1]]], n)] + s[1:]
        }
        self.outp = {}
        for s in self.func:
            self.outp[s] = {}
            for v in self.func[s]:
                self.outp[s][v] = out[v]

        self.now = self.init
        self.inp = []
        self.stack = [("", [], self.init)]

    def reducestack(self):
        s, v, n = self.stack[0]
        moeum = {
            (u"ㅏ", u"ㅣ"): u"ㅐ",
            (u"ㅑ", u"ㅣ"): u"ㅒ",
            (u"ㅓ", u"ㅣ"): u"ㅔ",
            (u"ㅕ", u"ㅣ"): u"ㅖ",
            (u"ㅗ", u"ㅏ"): u"ㅘ",
            (u"ㅗ", u"ㅣ"): u"ㅚ",
            (u"ㅘ", u"ㅣ"): u"ㅙ",
            (u"ㅜ", u"ㅓ"): u"ㅝ",
            (u"ㅜ", u"ㅣ"): u"ㅟ",
            (u"ㅝ", u"ㅣ"): u"ㅞ",
            (u"ㅡ", u"ㅣ"): u"ㅢ"
        }
        jaeum = {
            (u"ㄱ", u"ㅅ"): u"ㄳ",
            (u"ㄴ", u"ㅈ"): u"ㄵ",
            (u"ㄴ", u"ㅎ"): u"ㄶ",
            (u"ㄹ", u"ㄱ"): u"ㄺ",
            (u"ㄹ", u"ㅁ"): u"ㄻ",
            (u"ㄹ", u"ㅂ"): u"ㄼ",
            (u"ㄹ", u"ㅅ"): u"ㄽ",
            (u"ㄹ", u"ㅌ"): u"ㄾ",
            (u"ㄹ", u"ㅍ"): u"ㄿ",
            (u"ㄹ", u"ㅎ"): u"ㅀ",
            (u"ㅂ", u"ㅅ"): u"ㅄ"
        }
        if len(v) == 3 and (v[1], v[2]) in moeum:
            self.stack = [(s, [v[0], moeum[(v[-2], v[-1])]], n)] + self.stack[1:]
        elif len(v) == 3 and hangul.isJaeum(v[2]) and v[2] not in hangul.Jongseong:
            s += hangul.join((v[0], v[1], ""))
            self.stack = [(s, [v[2]], n), (s, [], self.init)] + self.stack[3:]
        elif len(v) == 4 and hangul.isMoeum(v[3]):
            s += hangul.join((v[0], v[1], ""))
            self.stack = [(s, [v[2], v[3]], n), (s, [v[2]], self.stack[1][2]), (s, [], self.init)] + self.stack[4:]
        elif len(v) == 4 and (v[2], v[3]) not in jaeum:
            s += hangul.join((v[0], v[1], v[2]))
            self.stack = [(s, [v[3]], n), (s, [], self.init)] + self.stack[4:]
        elif len(v) == 5 and hangul.isMoeum(v[4]):
            s += hangul.join((v[0], v[1], v[2]))
            self.stack = [(s, [v[3], v[4]], n), (s, [v[3]], self.stack[1][2]), (s, [], self.init)] + self.stack[5:]
        elif len(v) == 5 and hangul.isJaeum(v[4]):
            s += hangul.join((v[0], v[1], jaeum[(v[2], v[3])]))
            self.stack = [(s, [v[4]], n), (s, [], self.init)] + self.stack[5:]

    def move(self, voca, debug=False):
        res = ME.ME.move(self, voca, debug)
        if res:
            self.stack = res(self.stack, voca, self.now)
            self.reducestack()
            self.now = self.stack[0][2]
        return bool(res)

    def current(self):
        s, v, n = self.stack[0]
        jaeum = {
            (u"ㄱ", u"ㅅ"): u"ㄳ",
            (u"ㄴ", u"ㅈ"): u"ㄵ",
            (u"ㄴ", u"ㅎ"): u"ㄶ",
            (u"ㄹ", u"ㄱ"): u"ㄺ",
            (u"ㄹ", u"ㅁ"): u"ㄻ",
            (u"ㄹ", u"ㅂ"): u"ㄼ",
            (u"ㄹ", u"ㅅ"): u"ㄽ",
            (u"ㄹ", u"ㅌ"): u"ㄾ",
            (u"ㄹ", u"ㅍ"): u"ㄿ",
            (u"ㄹ", u"ㅎ"): u"ㅀ",
            (u"ㅂ", u"ㅅ"): u"ㅄ"
        }
        if len(v) == 0:
            return ""
        elif len(v) == 1:
            return s + v[0]
        elif len(v) == 2:
            return s + hangul.join((v[0], v[1], ""))
        elif len(v) == 3:
            if hangul.isMoeum(v[2]) or self.Choseong:
                return s + hangul.join((v[0], v[1], "")) + v[2]
            else:
                return s + hangul.join((v[0], v[1], v[2]))
        elif len(v) == 4:
            if self.Choseong:
                return s + hangul.join((v[0], v[1], v[2])) + v[3]
            else:
                return s + hangul.join((v[0], v[1], jaeum[(v[2], v[3])]))
