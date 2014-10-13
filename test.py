import DFA

A = DFA.DFA.FromFile("test.json")
A.query("000", True)
A.query("011", True)
A.query("01101101", True)
A.query("001101010011", True)
