from sintatica import *

parser = yacc.yacc()
yacc.parse(debug=True)