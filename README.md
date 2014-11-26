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
Use \e instead of ε, \p instead of ∅. Compiled DFA is expected to process only queries which was conisted of symbols that appeared in reguler expression.

Usage
-----
```python
from reyacc import parser
...
parser.parse(expression).toNFA().toDFA().minimized().query(querystring)
```
