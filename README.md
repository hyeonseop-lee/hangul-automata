Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X
- Built on Python 2.7

Files
-----
- DFA.py : DFA Implementation
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
import DFA
A = DFA.FromFile("test.json")
print A.query("01011")
```

Input
-----
```json
{
	"states": [], // list of states..
	"voca": [], // list of vocabularies..
	"func": {
		"state": {
			"vocabulary": "next state"
		}
	},
	"init": "", // an initial state
	"fini": [] // list of final states..
}
