import ply.yacc as yacc
from lexico import *
from sintaxeabstrata import *


def p_programa(p):
  '''programa : INICIO functionorcmds FIM
              | INICIO functionorcmds'''
  if (len(p) == 4):
    p[0] = ProgramaFC(p[1], p[2], p[3])
  else:
    p[0] = ProgramaFC(p[1], p[2], None)


def p_functionorcmds(p):
  '''functionorcmds : comando
                    | function
                    | comando functionorcmds
                    | function functionorcmds'''
  if (len(p) == 2):
    if (isinstance(p[1], Comando)):
      p[0] = FunctionOrCmds_Cmd(p[1])
    else:
      p[0] = FunctionOrCmds_Function(p[1])
  else:
    if (isinstance(p[1], Comando)):
      p[0] = FunctionOrCmds_CmdFun(p[1], p[2])
    else:
      p[0] = FunctionOrCmds_FunctionFunc(p[1], p[2])


def p_comando(p):
  '''comando : atribuir
             | exp PONTOVIRGULA
             | RETURN exp PONTOVIRGULA
             | IF LPAREN exp RPAREN LCHAV listadecomandos RCHAV ELSE LCHAV listadecomandos RCHAV
             | IF LPAREN exp RPAREN LCHAV listadecomandos RCHAV
             | FOR LPAREN atribuir exp PONTOVIRGULA exp RPAREN LCHAV listadecomandos RCHAV
             | WHILE LPAREN exp RPAREN LCHAV listadecomandos RCHAV'''
  if (len(p) == 2):
    p[0] = Cmd_Var(p[1])
  elif (len(p) == 3):
    p[0] = Cmd_Exp(p[1])
  elif (len(p) == 4):
    p[0] = Cmd_Return(p[2])
  elif (p[1] == 'if'):
    if (len(p) == 12):
      p[0] = Cmd_IfElse(p[3], p[6], p[10])
    else:
      p[0] = Cmd_If(p[3], p[6])
  elif (p[1] == 'for'):
    p[0] = Cmd_For(p[3], p[4], p[6], p[9])
  elif (p[1] == 'while'):
    p[0] = Cmd_While(p[3], p[6])


def p_listadecomandos(p):
  '''listadecomandos : comando
                     | listadecomandos comando'''
  if (len(p) == 3):
    p[0] = Lst_ListaCmd(p[1], p[2])
  else:
    p[0] = Lst_Cmd(p[1])


def p_function(p):
  '''function : FUNCTION ID LPAREN parametros RPAREN LCHAV listadecomandos RCHAV
              | FUNCTION ID LPAREN RPAREN LCHAV listadecomandos RCHAV'''
  if (isinstance(p[4], Parametros)):
    p[0] = FuncDec(p[2], p[4], p[7])
  else:
    p[0] = FuncDec(p[2], None, p[6])


def p_atribuir(p):
  '''atribuir : VAR ATRIBUICAO exp PONTOVIRGULA'''
  p[0] = AtribuirVar(p[1], p[3])


def p_chamadaFunc(p): #chamada de função
  '''chamadaFunc : ID LPAREN parametros RPAREN
                 | ID LPAREN RPAREN'''
  if (isinstance(p[3], Parametros)):
    p[0] = ChamadaFunctionCallF(p[1], p[3])
  else:
    p[0] = ChamadaFunctionCallF(p[1], None)


def p_parametros(p):
  '''parametros : VAR VIRGULA parametros
                | VAR'''
  if (len(p) == 2):
    p[0] = Param_Unico(p[1])
  else:
    p[0] = Param_Composto(p[1], p[3])


def p_exp(p):
  '''exp : exp POT exp2
         | exp2'''
  if (len(p) == 4):
    # n ta reconhecendo os parametros
    p[0] = PotExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp2(p):
  '''exp2 : exp2 INCREMENTA
          | exp3'''
  if (len(p) == 3):
    p[0] = IncrementExp(p[1])
  else:
    p[0] = p[1]


def p_exp3(p):
  '''exp3 : exp3 DECREMENTA
          | exp4'''
  if (len(p) == 3):
    p[0] = DecrementExp(p[1])
  else:
    p[0] = p[1]


def p_exp4(p):
  '''exp4 : NOT exp5
          | exp5'''
  if (len(p) == 3):
    p[0] = NotExp(p[2])
  else:
    p[0] = p[1]


def p_exp5(p):
  '''exp5 : exp5 SOMA exp6
          | exp6'''
  if (len(p) == 4):
    p[0] = SomaExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp6(p):
  '''exp6 : exp6 SUB exp7
          | exp7'''
  if (len(p) == 4):
    p[0] = SubExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp7(p):
  '''exp7 : exp7 MULTI exp8
          | exp8'''
  if (len(p) == 4):
    p[0] = MulExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp8(p):
  '''exp8 : exp8 DIVISAO exp9
          | exp9'''
  if (len(p) == 4):
    p[0] = DivExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp9(p):
  '''exp9 : exp9 MODULO exp10
          | exp10'''
  if (len(p) == 4):
    p[0] = ModuloExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp10(p):
  '''exp10 : exp10 MAIOR exp11
           | exp11'''
  if (len(p) == 4):
    p[0] = MaiorExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp11(p):
  '''exp11 : exp11 MENOR exp12
           | exp12'''
  if (len(p) == 4):
    p[0] = MenorExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp12(p):
  '''exp12 : exp12 MAIORIGUAL exp13
           | exp13'''
  if (len(p) == 4):
    p[0] = MaiorIgualExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp13(p):
  '''exp13 : exp13 MENORIGUAL exp14
           | exp14'''
  if (len(p) == 4):
    p[0] = MenorIgualExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp14(p):
  '''exp14 : exp14 IGUAL exp15
           | exp15'''
  if (len(p) == 4):
    p[0] = IgualExp(p[1], p[3])
  else:
    p[0] = p[1]

def p_exp15(p):
  '''exp15 : exp15 DIFERENTE exp16
           | exp16'''
  if (len(p) == 4):
    p[0] = DifExp(p[1], p[3])
  else:
    p[0] = p[1]

def p_exp16(p):
  '''exp16 : exp16 AND exp17
           | exp16 OR exp17
           | exp17'''
  if (len(p) > 2):
    if (p[2] == '&&' or p[2] == '&' or p[2] == 'and'):
      p[0] = AndExp(p[1], p[3])
    elif (p[2] == '||' or p[2] == '|' or p[2] == 'or'):
      p[0] = OrExp(p[1], p[3])
  else:
    p[0] = p[1]


def p_exp17(p):
  '''exp17 : chamadaFunc
           | VAR
           | INT
           | FLOAT
           | BOOL
           | ID
           | LPAREN exp RPAREN'''

  if (isinstance(p[1], int)):
    p[0] = IntExp(p[1])
  elif (len(p) == 4):
    p[0] = ExpressaoExp(p[2])
  elif (isinstance(p[1], float)):
    p[0] = FloatExp(p[1])
  elif (p[1] == 'true' or p[1] == 'false'):
    p[0] = BoolExp(p[1])
  elif (p[1][0] == '$'):
    p[0] = VarExp(p[1])
  elif (isinstance(p[1], ChamadaFunction)):
    p[0] = CallFuncExp(p[1])
  else:
    p[0] = IdExp(p[1])
