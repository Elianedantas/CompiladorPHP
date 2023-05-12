from abc import abstractmethod
from abc import ABCMeta


#programa
class Programa(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ProgramaFC(Programa):
  def __init__(self, inicio, functionorcmd, fim):
    self.inicio = inicio
    self.functionorcmd = functionorcmd
    self.fim = fim
  def accept(self, visitor):
    return visitor.visitProgramaFC(self)


#functionorcmds
class FunctionOrCmds(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class FunctionOrCmds_Cmd(FunctionOrCmds):
  def __init__(self, comando):
    self.comando = comando
  def accept(self, visitor):
    return visitor.visitFunctionOrCmds_Cmd(self)

class FunctionOrCmds_Function(FunctionOrCmds):
  def __init__(self, function):
    self.function = function
  def accept(self, visitor):
    return visitor.visitFunctionOrCmds_Function(self)

class FunctionOrCmds_CmdFun(FunctionOrCmds):
  def __init__(self, comando, functionorcmds):
    self.comando = comando
    self.functionorcmds = functionorcmds
  def accept(self, visitor):
    return visitor.visitFunctionOrCmds_CmdFun(self)

class FunctionOrCmds_FunctionFunc(FunctionOrCmds):
  def __init__(self, function, functionorcmds):
    self.function = function
    self.functionorcmds = functionorcmds
  def accept(self, visitor):
    return visitor.visitFunctionOrCmds_FunctionFunc(self)


#comando
class Comando(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Cmd_Var(Comando):
  def __init__(self, atribuir):
    self.atribuir = atribuir
  def accept(self, visitor):
    return visitor.visitCmd_Var(self)

class Cmd_Exp(Comando):
  def __init__(self, expressao):
    self.expressao = expressao
  def accept(self, visitor):
    return visitor.visitCmd_Exp(self)

class Cmd_Return(Comando):
  def __init__(self, expressao):
    self.expressao = expressao
  def accept(self, visitor):
    return visitor.visitCmd_Return(self)

class Cmd_IfElse(Comando):
  def __init__(self, expressao, listadecomandos, listadecomandos2):
    self.expressao = expressao
    self.listadecomandos = listadecomandos
    self.listadecomandos2 = listadecomandos2
  def accept(self, visitor):
    return visitor.visitCmd_IfElse(self)

class Cmd_If(Comando):
  def __init__(self, expressao, listadecomandos):
    self.expressao = expressao
    self.listadecomandos = listadecomandos
  def accept(self, visitor):
    return visitor.visitCmd_If(self)

class Cmd_For(Comando):
  def __init__(self, atribuir, expressao, expressao2, listadecomandos):
    self.atribuir = atribuir
    self.expressao = expressao
    self.expressao2 = expressao2
    self.listadecomandos = listadecomandos
  def accept(self, visitor):
    return visitor.visitCmd_For(self)

class Cmd_While(Comando):
  def __init__(self, expressao, listadecomandos):
    self.expressao = expressao
    self.listadecomandos = listadecomandos
  def accept(self, visitor):
    return visitor.visitCmd_While(self)


#listadecomandos
class ListaDeComandos(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Lst_Cmd(ListaDeComandos):
  def __init__(self, comando):
    self.comando = comando
  def accept(self, visitor):
    return visitor.visitLst_Cmd(self)

class Lst_ListaCmd(ListaDeComandos):
  def __init__(self, listadecomandos, comando):
    self.listadecomandos = listadecomandos
    self.comando = comando
  def accept(self, visitor):
    return visitor.visitLst_ListaCmd(self)


#function
class Function(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class FuncDec(Function):
  def __init__(self, ID, parametros, listadecomandos):
    self.ID = ID
    self.parametros = parametros
    self.listadecomandos = listadecomandos
  def accept(self, visitor):
    return visitor.visitFuncDec(self)


#atribuir
class Atribuir(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
 
class AtribuirVar(Atribuir):
  def __init__(self, var, exp):
    self.var = var
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitAtribuirVar(self)


#chamadaFunc
class ChamadaFunction(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ChamadaFunctionCallF(ChamadaFunction):
  def __init__(self, ID, parametros):
    self.ID = ID
    self.parametros = parametros
  def accept(self, visitor):
    return visitor.visitChamadaFunctionCallF(self)


#parametros
class Parametros(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Param_Unico(Parametros):
  def __init__(self, var):
    self.var = var
  def accept(self, visitor):
    return visitor.visitParam_Unico(self)

class Param_Composto(Parametros):
  def __init__(self, var, parametros):
    self.var = var
    self.parametros = parametros
  def accept(self, visitor):
    return visitor.visitParam_Composto(self)


#expressão
class Exp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class PotExp(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitPotExp(self)

#Exp2 Incrementa
class IncrementExp(Exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitIncrementExp(self)


#Exp3 Decrementa    
class DecrementExp(Exp):
  def __init__(self, exp3):
    self.exp3 = exp3
  def accept(self, visitor):
    return visitor.visitDecrementExp(self)


#Exp4 Not
class NotExp(Exp):
  def __init__(self, exp5):
    self.exp5 = exp5
  def accept(self, visitor):
    return visitor.visitNotExp(self)


#Exp5 Soma    
class SomaExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitSomaExp(self)


#Exp6 Subtração    
class SubExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitSubExp(self)

#Exp7 Multi
class MulExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitMulExp(self)


#Exp8 Divisão    
class DivExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitDivExp(self)


#Exp9 Modulo    
class ModuloExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitModuloExp(self)


#Exp10 maior    
class MaiorExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitMaiorExp(self)


#Exp11 menor    
class MenorExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitMenorExp(self)


#Exp12 maiorIgual    
class MaiorIgualExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitMaiorIgualExp(self)


#Exp13 menorIgual    
class MenorIgualExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitMenorIgualExp(self)


#Exp14 Igual    
class IgualExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitIgualExp(self)


#Exp15 Dif
class DifExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitDifExp(self)


#Exp16
class AndExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitAndExp(self)

class OrExp(Exp):
  def __init__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    return visitor.visitOrExp(self)


#Exp17
class CallFuncExp(Exp):
  def __init__(self, chamadaFunc):
    self.chamadaFunc = chamadaFunc
  def accept(self, visitor):
    return visitor.visitChamadaFuncExp(self)

class VarExp(Exp):
  def __init__(self, var):
    self.var = var
  def accept(self, visitor):
    return visitor.visitVarExp(self)

class IntExp(Exp):
  def __init__(self, int):
    self.int = int
  def accept(self, visitor):
    return visitor.visitIntExp(self)

class FloatExp(Exp):
  def __init__(self, float):
    self.float = float
  def accept(self, visitor):
    return visitor.visitFloatExp(self)

class BoolExp(Exp):
  def __init__(self, bool):
    self.bool = bool
  def accept(self, visitor):
    return visitor.visitBoolExp(self)

class IdExp(Exp):
  def __init__(self, ID):
    self.ID = ID
  def accept(self, visitor):
    return visitor.visitIdExp(self)

class ExpressaoExp(Exp):
  def __init__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitExpressaoExp(self)



