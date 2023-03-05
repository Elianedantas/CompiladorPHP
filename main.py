import ply.lex as lex

reservadas = {
  'abstract': 'ABSTRACT',
  'and': 'AND',
  'break': 'BREAK',
  'case': 'CASE',
  'class': 'CLASS',
  'clone': 'CLONE',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'declare': 'DECLARE',
  'default': 'DEFAULT',
  'die': 'DIE',
  'do': 'DO',
  'echo': 'ECHO',
  'else': 'ELSE',
  'empty': 'EMPTY',
  'endif': 'ENDIF',
  'endwhile': 'ENDWHILE',
  'endfor': 'ENDFOR',
  'endforeach': 'ENDFOREACH',
  'endswitch': 'ENDSWITCH',
  'eval': 'EVAL',
  'exit': 'EXIT',
  'extends': 'EXTENDS',
  'false': 'FALSE',
  'final': 'FINAL',
  'for': 'FOR',
  'foreach': 'FOREACH',
  'function': 'FUNCTION',
  'global': 'GLOBAL',
  'goto': 'GOTO',
  'if': 'IF',
  'implements': 'IMPLEMENTS',
  'include': 'INCLUDE',
  'include_once': 'INCLUDE_ONCE',
  'instanceof': 'INSTANCEOF',
  'interface': 'INTERFACE',
  'isset': 'ISSET',
  'list': 'LIST',
  'match': 'MATCH',
  'namespace': 'NAMESPACE',
  'new': 'NEW',
  'null': 'NULL',
  'or': 'OR',
  'print': 'PRINT',
  'private': 'PRIVATE',
  'protected': 'PROTECTED',
  'public': 'PUBLIC',
  'require': 'REQUIRE',
  'require_once': 'REQUIRE_ONCE',
  'return': 'RETURN',
  'static': 'STATIC',
  'switch': 'SWITCH',
  'this': 'THIS',
  'throw': 'THROW',
  'traits': 'TRAITS',
  'true': 'TRUE',
  'unset': 'UNSET',
  'while': 'WHILE',
  'xor': 'XOR',
  'yield': 'YIELD'
}
tokens = [
  'IGUAL', 'SOMA', 'SUB', 'MULTI', 'DIVISAO', 'MODULO', 'POT',
  'LPAREN', 'RPAREN', 'VIRGULA', 'LCHAV', 'RCHAV', 'PV', 'AND1', 'ORINCLUSIVO',
  'OREXCLUSIVO', 'NOT', 'LDES', 'RDES', 'VARIAVEL', 'INT', 'FLOAT', 'MENOR',
  'MAIOR', 'DIF_IGUAL', 'MIGUAL', 'MMAIOR', 'ERRO', 'COMENT'
] + list(reservadas.values())

t_IGUAL = r'='
t_SOMA = r'\+'
t_SUB = r'-'
t_MULTI = r'\*'
t_DIVISAO = r'/'
t_MODULO = r'%'
t_POT = r'[**]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VIRGULA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'
t_AND1 = r'&'
t_ORINCLUSIVO = r'\|'
t_OREXCLUSIVO = r'\^'
t_NOT = r'~'
t_LDES = r'<<'
t_RDES = r'>>'
t_MENOR = r'<'
t_MIGUAL = r'<='
t_MAIOR = r'>'
t_MMAIOR = r'>='
t_DIF_IGUAL = r'\!='
t_ERRO = r'@'
t_COMENT = r'[#][a-zA-Z0-9 ]*'


def t_VARIAVEL(t):
  r'[$][a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reservadas.get(t.value, 'VARIAVEL')
  return t


def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_FLOAT(t):
  r'[0-9.]+[.]*'
  t.value = float(t.value)
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


lex.lex()
programa = """<?php
for ($i = 1; $i <= 10; $i++) {
  if ($i == 2 & $i > 3){
    echo "teste";
  }
  echo $i;
  echo "\n";
}"""
lex.input(programa)
for tok in lex.lexer:
  print(tok.value)
