from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error


class Assignment(Instruction):
    def __init__(self, id, operator, exp, line, column):
        self.id = id
        self.operator = operator
        self.exp = exp
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        symbol = self.exp.run(ast, env)
        env.update_variable(ast, self.id, self.operator,
                            symbol, self.line, self.column)
