#-*- coding: utf-8 -*-
import sys
import hangul

if __name__ == "__main__":
    s = ''
    while True:
        s += sys.stdin.read(1)
        try:
            u = s.decode('utf-8')
        except UnicodeDecodeError:
            pass
        else:
            s = ''
            if hangul.ishangul(u):
                for i in hangul.split(u):
                    if i != u'':
                        print i
