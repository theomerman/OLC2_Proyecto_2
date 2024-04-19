from controllers.interfaces.expression import Expression
from controllers.environment.symbol import Symbol
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.types import ExpressionType
from controllers.environment.generator import Generator
from controllers.environment.value import Value

class Primitive(Expression):
    def __init__(self, value, type: ExpressionType, line, column):
        self.value = value
        self.type = type
        self.line = line
        self.column = column
        # self.symbol = Symbol(self.line, self.column, self.value, self.type)
        # self.value_object = Value(value, True, self.type, [],[],[])
        self.value_object = Value(value, type, self.line, self.column)

    def run(self, ast: Ast, env: Environment, gen: Generator):
        # return Symbol(self.line, self.column, self.value, self.type)
        gen.base += 4
        gen.add_li("t0", self.value)
        gen.add_li("t1", str(gen.base))
        gen.add_sw("t0", gen.offset, "t1")
        self.value_object.value = gen.base
        return self.value_object
