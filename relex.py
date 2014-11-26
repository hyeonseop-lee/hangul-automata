# relex.py
import ply.lex as lex

tokens = ("EPSILON", "PHI", "SYMBOL", "PLUS", "STAR", "LPAREN", "RPAREN")

t_EPSILON = r"\\e"
t_PHI = r"\\p"
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
