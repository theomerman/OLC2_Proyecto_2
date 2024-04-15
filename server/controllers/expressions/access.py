from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast


class Access(Expression):
    def __init__(self, id, line, column):
        self.id = id
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        return env.get_variable(ast, self.id)
