from abc import abstractmethod
from abc import ABCMeta

class Visitor(metaclass=ABCMeta):
  #programa
  @abstractmethod
  def visitProgramaFC(self, programafc):
    pass
  
  #functionorcmds
  @abstractmethod
  def visitFunctionOrCmds_Cmd(self, functionorcmds_cmd):
    pass
  
  @abstractmethod
  def visitFunctionOrCmds_Function(self, functionorcmds_function):
    pass
  
  @abstractmethod
  def visitFunctionOrCmds_CmdFun(self, functionorcmds_cmdfun):
    pass
    
  @abstractmethod
  def visitFunctionOrCmds_FunctionFunc(self, functionorcmds_functionfunc):
    pass
 
  #comando
  @abstractmethod
  def visitCmd_Var(self, cmd_var):
    pass
    
  @abstractmethod
  def visitICmd_Exp(self, cmd_exp):
    pass
    
  @abstractmethod
  def visitCmd_Return(self, cmd_return):
    pass
    
  @abstractmethod
  def visitCmd_IfElse(self, cmd_ifelse):
    pass
  
  @abstractmethod
  def visitCmd_If(self, cmd_if):
    pass
    
  @abstractmethod
  def visitCmd_For(self, cmd_for):
    pass
    
  @abstractmethod
  def visitCmd_While(self, cmd_while):
    pass

  #Lista de comandos
  @abstractmethod
  def visitLst_Cmd(self, lst_cmdself):
    pass
  
  @abstractmethod
  def visitLst_ListaCmd(self, lst_listacmd):
    pass

  #function
  @abstractmethod
  def visitFuncDec(self, funcdec):
    pass
  
  #atribuir
  @abstractmethod
  def visitAtribuirVar(self, atribuirvar):
    pass

  #chamadaFunc
  @abstractmethod
  def visitChamadaFunction(self, chamadafunction):
    pass

  #parametros
  @abstractmethod
  def visitParam_Unico(self, param_unico):
    pass

  @abstractmethod
  def visitParam_Composto(self, param_composto):
    pass

  #expressao
  @abstractmethod
  def visitPotExp(self, potexp):
    pass

  @abstractmethod
  def visitIncrementExp(self, incrementexp):
    pass

  @abstractmethod
  def visitDecrementExp(self, decrementexp):
    pass

  @abstractmethod
  def visitNotExp(self, notexp):
    pass

  @abstractmethod
  def visitSomaExp(self, somaexp):
    pass

  @abstractmethod
  def visitSubExp(self, subexp):
    pass

  @abstractmethod
  def visitMulExp(self, mulexp):
    pass

  @abstractmethod
  def visitDivExp(self, divexp):
    pass

  @abstractmethod
  def visitModuloExp(self, moduloexp):
    pass

  @abstractmethod
  def visitMaiorExp(self, maiorexp):
    pass

  @abstractmethod
  def visitMenorExp(self, menorexp):
    pass

  @abstractmethod
  def visitMaiorIgualExp(self, maiorigualexp):
    pass

  @abstractmethod
  def visitMenorIgualExp(self, menorigualexp):
    pass

  @abstractmethod
  def visitIgualExp(self, igualexp):
    pass

  @abstractmethod
  def visitDifExp(self, difexp):
    pass

  @abstractmethod
  def visitAndExp(self, andexp):
    pass

  @abstractmethod
  def visitOrExp(self, orexp):
    pass

  @abstractmethod
  def visitChamadaFuncExp(self, chamadafuncexp):
    pass

  @abstractmethod
  def visitVarExp(self, varexp):
    pass

  @abstractmethod
  def visitIntExp(self, intexp):
    pass

  @abstractmethod
  def visitFloatExp(self, floatexp):
    pass

  @abstractmethod
  def visitBoolExp(self, boolexp):
    pass

  @abstractmethod
  def visitIdExp(self, idexp):
    pass

  @abstractmethod
  def visitExpressaoExp(self, expressaoexp):
    pass
 