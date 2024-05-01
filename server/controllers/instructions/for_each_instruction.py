from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast

class ForEach(Instruction):
    def __init__(self, variable, array, block, line, column):
        self.variable = variable
        self.array = array
        self.block = block
        self.line = line
        self.column = column
    def run(self, ast: Ast, env: Environment):
        print("ForEach")
