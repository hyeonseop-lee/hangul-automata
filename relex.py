# relex.py
import ply.lex as lex

tokens = ("PLUS", "STAR", "LPAREN", "RPAREN", "SYMBOL")

t_PLUS = r"\+"
t_STAR = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SYMBOL = r"[0-9A-Za-z]"
t_ignore = " \t\r\n"

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()
