import NFA

A = NFA.NFA.FromFile("test.json")
B = A.toDFA().minimized()
B.query("000", True)
B.query("011", True)
B.query("01101101", True)
B.query("001101010011", True)
