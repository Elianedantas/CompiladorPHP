from visitorPrinter import *
from sintatico import *

#parser = yacc.yacc()
#yacc.parse(debug=True)

# Testando visitorprinter
sint = yacc.yacc()
tree = sint.parse(debug = True)

vp = VisitorPrinter()
tree.accept(vp)
print('')