import ply.yacc as yacc
from lexico import *
import sintaxeabstrata as sa


def p_programa(p):
  '''programa : INICIO functionorcmds FIM'''
  p[0] = p[2]


def p_functionorcmds(p):
  '''functionorcmds : comando
                    | function
                    | comando functionorcmds
                    | function functionorcmds'''
  pass


def p_comando(p):
  '''comando : VAR ATRIBUICAO expressao PONTOVIRGULA
             | expressao PONTOVIRGULA
             | RETURN expressao PONTOVIRGULA
             | IF LPAREN expressao RPAREN LCHAV listadecomandos RCHAV ELSE LCHAV listadecomandos RCHAV
             | IF LPAREN expressao RPAREN LCHAV listadecomandos RCHAV
             | FOR LPAREN atribuir PONTOVIRGULA expressao PONTOVIRGULA expressao RPAREN LCHAV listadecomandos RCHAV
             | WHILE LPAREN expressao RPAREN LCHAV listadecomandos RCHAV'''
  pass


def p_listadecomandos(p):
  '''listadecomandos : comando
                     | listadecomandos comando'''
  pass
  #if (len(p) == 3):
  #  p[0] = p[1] + p[2]
  #else:
  #  p[0] = p[1]


def p_function(p):
  '''function : ID LPAREN parametros RPAREN LCHAV listadecomandos RCHAV
              | ID LPAREN RPAREN LCHAV listadecomandos RCHAV'''
  pass


def p_expressao(p):
  '''expressao : expressao POT exp2
               | exp2'''
  pass
  #if (len(p) == 4):
  #  p[0] = p[1] + p[2]
  #else:
  #  p[0] = p[1]


def p_exp2(p):
  '''exp2 : exp2 INCREMENTA
          | exp3'''
  pass


def p_exp3(p):
  '''exp3 : exp3 DECREMENTA
          | exp4'''
  pass

def p_exp4(p):
  '''exp4 : NOT exp5
          | exp5'''
  pass
  #if (len(p) == 3):
  #  p[0] = p[2]
  #else:
  #  p[0] = p[1]


def p_exp5(p):
  '''exp5 : exp5 MULTI exp6
          | exp6'''
  pass

def p_exp6(p):
  '''exp6 : exp6 DIVISAO exp7
          | exp7'''
  pass
          
def p_exp7(p):
  '''exp7 : exp7 MODULO exp8
          | exp8'''
  pass

def p_exp8(p):
  '''exp8 : exp8 SOMA exp9
          | exp9'''
  pass

def p_exp9(p):
  '''exp9 : exp9 SUB exp10
          | exp10'''
  pass

def p_exp10(p):
  '''exp10 : exp10 MAIOR exp11
           | exp11'''
  pass

def p_exp11(p):
  '''exp11 : exp11 MENOR exp12
           | exp12'''
  pass

def p_exp12(p):
  '''exp12 : exp12 MAIORIGUAL exp13
           | exp13'''
  pass

def p_exp13(p):
  '''exp13 : exp13 MENORIGUAL exp14
           | exp14'''
  pass

def p_exp14(p):
  '''exp14 : exp14 IGUAL exp15
           | exp15'''
  pass

def p_exp15(p):
  '''exp15 : exp15 AND exp16
           | exp15 OREXCLUSIVO exp16
           | exp15 ORINCLUSIVO exp16
           | exp16'''
  pass

def p_exp16(p):
  '''exp16 : chamadaF
           | VAR
           | INT
           | FLOAT
           | BOOL
           | ID
           | LPAREN expressao RPAREN'''
  pass


def p_atribuir(p):
  '''atribuir : VAR ATRIBUICAO expressao'''
  pass

def p_chamadaF(p): #chamada de função
  '''chamadaF : ID LPAREN parametros RPAREN
              | ID LPAREN RPAREN'''
  pass

def p_parametros(p):
  '''parametros : expressao VIRGULA parametros
                | expressao'''
  pass
