Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X Yosemite
- Built on Python 2.7

Dependencies
------------
- hangul.py : http://sugarcube.cvs.sourceforge.net/viewvc/sugarcube/plugins/KoreanConvert/hangul.py
- python getch : http://pypi.python.org/pypi/getch

Files
-----
- DFA.py : DFA Implementation
- ME.py : Mealy Machine Implementation
- HME.py : Korean Mealy Machine Implementation
- hangul.py : Korean unicode utility by perky@FreeBSD.org
- main.py : Main code to execute Korean Automata

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
An error may occur if getch catch multibyte character from terminal. Be sure to type english characters, main.py will automately convert to Korean letters.

Usage
-----
```python
import HME
H = HME.HME(False) # True: 초성우선, False: 종성우선
H.move(u"ㄱ") # One of total 34 Vocabularies
print H.current() # Get current string
H.move(u"\x7f") # Backspace is represented as u"\x7f"
print H.current()
```
