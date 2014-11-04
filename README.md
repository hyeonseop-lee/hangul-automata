Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X
- Built on Python 2.7

Dependencies
------------
- hangul.py : http://sugarcube.cvs.sourceforge.net/viewvc/sugarcube/plugins/HangulConvert/hangul.py
- python getch : http://pypi.python.org/pypi/getch

Files
-----
- DFA.py : DFA Implementation
- ME.py : Mealy Machine Implementation
- HME.py : Hangul Mealy Machine Implementation
- hangul.py : Korean unicode utility by perky@FreeBSD.org
- main.py : Main code to execute Hangul Automata

Requirements
------------
- Python 2.7
- virtualenv

Setup
-----
```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Run
---
```sh
python main.py
```
