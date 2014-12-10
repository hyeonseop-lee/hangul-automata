#-*- coding: utf-8 -*-
import HME
import sys
try:
    import getch
except ImportError:
    import msvcrt as getch

inp = "123qweasdzxc\x7f"

if __name__ == "__main__":
    hme = HME.HME(True)
    while True:
        c = getch.getch()
        if c in inp:
            sys.stdout.write("\r" + "  " * len(hme.current()))
            hme.move(c)
            sys.stdout.write("\r" + hme.current())
