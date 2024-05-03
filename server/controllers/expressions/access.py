from icecream import ic
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.generator import Generator


class Access(Expression):
    def __init__(self, id, line, column):
        self.id = id
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        return env.get_variable(ast, self.id)
