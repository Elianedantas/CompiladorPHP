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
  'function': 'FUNCTION',
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
  'MAIORIGUAL', 'DIFERENTE', 'IGUAL', 'INCREMENTA',
  'DECREMENTA', 'BOOL', 'INT', 'FLOAT', 'STRING', 'ID', 'VAR', 'COMENT'
] + list(reservadas.values())

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
t_INCREMENTA = r'\+\+'
t_DECREMENTA = r'--'
t_BOOL = r'(true)|(false)'

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
  $a = 34;
  $b=1;
  $c=3;
  if($a==5){
    $a=3;
  }
  for ($i=0;$i<3;$i++){
    $a=1;
  }
  if($b==1 && $c==3){
    $a=10;
  }
?>
"""

lex.input(programa)
if __name__ == "__main__":
  for token in lex.lexer:
    print(token.type, token.value)
