from reyacc import parser

res = raw_input("Regular Expression: ")
ast = parser.parse(res)
nfa = ast.toNFA()
dfa = nfa.toDFA()

while True:
    req = raw_input("> ")
    print dfa.query(req)
