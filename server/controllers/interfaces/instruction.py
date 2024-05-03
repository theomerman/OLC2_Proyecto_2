from abc import ABC, abstractmethod
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.generator import Generator
class Instruction(ABC):
    @abstractmethod
    def run(self,ast: Ast,env:Environment, gen: Generator):
        pass
