Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X
- Built on Python 2.7

Files
-----
- DFA.py : DFA Implementation
- NFA.py : NFA Implementation
- test.py : Testing code
- test.json : Test DFA in json form

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
```python
import NFA
A = NFA.FromFile("test.json")
B = A.toDFA()
print B.query("01011")
```

Input
-----
```json
{
	"states": [], // list of states..
	"voca": [], // list of vocabularies..
	"func": {
		"state": {
			"": ["e-move state"],
			"vocabulary": ["next state", "next state"]
		}
	},
	"init": "", // an initial state
	"fini": [] // list of final states..
}
