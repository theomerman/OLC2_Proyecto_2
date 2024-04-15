from controllers.interfaces.expression import Expression
from controllers.environment.symbol import Symbol
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.types import ExpressionType


class Primitive(Expression):
    def __init__(self, value, type: ExpressionType, line, column):
        self.value = value
        self.type = type
        self.line = line
        self.column = column
        self.symbol = Symbol(self.line, self.column, self.value, self.type)

    def run(self, ast: Ast, env: Environment):
        # return Symbol(self.line, self.column, self.value, self.type)
        return self.symbol
