from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.generator import Generator


class Assignment(Instruction):
    def __init__(self, id, operator, exp, line, column):
        self.id = id
        self.operator = operator
        self.exp = exp
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        symbol = self.exp.run(ast, env, gen)
        env.update_variable(gen, ast, self.id, self.operator,
                            symbol, self.line, self.column)
