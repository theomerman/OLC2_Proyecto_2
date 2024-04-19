from abc import ABC, abstractmethod
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.symbol import Symbol
from controllers.environment.generator import Generator
from controllers.environment.value import Value
class Expression(ABC):
    @abstractmethod
    def run(self,ast:Ast, env:Environment, gen: Generator) -> Value: pass
