from controllers.interfaces.instruction import Instruction
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment

class Empty(Instruction):
    def __init__(self):
        pass
    def run(self, ast: Ast, env: Environment):
        pass
