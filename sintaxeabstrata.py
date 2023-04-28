from abc import abstractmethod
from abc import ABCMeta


#functionorcmds : comando
#               | function
#               | comando functionorcmds
#               | function functionorcmds
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

