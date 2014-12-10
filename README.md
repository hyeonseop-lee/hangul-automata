Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X
- Built on Python 2.7

Files
-----
- DFA.py : DFA Implementation
- NFA.py : NFA Implementation
- AST.py : Abstract Syntax Tree for regular expression
- ME.py : Mealy Machine Implementation
- HME.py : Korean Mealy Machine with 3x4 Pad Implementaion
- relex.py : lex code with PLY
- reyacc.py : yacc code with PLY
- main.py : main code to interact with regular expression

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
Use 3x4 key mapping as below.
<pre>
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|   ㄱ  |   ㄴ  |  ㅏㅓ |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   q   |   w   |   e   |
|   ㄹ  |   ㅁ  |  ㅗㅜ |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   a   |   s   |   d   |
|   ㅅ  |   ㅇ  |   ㅣ  |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   z   |   x   |   c   |
| 획추가|   ㅡ  | 쌍자음|
|       |       |       |
+-------+-------+-------+
</pre>
Be sure to type lowercase letters.

Usage
-----
```python
import HME
H = HME.HME(False) # True: 초성우선, False: 종성우선
H.move(u"w") # One of 3x4 Pad or Backspace
H.move(u"z")
H.move(u"e")
H.move(u"e")
H.move(u"3")
H.move(u"3")
H.move(u"d")
H.move(u"q")
H.move(u"1")
print H.current() # Get current string
H.move(u"\x7f") # Backspace is represented as u"\x7f"
print H.current()
```
