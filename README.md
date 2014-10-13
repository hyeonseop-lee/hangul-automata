Korean-Automata
===============

Korean Automata Project in KAIST CS322
- Implemeted on OS X
- Built on Python 2.7

Files
-----
- DFA.py : DFA Implementation
- ME.py : Mealy Machine Implementation
- test.py : Testing code
- test.json : Test DFA and ME in json form

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
import ME
A = DFA.DFA.FromFile("test.json")
print A.query("01011")
B = ME.ME.FromFile("test.json")
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
			"vocabulary": "next state"
		}
	},
	"outp": { // for ME
		"state": {
			"vocabulary": "output object"
		}
	},
	"init": "", // an initial state
	"fini": [] // for DFA, list of final states..
}
