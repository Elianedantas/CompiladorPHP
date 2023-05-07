import ply.lex as lex


def space_counter(token):
  spaces = 0
  for c in token.value:
    if c == ' ':
      spaces += 1
    elif c == '\t':
      spaces += 8 - (spaces % 8)
  return spaces


reservadas = {
  'break': 'BREAK',
  'case': 'CASE',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'declare': 'DECLARE',
  'default': 'DEFAULT',
  'do': 'DO',
  'echo': 'ECHO',
  'else': 'ELSE',
  'empty': 'EMPTY',
  'endif': 'ENDIF',
  'endwhile': 'ENDWHILE',
  'endfor': 'ENDFOR',
  'endforeach': 'ENDFOREACH',
  'endswitch': 'ENDSWITCH',
  'exit': 'EXIT',
  'for': 'FOR',
  'foreach': 'FOREACH',
  'global': 'GLOBAL',
  'goto': 'GOTO',
  'if': 'IF',
  'implements': 'IMPLEMENTS',
  'include': 'INCLUDE',
  'include_once': 'INCLUDE_ONCE',
  'isset': 'ISSET',
  'list': 'LIST',
  'match': 'MATCH',
  'namespace': 'NAMESPACE',
  'null': 'NULL',
  'print': 'PRINT',
  'private': 'PRIVATE',
  'protected': 'PROTECTED',
  'public': 'PUBLIC',
  'return': 'RETURN',
  'static': 'STATIC',
  'switch': 'SWITCH',
  'throw': 'THROW',
  'traits': 'TRAITS',
  'unset': 'UNSET',
  'while': 'WHILE',
  'yield': 'YIELD'
}
tokens = [
  'INICIO', 'FIM', 'ATRIBUICAO', 'SOMA', 'SUB', 'MULTI', 'DIVISAO', 'MODULO',
  'POT', 'LPAREN', 'RPAREN', 'LCHAV', 'RCHAV', 'VIRGULA', 'PONTOVIRGULA',
  'AND', 'OR', 'NOT', 'MENOR', 'MAIOR', 'MENORIGUAL',
  'MAIORIGUAL', 'DIFERENTE', 'IGUAL', 'IDENTICO', 'NAOIDENTICO', 'INCREMENTA',
  'DECREMENTA', 'ERRO', 'BOOL', 'INT', 'FLOAT', 'STRING', 'ID', 'VAR', 'COMENT'
] + list(reservadas.values())

# stack = [0]
# states = (('idstate', 'exclusive'), ('dedstate', 'exclusive'))

t_INICIO = r'\<\?php'
t_FIM = r'\?\>'
t_ATRIBUICAO = r'='
t_SOMA = r'\+'
t_SUB = r'-'
t_MULTI = r'\*'
t_DIVISAO = r'/'
t_MODULO = r'%'
t_POT = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAV = r'{'
t_RCHAV = r'}'
t_VIRGULA = r','
t_PONTOVIRGULA = r';'
t_AND = r'(&&)|(&)|(and)'
t_OR = r'(\|\|)|(\|)|(or)'
t_NOT = r'!'
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENORIGUAL = r'<='
t_MAIORIGUAL = r'>='
t_DIFERENTE = r'(!=)|(<>)'
t_IGUAL = r'=='
t_IDENTICO = r'==='
t_NAOIDENTICO = r'!=='
t_INCREMENTA = r'\+\+'
t_DECREMENTA = r'--'
t_ERRO = r'@'
t_BOOL = r'(true)|(false)'


def t_breakline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  # t.lexer.begin('idstate')


# def t_idstate_blankline(t):
#   r'([ \t]+)\n'
#   pass

# def t_idstate_linewithcode(t):
#   '([ \t]+) | ([a-zA-Z])'
#   n_spaces = space_counter(t)
#   t.lexer.begin('INITIAL')
#   if n_spaces < stack[-1]:
#     t.lexer.skip(-len(t.value))
#     stack.pop()
#     t.type = 'DEDENT'
#     t.lexer.begin('dedstate')
#   elif n_spaces > stack[-1]:
#     stack.append(n_spaces)
#     t.type = 'IDENT'
#   elif n_spaces == 0:
#     t.lexer.skip(-1)

# def t_dedstate_linewithdedent(t):
#   '([ \t]+) | ([a-zA-Z])'
#   n_spaces = space_counter(t)
#   if n_spaces < stack[-1]:
#     t.lexer.skip(-len(t.value))
#     stack.pop()
#     t.type = 'DEDENT'
#     return t
#   elif n_spaces >= stack[-1]:
#     t.lexer.begin('INITIAL')
#     if n_spaces > stack[-1]:
#       print('Erro de dedentação --->', n_spaces)
#     elif n_spaces == 0:
#       t.lexer.skip(-1)

# def t_idstate_error(t):
#   t.lexer.skip(1)

# def t_dedstate_error(t):
#   t.lexer.skip(1)


def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_FLOAT(t):
  r'[0-9.]+[.]*'
  t.value = float(t.value)
  return t


def t_STRING(t):
  r'(\"([^\\]|(\\.))*?\") | (\'([^\\]|(\\.))*?\')'
  return t


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reservadas.get(t.value, 'ID')
  return t


def t_VAR(t):
  r'[$][a-zA-Z_][a-zA-Z_0-9]*'
  return t


def t_COMENT(t):
  r'(//.*)|(\#.*)|(/\*(.|\n)*?\*/)'
  pass


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  #print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


lex.lex()
programa = """<?php
    $a = 3;
?>
"""

lex.input(programa)
if __name__ == "__main__":
  for token in lex.lexer:
    print(token.type, token.value)
