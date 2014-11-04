#-*- coding: utf-8 -*-
import HME
import sys
try:
    import getch
except ImportError:
    import msvcrt as getch

asc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
han = u"ㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔㅁㄴㅇㄹㅎㅗㅓㅏㅣㅋㅌㅊㅍㅠㅜㅡㅃㅉㄸㄲㅆㅛㅕㅑㅒㅖㅁㄴㅇㄹㅎㅗㅓㅏㅣㅋㅌㅊㅍㅠㅜㅡ"
asc2han = {"\x7f": u"\x7f"}

for i in range(52):
    asc2han[asc[i]] = han[i]

if __name__ == "__main__":
    hme = HME.HME(True)
    while True:
        c = getch.getch()
        if c in asc2han:
            h = asc2han[c]
            sys.stdout.write("\r" + "  " * len(hme.current()))
            hme.move(h)
            sys.stdout.write("\r" + hme.current())
