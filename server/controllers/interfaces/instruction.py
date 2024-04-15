from abc import ABC, abstractmethod
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
class Instruction(ABC):
    @abstractmethod
    def run(self,ast: Ast,env:Environment):
        pass
