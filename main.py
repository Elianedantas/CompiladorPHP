from sintatico import *

parser = yacc.yacc()
yacc.parse(debug=True)