from reyacc import parser

res = raw_input("Regular Expression: ")
ast = parser.parse(res)
nfa = ast.toNFA()
dfa = nfa.toDFA()
dfa = dfa.minimized()

while True:
    req = raw_input("> ")
    print dfa.query(req)
