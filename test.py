import DFA
import ME

A = DFA.DFA.FromFile("test.json")
print A.query("000", True)
print A.query("011", True)
print A.query("01101101", True)
print A.query("001101010011", True)

B = ME.ME.FromFile("test.json")
print B.query("000", True)
print B.query("011", True)
print B.query("01101101", True)
print B.query("001101010011", True)
