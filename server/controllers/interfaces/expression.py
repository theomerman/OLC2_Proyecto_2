from abc import ABC, abstractmethod
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.symbol import Symbol
class Expression(ABC):
    @abstractmethod
    def run(self,ast:Ast, env:Environment) -> Symbol: pass
