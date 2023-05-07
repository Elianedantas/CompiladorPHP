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
    pass
    #functionorcmds_function.function.accept(self)
 
  def visitFunctionOrCmds_CmdFun(self, functionorcmds_cmdfun):
    pass
    #functionorcmds_cmdfun.comando.accept(self)
    #functionorcmds_cmdfun.functionorcmds.accept(self)
  
  def visitFunctionOrCmds_FunctionFunc(self, functionorcmds_functionfunc):
    pass
    #functionorcmds_functionfunc.function.accept(self)
    #functionorcmds_functionfunc.functionorcmds.accept(self)

  
  #comando
  def visitCmd_Var(self, cmd_var):
    cmd_var.atribuir.accept(self)
  
  def visitICmd_Exp(self, cmd_exp):
    pass
    #cmd_exp.expressao.accept(self)
    #print(';')
  
  def visitCmd_Return(self, cmd_return):
    pass
  
  def visitCmd_IfElse(self, cmd_ifelse):
    pass
  
  def visitCmd_If(self, cmd_if):
    pass
  
  def visitCmd_For(self, cmd_for):
    pass
  
  def visitCmd_While(self, cmd_while):
    pass

  #Lista de comandos
  def visitLst_Cmd(self, lst_cmdself):
    pass
  
  def visitLst_ListaCmd(self, lst_listacmd):
    pass

  #function
  def visitFuncDec(self, funcdec):
    pass  
  
  #atribuir
  def visitAtribuirVar(self, atribuirvar):
    print(atribuirvar.var, end='')
    print(' = ', end='')
    print(atribuirvar.exp, end='')
#    atribuirvar.exp.accept(self)
    print(';')

  #chamadaFunc
  def visitChamadaFunction(self, chamadafunction):
    pass

  #parametros
  def visitParam_Unico(self, param_unico):
    pass

  def visitParam_Composto(self, param_composto):
    pass


  #expressao
  def visitPotExp(self, potexp):
    pass
    #potexp.exp.accept(self)
    #print(' ** ', end='')
    #potexp.exp2.accept(self)

  def visitIncrementExp(self, incrementexp):
    pass

  def visitDecrementExp(self, decrementexp):
    pass

  def visitNotExp(self, notexp):
    pass

  def visitSomaExp(self, somaexp):
    pass
#    somaexp.exp5.accept(self)
#    print(' + ', end='')
#    somaexp.exp6.accept(self)

  def visitSubExp(self, subexp):
    pass

  def visitMulExp(self, mulexp):
    pass

  def visitDivExp(self, divexp):
    pass

  def visitModuloExp(self, moduloexp):
    pass

  def visitMaiorExp(self, maiorexp):
    pass

  def visitMenorExp(self, menorexp):
    pass

  def visitMaiorIgualExp(self, maiorigualexp):
    pass

  def visitMenorIgualExp(self, menorigualexp):
    pass

  def visitIgualExp(self, igualexp):
    pass

  def visitDifExp(self, difexp):
    pass

  def visitAndExp(self, andexp):
    pass

  def visitOrExp(self, orexp):
    pass

  def visitChamadaFuncExp(self, chamadafuncexp):
    pass

  def visitVarExp(self, varexp):
    pass
    #print(varexp.var, end='')

  def visitIntExp(self, intexp):
    pass
    #print(intexp.int, end='')

  def visitFloatExp(self, floatexp):
    pass
    #print(floatexp.float, end='')

  def visitBoolExp(self, boolexp):
    pass
    #print(boolexp.bool, end='')

  def visitIdExp(self, idexp):
    pass
    #print(idexp.ID, end='')

  def visitExpressaoExp(self, expressaoexp):
    pass
    #print('(', end='')
    #print(expressaoexp.exp, end='')
    #print(')', end='')
 