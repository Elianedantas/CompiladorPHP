from visitor import *
from sintatico import *

class VisitorPrinter(Visitor):
  #programa
  def visitProgramaFC(self, programafc):
    print(programafc.inicio)
    programafc.functionorcmd.accept(self)
    if (programafc.fim != None):
      print(programafc.fim)
  
  #functionorcmds
  def visitFunctionOrCmds_Cmd(self, functionorcmds_cmd):
    functionorcmds_cmd.comando.accept(self)
  
  def visitFunctionOrCmds_Function(self, functionorcmds_function):
    functionorcmds_function.function.accept(self)
 
  def visitFunctionOrCmds_CmdFun(self, functionorcmds_cmdfun):
    functionorcmds_cmdfun.comando.accept(self)
    functionorcmds_cmdfun.functionorcmds.accept(self)
  
  def visitFunctionOrCmds_FunctionFunc(self, functionorcmds_functionfunc):
    functionorcmds_functionfunc.function.accept(self)
    functionorcmds_functionfunc.functionorcmds.accept(self)

  
  #comando
  def visitCmd_Var(self, cmd_var):
    cmd_var.atribuir.accept(self)
    print(end='\n')
  
  def visitICmd_Exp(self, cmd_exp):
    cmd_exp.expressao.accept(self)
    print(';')
  
  def visitCmd_Return(self, cmd_return):
    print("return", end='')
    cmd_return.expressao.accept(self)
    print(';')
  
  def visitCmd_IfElse(self, cmd_ifelse):
    print("if (", end='')
    cmd_ifelse.expressao.accept(self)
    print(") {")
    cmd_ifelse.listadecomandos.accept(self)
    print("} else {")
    cmd_ifelse.listadecomandos2.accept(self)
    print("}")
  
  def visitCmd_If(self, cmd_if):
    print("if (", end='')
    cmd_if.expressao.accept(self)
    print(") {")
    cmd_if.listadecomandos.accept(self)
    print("}")
  
  def visitCmd_For(self, cmd_for):
    print("for (", end='')
    cmd_for.atribuir.accept(self)
    cmd_for.expressao.accept(self)
    print(';', end='')
    cmd_for.expressao2.accept(self)
    print(') {')
    cmd_for.listadecomandos.accept(self)
    print('}')
  
  def visitCmd_While(self, cmd_while):
    print('while (', end='')
    cmd_while.expressao.accept(self)
    print(') {')
    cmd_while.listadecomandos.accept(self)
    print('}')

  #Lista de comandos
  def visitLst_Cmd(self, lst_cmd):
    lst_cmd.comando.accept(self)
  
  def visitLst_ListaCmd(self, lst_listacmd):
    lst_listacmd.listadecomandos.accept(self)
    lst_listacmd.comando.accept(self)

  #function
  def visitFuncDec(self, funcdec):
    print('function ', end='')
    print(funcdec.ID, end='')
    print('(', end='')
    if (funcdec.parametros != None):
      funcdec.parametros.accept(self)
    print(') {', end='')
    funcdec.listadecomandos.accept(self)
    print('}')
    
  #atribuir
  def visitAtribuirVar(self, atribuirvar):
    print(atribuirvar.var, end='')
    print(' = ', end='')
    atribuirvar.exp.accept(self)
    print(';', end='')

  #chamadaFunc
  def visitChamadaFunction(self, chamadafunction):
    print(chamadafunction.ID, ' (')
    if (chamadafunction.parametros != None):
      chamadafunction.parametros.accept(self)
    print(')')

  #parametros
  def visitParam_Unico(self, param_unico):
    print(param_unico.var, end='')

  def visitParam_Composto(self, param_composto):
    print(param_composto.var, ', ', end='')
    param_composto.parametros.accept(self)


  #expressao
  def visitPotExp(self, potexp):
    potexp.exp.accept(self)
    print(' ** ', end='')
    potexp.exp2.accept(self)

  def visitIncrementExp(self, incrementexp):
    incrementexp.exp2.accept(self)
    print('++', end='')

  def visitDecrementExp(self, decrementexp):
    decrementexp.exp3.accept(self)
    print('--', end='')

  def visitNotExp(self, notexp):
    print('!', end='')
    notexp.exp5.accept(self)

  def visitSomaExp(self, somaexp):
    somaexp.exp5.accept(self)
    print(' + ', end='')
    somaexp.exp6.accept(self)

  def visitSubExp(self, subexp):
    subexp.exp5.accept(self)
    print(' - ', end='')
    subexp.exp6.accept(self)

  def visitMulExp(self, mulexp):
    mulexp.exp5.accept(self)
    print(' * ', end='')
    mulexp.exp6.accept(self)

  def visitDivExp(self, divexp):
    divexp.exp5.accept(self)
    print(' / ', end='')
    divexp.exp6.accept(self)

  def visitModuloExp(self, moduloexp):
    moduloexp.exp5.accept(self)
    print(' % ', end='')
    moduloexp.exp6.accept(self)

  def visitMaiorExp(self, maiorexp):
    maiorexp.exp5.accept(self)
    print(' > ', end='')
    maiorexp.exp6.accept(self)

  def visitMenorExp(self, menorexp):
    menorexp.exp5.accept(self)
    print(' < ', end='')
    menorexp.exp6.accept(self)

  def visitMaiorIgualExp(self, maiorigualexp):
    maiorigualexp.exp5.accept(self)
    print(' >= ', end='')
    maiorigualexp.exp6.accept(self)

  def visitMenorIgualExp(self, menorigualexp):
    menorigualexp.exp5.accept(self)
    print(' <= ', end='')
    menorigualexp.exp6.accept(self)

  def visitIgualExp(self, igualexp):
    igualexp.exp5.accept(self)
    print(' == ', end='')
    igualexp.exp6.accept(self)

  def visitDifExp(self, difexp):
    difexp.exp5.accept(self)
    print(' != ', end='')
    difexp.exp6.accept(self)

  def visitAndExp(self, andexp):
    andexp.exp5.accept(self)
    print(' && ', end='')
    andexp.exp6.accept(self)

  def visitOrExp(self, orexp):
    orexp.exp5.accept(self)
    print(' || ', end='')
    orexp.exp6.accept(self)

  def visitChamadaFuncExp(self, chamadafuncexp):
    chamadafuncexp.chamadaFunc.accept(self)

  def visitVarExp(self, varexp):
    print(varexp.var, end='')

  def visitIntExp(self, intexp):
    print(intexp.int, end='')

  def visitFloatExp(self, floatexp):
    print(floatexp.float, end='')

  def visitBoolExp(self, boolexp):
    print(boolexp.bool, end='')

  def visitIdExp(self, idexp):
    print(idexp.ID, end='')

  def visitExpressaoExp(self, expressaoexp):
    print('(', end='')
    print(expressaoexp.exp, end='')
    print(')', end='')
 