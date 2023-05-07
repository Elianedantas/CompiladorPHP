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
  def __int__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    visitor.visitPotExp(self)

#Exp2 Incrementa
class IncrementExp(Exp):
  def __int__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    visitor.visitIncrementExp(self)


#Exp3 Decrementa    
class DecrementExp(Exp):
  def __int__(self, exp3):
    self.exp3 = exp3
  def accept(self, visitor):
    visitor.visitDecrementExp(self)


#Exp4 Not
class NotExp(Exp):
  def __int__(self, exp5):
    self.exp5 = exp5
  def accept(self, visitor):
    visitor.visitNotExp(self)


#Exp5 Soma    
class SomaExp(Exp):
  def __int__(self, exp5, exp6):
    self.exp5 = exp5
    self.exp6 = exp6
  def accept(self, visitor):
    visitor.visitSomaExp(self)


#Exp6 Subtração    
class SubExp(Exp):
  def __int__(self, exp6, exp7):
    self.exp6 = exp6
    self.exp7 = exp7
  def accept(self, visitor):
    visitor.visitSubExp(self)

#Exp7 Multi
class MulExp(Exp):
  def __int__(self, exp7, exp8):
    self.exp7 = exp7
    self.exp8 = exp8
  def accept(self, visitor):
    visitor.visitMulExp(self)


#Exp8 Divisão    
class DivExp(Exp):
  def __int__(self, exp8, exp9):
    self.exp8 = exp8
    self.exp9 = exp9
  def accept(self, visitor):
    visitor.visitDivExp(self)


#Exp9 Modulo    
class ModuloExp(Exp):
  def __int__(self, exp9, exp10):
    self.exp9 = exp9
    self.exp10 = exp10
  def accept(self, visitor):
    visitor.visitModuloExp(self)


#Exp10 maior    
class MaiorExp(Exp):
  def __int__(self, exp10, exp11):
    self.exp10 = exp10
    self.exp11 = exp11
  def accept(self, visitor):
    visitor.visitMaiorExp(self)


#Exp11 menor    
class MenorExp(Exp):
  def __int__(self, exp11, exp12):
    self.exp11 = exp11
    self.exp12 = exp12
  def accept(self, visitor):
    visitor.visitMenorExp(self)


#Exp12 maiorIgual    
class MaiorIgualExp(Exp):
  def __int__(self, exp12, exp13):
    self.exp1 = exp12
    self.exp2 = exp13
  def accept(self, visitor):
    visitor.visitMaiorIgualExp(self)


#Exp13 menorIgual    
class MenorIgualExp(Exp):
  def __int__(self, exp13, exp14):
    self.exp13 = exp13
    self.exp14 = exp14
  def accept(self, visitor):
    visitor.visitMenorIgualExp(self)


#Exp14 Igual    
class IgualExp(Exp):
  def __int__(self, exp14, exp15):
    self.exp14 = exp14
    self.exp15 = exp15
  def accept(self, visitor):
    visitor.visitIgualExp(self)


#Exp15 Dif
class DifExp(Exp):
  def __int__(self, exp15, exp16):
    self.exp15 = exp15
    self.exp16 = exp16
  def accept(self, visitor):
    visitor.visitDifExp(self)


#Exp16
class AndExp(Exp):
  def __int__(self, exp16, exp17):
    self.exp16 = exp16
    self.exp17 = exp17
  def accept(self, visitor):
    visitor.visitAndExp(self)

class OrExp(Exp):
  def __int__(self, exp16, exp17):
    self.exp16 = exp16
    self.exp17 = exp17
  def accept(self, visitor):
    visitor.visitOrExp(self)


#Exp17
class CallFuncExp(Exp):
  def __int__(self, chamadaFunc):
    self.chamadaFunc = chamadaFunc
  def accept(self, visitor):
    visitor.visitChamadaFuncExp(self)

class VarExp(Exp):
  def __int__(self, var):
    self.var = var
  def accept(self, visitor):
    visitor.visitVarExp(self)

class IntExp(Exp):
  def __int__(self, int):
    self.int = int
  def accept(self, visitor):
    visitor.visitIntExp(self)

class FloatExp(Exp):
  def __int__(self, float):
    self.float = float
  def accept(self, visitor):
    visitor.visitFloatExp(self)

class BoolExp(Exp):
  def __int__(self, bool):
    self.bool = bool
  def accept(self, visitor):
    visitor.visitBoolExp(self)

class IdExp(Exp):
  def __int__(self, ID):
    self.ID = ID
  def accept(self, visitor):
    visitor.visitIdExp(self)

class ExpressaoExp(Exp):
  def __int__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    visitor.visitExpressaoExp(self)

