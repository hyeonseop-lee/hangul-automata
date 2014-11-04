#-*- coding: utf-8 -*-
import HME
import sys
try:
    import getch
except ImportError:
    import msvcrt as getch

asc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
han = u"ㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔㅁㄴㅇㄹㅎㅗㅓㅏㅣㅋㅌㅊㅍㅠㅜㅡㅃㅉㄸㄲㅆㅛㅕㅑㅒㅖㅁㄴㅇㄹㅎㅗㅓㅏㅣㅋㅌㅊㅍㅠㅜㅡ"
asc2han = {}

for i in range(52):
    asc2han[asc[i]] = han[i]

if __name__ == "__main__":
    hme = HME.HME()
    while True:
        c = getch.getch()
        h = asc2han[c]
        hme.move(h)
        sys.stdout.write("\r" + hme.current())
