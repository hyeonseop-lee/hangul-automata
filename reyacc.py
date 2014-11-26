# reyacc.py
import ply.yacc as yacc

import AST
from relex import tokens

def p_expression_symbol(p):
    "expression : SYMBOL"
    p[0] = AST.Symbol(p[1])

def p_expression_plus(p):
    "expression : expression PLUS expression"
    p[0] = AST.Plus(p[1], p[3])

def p_expression_concat(p):
    "expression : expression expression %prec SYMBOL"
    p[0] = AST.Concat(p[1], p[2])

def p_expression_star(p):
    "expression : expression STAR"
    p[0] = AST.Star(p[1])

def p_expression_paren(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_error(p):
    print "syntax error"

precedence = (
    ("left", "PLUS"),
    ("left", "SYMBOL"),
    ("left", "STAR"),
    ("left", "LPAREN", "RPAREN")
)

parser = yacc.yacc()
