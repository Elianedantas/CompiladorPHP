#import SymbolTable as st
from visitor import *

def coercion(tipo1, tipo2):
  if (tipo1 in st.Number and tipo2 in st.Number):
    if (tipo1 == st.FLOAT or tipo2 == st.FLOAT):
      return st.FLOAT
    else:
      return st.INT
  else:
    return None

class SemanticVisitor(Visitor):
  def visitSomaExp(self, somaexp):
    tipoExp1 = somaexp.exp1.accept(self)
    tipoExp2 = somaexp.exp2.accept(self)
    c = coercion(tipoExp1, tipoExp2)
    if (c == None):
        somaexp.accept(self.printer)
        print('\n\t[Erro] Soma invalida. A expressao ', end='')
        somaexp.exp1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        somaexp.exp2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
    return c
  
  def visitSubExp(self, subexp):
    tipoExp1 = subexp.exp1.accept(self)
    tipoExp2 = subexp.exp2.accept(self)
    c = coercion(tipoExp1, tipoExp2)
    if (c == None):
        subexp.accept(self.printer)
        print('\n\t[Erro] Subtração invalida. A expressao ', end='')
        subexp.exp1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        subexp.exp2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
    return c
  
  def visitDivExp(self, divexp):
    tipoExp1 = divexp.exp1.accept(self)
    tipoExp2 = divexp.exp2.accept(self)
    c = coercion(tipoExp1, tipoExp2)
    if (c == None):
        divexp.accept(self.printer)
        print('\n\t[Erro] Multiplicação invalida. A expressao ', end='')
        divexp.exp1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        divexp.exp2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
    return c
  
  def visitMulExp(self, mulexp):
    tipoExp1 = mulexp.exp1.accept(self)
    tipoExp2 = mulexp.exp2.accept(self)
    c = coercion(tipoExp1, tipoExp2)
    if (c == None):
        mulexp.accept(self.printer)
        print('\n\t[Erro] Multiplicação invalida. A expressao ', end='')
        mulexp.exp1.accept(self.printer)
        print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
        mulexp.exp2.accept(self.printer)
        print(' eh do tipo', tipoExp2,'\n')
    return c

