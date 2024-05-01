from controllers.environment.error import Error
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.interfaces.instruction import Instruction

class SyntaxError(Instruction):
    def __init__(self, description: str, env: str, type: str, line, column):
        self.description = description
        self.env = env
        self.type = type
        self.line = line
        self.column = column
    def run(self, ast: Ast, env: Environment):
        ast.add_error(Error(self.description, env.id, self.type, self.line, self.column))
        return None
